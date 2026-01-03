本节将指导你如何在不同的平台上移植SGL图形库

SGL移植步骤
-------------

PC模拟器
~~~~~~~~~~~~~~~
1. 安装make工具，确保make命令可用
2. 安装MinGW工具链，确保gcc命令可用，这里推荐一个gcc工具链地址：(https://github.com/niXman/mingw-builds-binaries/releases/download/13.2.0-rt_v11-rev0/x86_64-13.2.0-release-posix-seh-ucrt-rt_v11-rev0.7z)
3. 安装git工具，确保git命令可用
4. 安装git工具后，打开git命令行，依次输入如下命令，即可完成SGL的移植：
   .. code-block:: bash
      git clone https://github.com/sgl-org/sgl-port-windows.git
      cd sgl-port-windows
      git submodule init
      git submodule update --remote
      cd demo
      make -j8
      make run


MCU平台
~~~~~~~~~~~~~~~


Linux FB平台
~~~~~~~~~~~~~~~


KEIL IDE使用
~~~~~~~~~~~~~~~
