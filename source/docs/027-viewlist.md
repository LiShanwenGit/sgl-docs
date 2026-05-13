## viewlist控件
创建一个viewlist控件，使用如下代码：
```c
sgl_obj_t *viewlist = sgl_viewlist_create(NULL);
sgl_obj_set_pos(viewlist, 250, 100);
sgl_obj_set_size(viewlist, 200, 300);
```
上面代码在默认的活动页面上创建了一个大小为200x300的Viewlist控件，并设置其位置为250,100。

### 设置Viewlist圆角
使用sgl_viewlist_set_radius()函数设置Viewlist的圆角，如下：
```c
sgl_obj_t *viewlist = sgl_viewlist_create(NULL);
sgl_obj_set_pos(viewlist, 250, 100);
sgl_obj_set_size(viewlist, 200, 300);
sgl_viewlist_set_radius(viewlist, 10);
```

### 设置Viewlist背景颜色
使用sgl_viewlist_set_bg_color()函数设置Viewlist的背景颜色，如下：
```c
sgl_viewlist_set_bg_color(viewlist, SGL_COLOR_WHITE);
```

### 设置Viewlist透明度
使用sgl_viewlist_set_alpha()函数设置Viewlist的透明度，如下：
```c
sgl_viewlist_set_alpha(viewlist, 128);
```

### 设置Viewlist边框宽度
使用sgl_viewlist_set_border_width()函数设置Viewlist的边框宽度，如下：
```c
sgl_viewlist_set_border_width(viewlist, 2);
```

### 设置Viewlist边框颜色
使用sgl_viewlist_set_border_color()函数设置Viewlist的边框颜色，如下：
```c
sgl_viewlist_set_border_color(viewlist, SGL_COLOR_BLACK);
```

### 设置Viewlist背景图片
使用sgl_viewlist_set_pixmap()函数设置Viewlist的背景图片，如下：
```c
extern const sgl_pixmap_t viewlist_pixmap;
sgl_viewlist_set_pixmap(viewlist, &viewlist_pixmap);
```

### 设置Viewlist项高度
使用sgl_viewlist_set_item_height()函数设置Viewlist的项高度，如下：
```c
sgl_viewlist_set_item_height(viewlist, 50);
```

### 添加子控件
使用sgl_viewlist_append_obj()函数向Viewlist添加子控件，如下：
```c
for (int i = 0; i < 10; i++) {
    sgl_obj_t *label = sgl_label_create(viewlist);
    sgl_label_set_font(label, &consolas24);
    sgl_label_set_text_fmt(label, "项目 %d", i);
    sgl_viewlist_set_item_height(viewlist, 50);
    sgl_viewlist_append_obj(viewlist, label);
}
```
