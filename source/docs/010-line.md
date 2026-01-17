## Line控件
line控件用于显示线，使用如下代码：
```c
sgl_obj_t *line = sgl_line_create(NULL);
sgl_line_set_pos(line, 10, 10, 102, 105);
sgl_line_set_width(line, 5);
sgl_line_set_color(line, SGL_COLOR_BLACK);
```
上面的代码中，sgl_line_set_pos()函数设置线的起始位置和结束位置，sgl_line_set_width()函数设置线的宽度，sgl_line_set_color()函数设置线的颜色，效果如下：          
![alt text](imgs/line/img-1.jpg)              

sgl_line_set_pos函数的参数说明如下：
```c
void sgl_line_set_pos(sgl_obj_t *obj, int16_t x1, int16_t y1, int16_t x2, int16_t y2)
```
- obj: 线对象
- x1: 线起始位置的x坐标
- y1: 线起始位置的y坐标
- x2: 线结束位置的x坐标
- y2: 线结束位置的y坐标

