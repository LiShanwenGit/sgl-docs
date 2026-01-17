## Button控件
创建一个Button控件，使用如下代码：
```c
sgl_obj_t *button = sgl_button_create(NULL);
/* 设置位置 */ 
sgl_obj_set_pos(button, 400, 100);
/* 设置大小 */
sgl_obj_set_size(button, 100, 50);
/* 设置颜色 */
sgl_button_set_color(button, SGL_COLOR_RED);
/* 设置边框颜色 */
sgl_button_set_border_color(button, SGL_COLOR_BLUE);
/* 设置边框宽度 */
sgl_button_set_border_width(button, 5);
/* 设置圆角半径 */
sgl_button_set_radius(button, 25);
/* 设置文本 */
sgl_button_set_text(button, "Button");
/* 设置透明度 */
sgl_button_set_alpha(button, 255);
```
