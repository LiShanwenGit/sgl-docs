# 文件名：docs/start.rst
快速开始（Getting Started）
==========================

本节将指导你快速完成 SGL 库的环境准备、安装部署和第一个简单示例程序。

一、环境要求
------------
支持的硬件与软件环境如下（最低配置）：
* 处理器：ARM Cortex-M0/M3 及以上，或 51 系列增强型处理器
* 编译器：Keil MDK 5.28+、GCC ARM Embedded 9.2+、IAR Embedded Workbench 8.3+
* 操作系统：无（裸机运行），或嵌入式 Linux（内核 3.10+）
* 存储空间：至少 16KB Flash（程序存储）、2KB RAM（运行时内存）

二、安装 SGL 库
--------------
### 2.1 从 GitHub 克隆代码仓库
打开终端（或 Git Bash），执行以下命令克隆最新代码：
.. code-block:: bash

   # 克隆 SGL 官方仓库
   git clone https://github.com/sgl-org/sgl.git
   # 进入仓库目录
   cd sgl

### 2.2 手动下载安装
如果无法使用 Git，可直接从 GitHub 下载源码包：
1. 访问 SGL GitHub 地址：https://github.com/sgl-org/sgl
2. 点击「Code」按钮，选择「Download ZIP」
3. 解压下载的 ZIP 包到你的项目目录下
4. 解压后目录结构如下：
   .. code-block:: text

      sgl/
      ├── include/  # 头文件目录
      ├── src/      # 源文件目录
      ├── examples/ # 示例程序目录
      └── docs/     # 文档目录

三、第一个 SGL 示例（Hello World）
--------------------------------
以下是一个最简单的 SGL 示例，用于在屏幕上显示「Hello SGL!」文字。

### 3.1 示例代码
.. code-block:: c

   #include "sgl/sgl.h"
   #include "sgl/sgl_text.h"

   int main(void)
   {
       // 1. 初始化 SGL 库
       sgl_init();
       
       // 2. 初始化显示设备
       sgl_display_init();
       
       // 3. 清屏（白色背景）
       sgl_clear(SGL_COLOR_WHITE);
       
       // 4. 设置文字颜色（黑色）和字体大小
       sgl_text_set_color(SGL_COLOR_BLACK);
       sgl_text_set_font_size(SGL_FONT_SIZE_16);
       
       // 5. 在屏幕坐标 (10, 10) 处绘制文字
       sgl_text_draw(10, 10, "Hello SGL!");
       
       // 6. 刷新显示缓冲区，将内容显示到屏幕
       sgl_display_refresh();
       
       while(1)
       {
           // 主循环
       }
       return 0;
   }

### 3.2 编译与运行
1. 将 SGL 库的 `include` 目录添加到编译器的头文件搜索路径
2. 将 SGL 库的 `src` 目录下所有 `.c` 文件添加到你的项目工程中
3. 编译项目，生成可执行文件（或固件）
4. 将固件下载到目标硬件设备，上电运行
5. 成功后，屏幕将显示清晰的「Hello SGL!」文字

四、常见问题排查
----------------
1. 编译报错「找不到 sgl.h」：检查头文件搜索路径是否正确配置
2. 下载后屏幕无显示：检查 SGL 初始化函数是否正确调用，显示设备接线是否正常
3. 文字显示乱码：检查字体文件是否已添加到项目，字体大小设置是否合法

五、下一步
----------
完成本快速开始后，你可以：
1. 查看 `docs/page.rst` 了解 SGL 库的页面管理功能
2. 参考 `examples/` 目录下的完整示例程序，学习更多高级功能
3. 加入 SGL 官方 QQ 群（544602724），获取更多技术支持
