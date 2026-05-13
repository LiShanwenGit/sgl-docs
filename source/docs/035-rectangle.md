## rectangle控件
创建一个rectangle控件，使用如下代码：
```c
sgl_obj_t *rect = sgl_rectangle_create(NULL);
sgl_obj_set_pos(rect, 250, 100);
sgl_obj_set_size(rect, 100, 50);
```
上面代码在默认的活动页面上创建了一个大小为100x50的Rectangle控件，并设置其位置为250,100。

### 设置Rectangle颜色
使用sgl_rectangle_set_color()函数设置Rectangle的颜色，如下：
```c
sgl_obj_t *rect = sgl_rectangle_create(NULL);
sgl_obj_set_pos(rect, 250, 100);
sgl_obj_set_size(rect, 100, 50);
sgl_rectangle_set_color(rect, SGL_COLOR_RED);
```

### 设置Rectangle圆角
使用sgl_rectangle_set_radius()函数设置Rectangle的圆角，如下：
```c
sgl_rectangle_set_radius(rect, 10);
```

### 设置Rectangle透明度
使用sgl_rectangle_set_alpha()函数设置Rectangle的透明度，如下：
```c
sgl_rectangle_set_alpha(rect, 128);
```

### 设置Rectangle边框颜色
使用sgl_rectangle_set_border_color()函数设置Rectangle的边框颜色，如下：
```c
sgl_rectangle_set_border_color(rect, SGL_COLOR_BLACK);
```

### 设置Rectangle边框宽度
使用sgl_rectangle_set_border_width()函数设置Rectangle的边框宽度，如下：
```c
sgl_rectangle_set_border_width(rect, 2);
```

### 设置Rectangle背景图片
使用sgl_rectangle_set_pixmap()函数设置Rectangle的背景图片，如下：
```c
extern const sgl_pixmap_t rect_pixmap;
sgl_rectangle_set_pixmap(rect, &rect_pixmap);
```
