## slider控件
创建一个slider控件，使用如下代码：
```c
sgl_obj_t *slider = sgl_slider_create(NULL);
sgl_obj_set_pos(slider, 250, 100);
sgl_obj_set_size(slider, 200, 30);
```
上面代码在默认的活动页面上创建了一个大小为200x30的Slider控件，并设置其位置为250,100。

### 设置Slider填充颜色
使用sgl_slider_set_fill_color()函数设置Slider的填充颜色，如下：
```c
sgl_obj_t *slider = sgl_slider_create(NULL);
sgl_obj_set_pos(slider, 250, 100);
sgl_obj_set_size(slider, 200, 30);
sgl_slider_set_fill_color(slider, SGL_COLOR_RED);
```

### 设置Slider轨道颜色
使用sgl_slider_set_track_color()函数设置Slider的轨道颜色，如下：
```c
sgl_slider_set_track_color(slider, SGL_COLOR_GRAY);
```

### 设置Slider旋钮颜色
使用sgl_slider_set_knob_color()函数设置Slider的旋钮颜色，如下：
```c
sgl_slider_set_knob_color(slider, SGL_COLOR_BLUE);
```

### 设置Slider方向
使用sgl_slider_set_direct()函数设置Slider的方向，如下：
```c
sgl_slider_set_direct(slider, SGL_DIRECT_HORIZONTAL);
```
Slider支持以下方向：
- SGL_DIRECT_HORIZONTAL：水平方向
- SGL_DIRECT_VERTICAL：垂直方向

### 设置Slider圆角
使用sgl_slider_set_radius()函数设置Slider的圆角，如下：
```c
sgl_slider_set_radius(slider, 15);
```

### 设置Slider旋钮厚度
使用sgl_slider_set_thickness()函数设置Slider的旋钮厚度，如下：
```c
sgl_slider_set_thickness(slider, 20);
```

### 设置Slider值
使用sgl_slider_set_value()函数设置Slider的值，如下：
```c
sgl_slider_set_value(slider, 50);
```

### 获取Slider值
使用sgl_slider_get_value()函数获取Slider的当前值，如下：
```c
uint8_t value = sgl_slider_get_value(slider);
```

### 设置Slider边框宽度
使用sgl_slider_set_border_width()函数设置Slider的边框宽度，如下：
```c
sgl_slider_set_border_width(slider, 2);
```
