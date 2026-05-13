## numberkbd控件
创建一个numberkbd控件，使用如下代码：
```c
sgl_obj_t *kbd = sgl_numberkbd_create(NULL);
sgl_obj_set_pos(kbd, 0, 300);
sgl_obj_set_size(kbd, 480, 200);
```
上面代码在默认的活动页面上创建了一个大小为480x200的NumberKbd控件，并设置其位置为0,300。

### 设置NumberKbd颜色
使用sgl_numberkbd_set_color()函数设置NumberKbd的颜色，如下：
```c
sgl_obj_t *kbd = sgl_numberkbd_create(NULL);
sgl_obj_set_pos(kbd, 0, 300);
sgl_obj_set_size(kbd, 480, 200);
sgl_numberkbd_set_color(kbd, SGL_COLOR_WHITE);
```

### 设置NumberKbd选中颜色
使用sgl_numberkbd_set_selected_color()函数设置NumberKbd的选中颜色，如下：
```c
sgl_numberkbd_set_selected_color(kbd, SGL_COLOR_BLUE);
```

### 设置NumberKbd字体
使用sgl_numberkbd_set_font()函数设置NumberKbd的字体，如下：
```c
sgl_numberkbd_set_font(kbd, &consolas24);
```

### 设置NumberKbd透明度
使用sgl_numberkbd_set_alpha()函数设置NumberKbd的透明度，如下：
```c
sgl_numberkbd_set_alpha(kbd, 128);
```

### 设置NumberKbd按键回调
使用sgl_numberkbd_set_callback()函数设置NumberKbd的按键回调，如下：
```c
void on_number_press(char key) {
    // 处理数字按键事件
}
sgl_numberkbd_set_callback(kbd, on_number_press);
```
