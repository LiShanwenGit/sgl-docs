## progress控件
创建一个progress控件，使用如下代码：
```c
sgl_obj_t *progress = sgl_progress_create(NULL);
sgl_obj_set_pos(progress, 250, 100);
sgl_obj_set_size(progress, 200, 20);
```
上面代码在默认的活动页面上创建了一个大小为200x20的Progress控件，并设置其位置为250,100。

### 设置Progress轨道颜色
使用sgl_progress_set_track_color()函数设置Progress的轨道颜色，如下：
```c
sgl_obj_t *progress = sgl_progress_create(NULL);
sgl_obj_set_pos(progress, 250, 100);
sgl_obj_set_size(progress, 200, 20);
sgl_progress_set_track_color(progress, SGL_COLOR_GRAY);
```

### 设置Progress轨道透明度
使用sgl_progress_set_track_alpha()函数设置Progress的轨道透明度，如下：
```c
sgl_progress_set_track_alpha(progress, 128);
```

### 设置Progress填充颜色
使用sgl_progress_set_fill_color()函数设置Progress的填充颜色，如下：
```c
sgl_progress_set_fill_color(progress, SGL_COLOR_RED);
```

### 设置Progress填充透明度
使用sgl_progress_set_fill_alpha()函数设置Progress的填充透明度，如下：
```c
sgl_progress_set_fill_alpha(progress, 128);
```

### 设置Progress圆角
使用sgl_progress_set_radius()函数设置Progress的圆角，如下：
```c
sgl_progress_set_radius(progress, 10);
```

### 设置Progress边框宽度
使用sgl_progress_set_border_width()函数设置Progress的边框宽度，如下：
```c
sgl_progress_set_border_width(progress, 2);
```

### 设置Progress边框颜色
使用sgl_progress_set_border_color()函数设置Progress的边框颜色，如下：
```c
sgl_progress_set_border_color(progress, SGL_COLOR_BLACK);
```

### 设置Progress背景图片
使用sgl_progress_set_pixmap()函数设置Progress的背景图片，如下：
```c
extern const sgl_pixmap_t progress_pixmap;
sgl_progress_set_pixmap(progress, &progress_pixmap);
```

### 设置Progress填充间隙
使用sgl_progress_set_fill_gap()函数设置Progress的填充间隙，如下：
```c
sgl_progress_set_fill_gap(progress, 5);
```

### 设置Progress填充圆角
使用sgl_progress_set_fill_radius()函数设置Progress的填充圆角，如下：
```c
sgl_progress_set_fill_radius(progress, 5);
```

### 设置Progress填充宽度
使用sgl_progress_set_fill_width()函数设置Progress的填充宽度，如下：
```c
sgl_progress_set_fill_width(progress, 8);
```

### 设置Progress值
使用sgl_progress_set_value()函数设置Progress的值，如下：
```c
sgl_progress_set_value(progress, 50);
```

### 获取Progress值
使用sgl_progress_get_value()函数获取Progress的当前值，如下：
```c
uint8_t value = sgl_progress_get_value(progress);
```
