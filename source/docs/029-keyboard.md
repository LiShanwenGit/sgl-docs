## keyboard控件
创建一个keyboard控件，使用如下代码：
```c
sgl_obj_t *keyboard = sgl_keyboard_create(NULL);
sgl_obj_set_pos(keyboard, 0, 300);
sgl_obj_set_size(keyboard, 480, 200);
```
上面代码在默认的活动页面上创建了一个大小为480x200的Keyboard控件，并设置其位置为0,300。

### 设置Keyboard颜色
使用sgl_keyboard_set_color()函数设置Keyboard的颜色，如下：
```c
sgl_obj_t *keyboard = sgl_keyboard_create(NULL);
sgl_obj_set_pos(keyboard, 0, 300);
sgl_obj_set_size(keyboard, 480, 200);
sgl_keyboard_set_color(keyboard, SGL_COLOR_WHITE);
```

### 设置Keyboard选中颜色
使用sgl_keyboard_set_selected_color()函数设置Keyboard的选中颜色，如下：
```c
sgl_keyboard_set_selected_color(keyboard, SGL_COLOR_BLUE);
```

### 设置Keyboard字体
使用sgl_keyboard_set_font()函数设置Keyboard的字体，如下：
```c
sgl_keyboard_set_font(keyboard, &consolas24);
```

### 设置Keyboard透明度
使用sgl_keyboard_set_alpha()函数设置Keyboard的透明度，如下：
```c
sgl_keyboard_set_alpha(keyboard, 128);
```

### 设置Keyboard按键回调
使用sgl_keyboard_set_callback()函数设置Keyboard的按键回调，如下：
```c
void on_key_press(char key) {
    // 处理按键事件
}
sgl_keyboard_set_callback(keyboard, on_key_press);
```
