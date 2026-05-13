## icon控件
创建一个icon控件，使用如下代码：
```c
sgl_obj_t *icon = sgl_icon_create(NULL);
sgl_obj_set_pos(icon, 250, 100);
sgl_obj_set_size(icon, 40, 40);
```
上面代码在默认的活动页面上创建了一个大小为40x40的Icon控件，并设置其位置为250,100。

### 设置Icon颜色
使用sgl_icon_set_color()函数设置Icon的颜色，如下：
```c
sgl_obj_t *icon = sgl_icon_create(NULL);
sgl_obj_set_pos(icon, 250, 100);
sgl_obj_set_size(icon, 40, 40);
sgl_icon_set_color(icon, SGL_COLOR_RED);
```

### 设置Icon透明度
使用sgl_icon_set_alpha()函数设置Icon的透明度，如下：
```c
sgl_icon_set_alpha(icon, 128);
```

### 设置Icon图标
使用sgl_icon_set_icon()函数设置Icon的图标，如下：
```c
extern const sgl_icon_pixmap_t icon_pixmap;
sgl_icon_set_icon(icon, &icon_pixmap);
```

### 设置Icon对齐方式
使用sgl_icon_set_align()函数设置Icon的对齐方式，如下：
```c
sgl_icon_set_align(icon, SGL_ALIGN_CENTER);
```

Icon支持以下对齐方式：
- SGL_ALIGN_LEFT：左对齐
- SGL_ALIGN_CENTER：居中对齐
- SGL_ALIGN_RIGHT：右对齐
