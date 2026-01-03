本节将指导你如何在不同的平台上移植SGL图形库

## SGL移植步骤

### PC模拟器
1.  安装make工具，确保make命令可用    
2.  安装MinGW工具链，确保gcc命令可用，这里推荐一个gcc工具链地址：[MinGW 13.2.0 工具链](https://github.com/niXman/mingw-builds-binaries/releases/download/13.2.0-rt_v11-rev0/x86_64-13.2.0-release-posix-seh-ucrt-rt_v11-rev0.7z)

3.  安装git工具，确保git命令可用        
4.  安装git工具后，打开git命令行，依次输入如下命令，即可完成SGL的移植：      
    ```bash
        git clone https://github.com/sgl-org/sgl-port-windows.git
        cd sgl-port-windows
        git submodule init
        git submodule update --remote
        cd demo
        make -j8
        make run
    ```
5. 执行完毕后，即可看到一个窗口，显示SGL的示例程序运行效果        
```{tip}
如果想修改模拟器的分辨率，可以在`sgl_port_sdl2.c`文件中修改`CONFIG_SGL_PANEL_WIDTH`和`CONFIG_SGL_PANEL_HEIGHT`的值
```

### MCU平台
1. 下载SGL发布版本代码：[SGL 20260101.zip](https://github.com/sgl-org/sgl/archive/refs/tags/20260101.zip)
2. 解压后如下文件结构：
```
source
├─sgl.h                 SGL头文件
├─sgl_config.h          SGL配置文件
├─core                  核心库文件
├─draw                  底层绘制库文件
├─fonts                 字体库文件
├─include               头文件
├─misc                  杂项文件
├─mm                    内存管理文件
│  ├─lwmem              lwmem内存管理库文件
│  ├─other              其他内存管理库文件
│  └─tlsf               tlsf内存管理库文件
└─widgets               控件库文件
    ├─2dball               2D小球
    ├─arc                  弧线
    ├─button               按钮
    ├─checkbox             复选框
    ├─circle               圆形
    ├─dropdown             下拉框
    ├─ext_img              扩展图片
    ├─icon                 图标
    ├─keyboard             键盘
    ├─label                标签
    ├─led                  LED
    ├─line                 线段
    ├─msgbox               消息框
    ├─numberkbd            数字键盘
    ├─polygon              多边形
    ├─progress             进度条
    ├─rectangle            矩形
    ├─ring                 圆形环
    ├─scope                示波器
    ├─scroll               滚动条
    ├─slider               滑块
    ├─switch               开关
    ├─textbox              文本框
    ├─textline             文本行
    └─unzip_image          解压图片

```
3. 将SGL的所有代码拷贝到MCU的工程文件中，并添加所有文件，注意：对于mm目录下的文件，只需要添加lwmem目录下的文件，如果你的项目中已经有动态内存管理函数，则不需要添加mm目录下的文件，自己定义`sgl_mm_init`，`sgl_malloc`，`sgl_free`函数即可。
4. 添加SGL的所有文件后，请修改`sgl_config.h`文件，用于适配你的MCU平台，下面是一个示例：
```c
#ifndef  __CONFIG_H__
#define  __CONFIG_H__

#define    CONFIG_SGL_PANEL_PIXEL_DEPTH       16          //颜色深度，这里是16位，即RGB565
#define    CONFIG_SGL_SYSTICK_MS              10          //SGL图形刷新事件间隔，这里设置为10ms
#define    CONFIG_SGL_EVENT_QUEUE_SIZE        16          //事件队列大小，这里设置为16
#define    CONFIG_SGL_DIRTY_AREA_NUM_MAX      16          //脏区域最大数量，这里设置为16
#define    CONFIG_SGL_ANIMATION               1           //是否启用动画，这里启用动画
#define    CONFIG_SGL_DEBUG                   1           //是否启用日志，这里启用日志，项目发布时，请关闭日志
#define    CONFIG_SGL_LOG_COLOR               1           //是否启用日志颜色，这里启用日志颜色
#define    CONFIG_SGL_LOG_LEVEL               0           //日志等级，0为全部输出，1为错误输出，2为警告输出，3为信息输出，4为调试输出
#define    CONFIG_SGL_OBJ_USE_NAME            0           //是否启用对象名称，这里不启用对象名称
#define    CONFIG_SGL_FONT_COMPRESSED         1           //是否启用字体压缩，这里启用字体压缩
#define    CONFIG_SGL_BOOT_LOGO               0           ///是否启用启动logo，这里不启用启动logo
#define    CONFIG_SGL_BOOT_ANIMATION          0           //是否启用启动动画，这里不启用启动动画
#define    CONFIG_SGL_HEAP_ALGO               lwmem       //内存管理算法，这里选择lwmem
#define    CONFIG_SGL_HEAP_MEMORY_SIZE        10240       //内存大小，这里设置为10KB
#define    CONFIG_SGL_FONT_SONG23             0           //是否启用宋体23号字体, 默认关闭
#define    CONFIG_SGL_FONT_CONSOLAS14         0           //是否启用Consolas14号字体, 默认关闭
#define    CONFIG_SGL_FONT_CONSOLAS23         0           //是否启用Consolas23号字体, 默认关闭
#define    CONFIG_SGL_FONT_CONSOLAS24         1           //是否启用Consolas24号字体, 默认开启
#define    CONFIG_SGL_FONT_CONSOLAS32         0           //是否启用Consolas32号字体, 默认关闭
#define    CONFIG_SGL_FONT_CONSOLAS24_COMPRESS     1      //是否启用Consolas24号字体压缩，这里启用字体压缩

#endif  //!__CONFIG_H__
```
```{tip}
在刚开始移植SGL时，最好开启`CONFIG_SGL_DEBUG`这个值，这样可以使用串口输出调试日志，如果出现问题，可以快速定位原因。
```
5. 对接屏幕底层驱动代码
在你的main函数中添加如下代码：
```c
#include "sgl.h"

#define PANEL_WIDTH     320
#define PANEL_HEIGHT    240

static sgl_color_t panel_buffer[PANEL_WIDTH * 10];

bool panel_flush_area(int16_t x1, int16_t y1, int16_t x2, int16_t y2, sgl_color_t *src)
{
    uint16_t w = x2 - x1 + 1;
    uint16_t h = y2 - y1 + 1;
    tft_set_win(x1, y1, x2, y2);
	GPIO_WriteBit(SPI_DC_PORT, SPI_DC_PIN, 1);
	SPI1_WriteMultByte((uint8_t*)src, w * h * 2);
    return true;
}

void uart_put_string(const char *str)
{
   /* 发送串口数据，将str中的数据发送出去 */
}

//你的SysTick中断处理函数，定时时间为1ms
void SysTick_Handler(void)
{
    sgl_tick_inc(1);
}

int main(void)
{
    sgl_device_fb_t fb_dev = {
        .xres = PANEL_WIDTH,
        .yres = PANEL_HEIGHT,
        .xres_virtual = PANEL_WIDTH,
        .yres_virtual = PANEL_HEIGHT,
        .flush_area = panel_flush_area,
        .buffer[0] = panel_buffer,
        .buffer_size = SGL_ARRAY_SIZE(panel_buffer), 
    };

    // 注册Framebuffer设备
    sgl_device_fb_register(&fb_dev);
    // 注册日志设备，可选
    sgl_device_log_register(uart_put_string);

    tft_init();

    sgl_init();

    //添加一个测试代码
    sgl_obj_t *label = sgl_label_create(NULL);
    sgl_obj_set_size(label, PANEL_WIDTH, 30);
    sgl_obj_set_pos_align(label, SGL_ALIGN_CENTER);
    sgl_label_set_font(label, &consolas24);
    sgl_label_set_text(label, "Hello SGL!");

    while (true) {
        sgl_task_handle();
    }
    return 0;
}

```
上面的过程中定义了一个sgl_device_fb_t结构体，并且初始化了一些主要的参数，参数的含义如下： 
- `xres`: 屏幕的宽度          
- `yres`: 屏幕的高度            
- `xres_virtual`: 屏幕的虚拟宽度     
- `yres_virtual`: 屏幕的虚拟高度       
- `flush_area`：刷新区域函数，用于刷新指定区域           
- `buffer[0]`：帧缓冲区指针，指向帧缓冲区地址处，如何需要双帧缓冲区，则需要设置`buffer[1]`        
- `buffer_size`：帧缓冲区大小，单位：缓冲区中像素点的个数          
           
panel_flush_area函数用于刷新指定区域，参数为：
- `x1`：区域左上角X坐标
- `y1`：区域左上角Y坐标
- `x2`：区域右下角X坐标
- `y2`：区域右下角Y坐标
- `src`：区域数据指针
- `return`：发送完成返回true，发送未完成返回false

```{tip}
如果没有使用DMA发送数据，则直接返回true即可，如果使用DMA发送数据，则需要先检测下DMA是否空闲，如果是空闲的，则发送数据后，返回true，如果DMA未空闲，则返回false。
例如：
使用DMA发送数据：   

```c
bool panel_flush_area(int16_t x1, int16_t y1, int16_t x2, int16_t y2, sgl_color_t *src)            
{             
    if (DMA_IS_BUSY()) {          
        return false;        
    }              
    DMA_SendData(src, (x2 - x1 + 1) * (y2 - y1 + 1)* sizeof(sgl_color_t));          
    return true;            
}  
```
```        
                  
编译后，烧录到开发板上，即可看到屏幕显示“Hello SGL!”，整个移植主要只有四件事：    
- 1. 调用sgl_device_fb_register()函数注册FB设备      
- 2. 调用sgl_device_log_register()函数注册日志设备，可选        
- 3. 调用sgl_init()函数初始化SGL框架       
- 4. 在滴答中断中调用sgl_tick_inc()函数，定时为1ms    
       
```{tip}
sgl_tick_inc()函数不是必须要在滴答中断中调用，你也可以在轮询或者线程中调用，每1ms调用一次即可。
```
              
### Linux FB平台
（此处填写Linux FrameBuffer平台的移植步骤）
1.  确保Linux系统启用FrameBuffer功能
2.  安装依赖库（如libpng、freetype）
3.  克隆Linux平台移植仓库并编译
4.  运行demo验证显示效果

### KEIL IDE使用
（此处填写KEIL IDE下的SGL使用与移植步骤）
1.  新建或打开已有KEIL工程
2.  添加SGL库的.h头文件路径和.c源文件
3.  配置工程编译选项（优化等级、芯片型号等）
4.  适配KEIL工程的底层驱动，编译下载
