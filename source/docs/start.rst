快速开始
========

本章将引导你完成 SGL 的基本配置和第一个“Hello World”示例，支持以下平台：

- PC 模拟器（Linux / Windows）
- 嵌入式 MCU（如 STM32）
- Linux Framebuffer（无 GUI 系统）

安装 SGL
---------

SGL 无需复杂安装，只需克隆代码仓库：

.. code-block:: bash

   git clone https://github.com/sgl-org/sgl.git
   cd sgl

SGL 是一个纯 C 库，无外部依赖，直接包含源码即可使用。

选择你的平台
-------------

根据你的目标平台，进入对应的子目录并编译示例：

PC 模拟器
~~~~~~~~~

适用于开发和调试。依赖 SDL2（仅用于模拟显示）。

.. code-block:: bash

   cd examples/pc_simulator
   make
   ./sgl_demo

> **提示**：在 Ubuntu/Debian 上安装 SDL2：
>
> .. code-block:: bash
>
>    sudo apt install libsdl2-dev

MCU 平台
~~~~~~~~

以 STM32 为例（需 HAL 库和 SPI/I2C 驱动）：

1. 将 ``src/`` 目录复制到你的工程中。
2. 实现底层接口（见 ``port/sgl_port.h``）：
   - 显存写入（如 LCD 控制器驱动）
   - 时间获取（用于动画）
   -
