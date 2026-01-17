## Label控件
```c
sgl_obj_t *label = sgl_label_create(NULL);
/* 设置位置 */ 
sgl_obj_set_pos(label, 400, 100);
/* 设置大小 */
sgl_obj_set_size(label, 100, 50);
/* 设置字体 */
sgl_label_set_font(label, &consolas24);
/* 设置文本 */
sgl_label_set_text(label, "label test");
```
