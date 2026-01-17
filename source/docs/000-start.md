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

#define    CONFIG_SGL_FBDEV_PIXEL_DEPTH       16          //颜色深度，这里是16位，即RGB565
#define    CONFIG_SGL_FBDEV_ROTATION          0           //屏幕旋转角度，软件旋转，这里设置为0度，即不做旋转
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

void panel_flush_area(sgl_area_t *area, sgl_color_t *src)
{
    uint16_t w = area->x2 - area->x1 + 1;
    uint16_t h = area->y2 - area->y1 + 1;
    tft_set_win(area->x1, area->y1, area->x2, area->y2);
    GPIO_WriteBit(SPI_DC_PORT, SPI_DC_PIN, 1);
    SPI1_WriteMultByte((uint8_t*)src, w * h * sizeof(sgl_color_t));
    /* 调用sgl_fbdev_flush_ready()函数，告诉SGL框架，刷新完成，可以继续处理下一帧处理 */ 
    sgl_fbdev_flush_ready();
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
    sgl_fbinfo_t fbinfo = {
        .xres = PANEL_WIDTH,
        .yres = PANEL_HEIGHT,
        .flush_area = panel_flush_area,
        .buffer[0] = panel_buffer,
        .buffer_size = SGL_ARRAY_SIZE(panel_buffer), 
    };

    // 注册日志设备，可选
    sgl_logdev_register(uart_put_string);
    // 注册Framebuffer设备
    sgl_fbdev_register(&fbinfo);

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
- `flush_area`：刷新区域函数，用于刷新指定区域           
- `buffer[0]`：帧缓冲区指针，指向帧缓冲区地址处，如何需要双帧缓冲区，则需要设置`buffer[1]`        
- `buffer_size`：帧缓冲区大小，单位：缓冲区中像素点的个数          
           
panel_flush_area函数用于刷新指定区域，参数为：
- `area`：区域结构体指针，包含区域左上角和右下角的坐标
    `x1`：区域左上角X坐标
    `y1`：区域左上角Y坐标
    `x2`：区域右下角X坐标
    `y2`：区域右下角Y坐标
- `src`：区域数据指针
panel_flush_area函数必须调用sgl_fbdev_flush_ready()函数，用来告诉SGL框架，刷新完成，可以继续处理下一帧处理。

```{tip}
如果没有使用DMA发送数据，则直接返回true即可，如果使用DMA发送数据，则需要先检测下DMA是否空闲，如果是空闲的，则发送数据后，返回true，如果DMA未空闲，则返回false。
例如：
使用DMA发送数据：   

```c
void dma_complete_handler(void)
{
    sgl_fbdev_flush_ready();
}

void panel_flush_area(sgl_area_t *area, sgl_color_t *src)          
{
    if (DMA_IS_BUSY()) {
        return;
    }
    DMA_SendData(src, (x2 - x1 + 1) * (y2 - y1 + 1)* sizeof(sgl_color_t));        
}
```
当然，对于使用DMA发送数据时，请使用双缓冲，即添加一个缓冲区，即`buffer[1]`，大小和`buffer[0]`一样，即`buffer_size`
                  
编译后，烧录到开发板上，即可看到屏幕显示“Hello SGL!”，整个移植主要只有四件事：    
- 1. 调用sgl_fbdev_register()函数注册FB设备      
- 2. 调用sgl_logdev_register()函数注册日志设备，可选        
- 3. 调用sgl_init()函数初始化SGL框架       
- 4. 在滴答中断中调用sgl_tick_inc()函数，定时为1ms    
       
```{tip}
sgl_tick_inc()函数不是必须要在滴答中断中调用，你也可以在轮询或者线程中调用，每1ms调用一次即可。
```
              
### KEIL IDE使用
#### 1.创建工程
1. 新建一个`SGL_STM32F103`目录，然后创建一个`sgl`目录，然后将`sgl`源码的`source`目录下的所有文件复制到`SGL_STM32F103/sgl/`目录下。      
    ![alt text](imgs/mdk5/image-1.png)

2. 打开`MDK5`软件，新建一个名为`SGL_STM32F103`的工程，保存到`SGL_STM32F103`目录下，点击【保存】。      
    ![alt text](imgs/mdk5/img-2.jpg)


3. 此时会进入芯片选择界面，然后选择STM32F103C8芯片，点击【OK】      
    ![alt text](imgs/mdk5/img-3.jpg)

4. 此时会进入`Manage Run-Time Environment`界面，勾选`CMSIS`和`Startup`，然后点击【OK】。       
    ![alt text](imgs/mdk5/img-4.jpg)

5. 点击文件扩展管理器:      
    ![alt text](imgs/mdk5/img-5.jpg)

    然后新建`sgl`和`example`目录结构，然后在`sgl`结构中，将`sgl/core/`目录下所有c文件添加，将`sgl/draw/`目录下所有c文件添加，将`sgl/fonts/`目录下所有c文件添加，将`sgl/source/mm/lwmem/`目录下的所有c文件添加，将`sgl/source/widgets/`目录下的所有文件添加，添加完毕后，目录结构如下：           
    ![alt text](imgs/mdk5/img-6.jpg)

6. 新建一个`main.c`文件，然后保存到`example`文件夹下：            
    ![alt text](imgs/mdk5/img-7.jpg)

    然后输入如下代码：          
    ```c
    #include "stm32f10x.h"
    #include "sgl.h"

    #define  PANEL_WIDTH    240
    #define  PANEL_HEIGHT   240
    sgl_color_t panel_buffer[PANEL_WIDTH * 10];

    /* 系统时钟中断服务函数，设置为1ms中断一次 */
    void systick_handler(void)
    {
        sgl_tick_inc(1);
    }

    void demo_panel_flush_area(sgl_area_t *area, sgl_color_t *src)
    {
        /* set flush windows address */
        tft_set_win(area->x1, area->y1, area->x2, area->y2);    
        SPI1_WriteMultByte((uint8_t*)src, (area->x2 - area->x1 + 1) * (area->y2 - area->y1 + 1) * sizeof(sgl_color_t));
        /* 调用sgl_fbdev_flush_ready()函数，告诉SGL框架，刷新完成，可以继续处理下一帧处理 */ 
        sgl_fbdev_flush_ready();
    }

    void UART1_SendString(const char *str)
        {
        while (*str != '\0') {
            while ((USART1->SR & USART_SR_TXE) == 0);
            USART1->DR = (uint8_t)(*str++);
        }
        while ((USART1->SR & USART_SR_TC) == 0);
    }

    int main(void)
    {
        sgl_fbinfo_t fbinfo = {
            .xres = PANEL_WIDTH,
            .yres = PANEL_HEIGHT,
            .flush_area = panel_flush_area,
            .buffer[0] = panel_buffer,
            .buffer_size = SGL_ARRAY_SIZE(panel_buffer), 
        };
        // 注册日志设备，可选
        sgl_logdev_register(UART1_SendString);
        // 注册Framebuffer设备
        sgl_fbdev_register(&fbinfo);

        //USART1_GPIO_Config();
        //USART1_Config();

        /* init sgl */
        sgl_init();

        while(1) {
            sgl_task_handle();
        }
        
        return 0;
    }
    ```

7. 编辑`sgl_config.h`文件，修改内容如下：
    ```c
    #define    CONFIG_SGL_FBDEV_PIXEL_DEPTH       16          //颜色深度，这里是16位，即RGB565
    #define    CONFIG_SGL_FBDEV_ROTATION          0           //屏幕旋转角度，软件旋转，这里设置为0度，即不做旋转
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
    ```
#### 2.配置编译选项
1. 打开`Options for Target`窗口，然后找到`Target`选项:             
    ![alt text](imgs/mdk5/img-8.jpg)

    选择`V6`版本编译器
2. 点击`C/C++(AC6)`选项`，然后选择如下配置：              
    ![alt text](imgs/mdk5/img-9.jpg)

   然后添加头文件路径，将`sgl/include`添加到`Include Path`中，将`sgl`目录添加到`Include Path`中。                   
    ![alt text](imgs/mdk5/img-10.jpg)

#### 3.创建一个简单的demo
在`main.c`中添加如下代码：
```c
int main(void)
{
    ...
    sgl_init();
    ...

    /* 添加一个按钮 */
    sgl_obj_t *button = sgl_button_create(NULL);
    sgl_obj_set_pos(button, 20, 20);
    sgl_obj_set_size(button, 200, 100);
    sgl_obj_set_style(button, SGL_STYLE_RADIUS, 50);
    sgl_obj_set_style(button, SGL_STYLE_BORDER_WIDTH, 2);
    sgl_obj_set_style(button, SGL_STYLE_BORDER_COLOR, SGL_COLOR(SGL_BLACK));

    while(1) {
        sgl_task_handle();
    }

    return 0;
}
```
然后点击编译按钮，编译成功后，烧录到开发板中即可。    
![alt text](imgs/mdk5/img-11.jpg)

```{note}
如果发现颜色显示不正确，请查看屏幕驱动芯片手册，是否存在16位颜色交换模式，如果存在，可以使用下面两种方式任意一种解决：
1. 修改`sgl_config.h`文件，将`CONFIG_SGL_COLOR16_SWAP`定义为1，使用软件交换颜色
2. 查看屏幕驱动芯片手册，设置16位颜色交换模式。
```
