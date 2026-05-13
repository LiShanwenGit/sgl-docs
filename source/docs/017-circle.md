## circle控件
创建一个circle控件，使用如下代码：
```c
sgl_obj_t *circle = sgl_circle_create(NULL);
sgl_obj_set_pos(circle, 250, 100);
sgl_obj_set_size(circle, 100, 100);
```
上面代码在默认的活动页面上创建了一个大小为100x100的Circle控件，并设置其位置为250,100。

### 设置Circle颜色
使用sgl_circle_set_color()函数设置Circle的颜色，如下：
```c
sgl_obj_t *circle = sgl_circle_create(NULL);
sgl_obj_set_pos(circle, 250, 100);
sgl_obj_set_size(circle, 100, 100);
sgl_circle_set_color(circle, SGL_COLOR_RED);
```

### 设置Circle半径
使用sgl_circle_set_radius()函数设置Circle的半径，如下：
```c
sgl_circle_set_radius(circle, 40);
```

### 设置Circle透明度
使用sgl_circle_set_alpha()函数设置Circle的透明度，如下：
```c
sgl_circle_set_alpha(circle, 128);
```

### 设置Circle背景图片
使用sgl_circle_set_pixmap()函数设置Circle的背景图片，如下：
```c
extern const sgl_pixmap_t circle_pixmap;
sgl_circle_set_pixmap(circle, &circle_pixmap);
```

### 设置Circle边框颜色
使用sgl_circle_set_border_color()函数设置Circle的边框颜色，如下：
```c
sgl_circle_set_border_color(circle, SGL_COLOR_BLACK);
```

### 设置Circle边框宽度
使用sgl_circle_set_border_width()函数设置Circle的边框宽度，如下：
```c
sgl_circle_set_border_width(circle, 2);
```
