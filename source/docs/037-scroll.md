## scroll控件
创建一个scroll控件，使用如下代码：
```c
sgl_obj_t *scroll = sgl_scroll_create(NULL);
sgl_obj_set_pos(scroll, 250, 100);
sgl_obj_set_size(scroll, 20, 200);
```
上面代码在默认的活动页面上创建了一个大小为20x200的Scroll控件，并设置其位置为250,100。

### 设置Scroll背景颜色
使用sgl_scroll_set_bg_color()函数设置Scroll的背景颜色，如下：
```c
sgl_obj_t *scroll = sgl_scroll_create(NULL);
sgl_obj_set_pos(scroll, 250, 100);
sgl_obj_set_size(scroll, 20, 200);
sgl_scroll_set_bg_color(scroll, SGL_COLOR_GRAY);
```

### 设置Scroll滑块颜色
使用sgl_scroll_set_slider_color()函数设置Scroll的滑块颜色，如下：
```c
sgl_scroll_set_slider_color(scroll, SGL_COLOR_BLUE);
```

### 设置Scroll圆角
使用sgl_scroll_set_radius()函数设置Scroll的圆角，如下：
```c
sgl_scroll_set_radius(scroll, 10);
```

### 设置Scroll方向
使用sgl_scroll_set_direct()函数设置Scroll的方向，如下：
```c
sgl_scroll_set_direct(scroll, SGL_DIRECT_VERTICAL);
```
Scroll支持以下方向：
- SGL_DIRECT_HORIZONTAL：水平方向
- SGL_DIRECT_VERTICAL：垂直方向

### 设置Scroll值
使用sgl_scroll_set_value()函数设置Scroll的值，如下：
```c
sgl_scroll_set_value(scroll, 50);
```

### 获取Scroll值
使用sgl_scroll_get_value()函数获取Scroll的当前值，如下：
```c
uint8_t value = sgl_scroll_get_value(scroll);
```
