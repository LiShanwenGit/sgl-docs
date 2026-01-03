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
```{note}
这是一个提示信息。
```

```{warning}
这是一个警告信息！
```

```{tip}
这是一个小技巧。
```

```{danger}
危险操作！可能导致系统崩溃。
```


### MCU平台
（此处填写MCU平台的移植步骤，例如STM32、GD32等平台的具体操作）
1.  准备目标MCU的开发环境（如Keil、STM32CubeMX）
2.  导入SGL核心库源码（include/、src/目录）
3.  适配MCU的显示驱动、GPIO驱动
4.  编译并下载验证

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
