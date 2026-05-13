## barchart控件
创建一个barchart控件，使用如下代码：
```c
sgl_obj_t *chart = sgl_barchart_create(NULL);
sgl_obj_set_pos(chart, 250, 100);
sgl_obj_set_size(chart, 300, 200);
```
上面代码在默认的活动页面上创建了一个大小为300x200的BarChart控件，并设置其位置为250,100。

### 设置BarChart背景颜色
使用sgl_barchart_set_bg_color()函数设置BarChart的背景颜色，如下：
```c
sgl_obj_t *chart = sgl_barchart_create(NULL);
sgl_obj_set_pos(chart, 250, 100);
sgl_obj_set_size(chart, 300, 200);
sgl_barchart_set_bg_color(chart, SGL_COLOR_WHITE);
```

### 设置BarChart边框颜色
使用sgl_barchart_set_border_color()函数设置BarChart的边框颜色，如下：
```c
sgl_barchart_set_border_color(chart, SGL_COLOR_BLACK);
```

### 设置BarChart边框宽度
使用sgl_barchart_set_border_width()函数设置BarChart的边框宽度，如下：
```c
sgl_barchart_set_border_width(chart, 2);
```

### 设置BarChart数据
使用sgl_barchart_set_data()函数设置BarChart的数据，如下：
```c
uint16_t data[] = {50, 80, 120, 60, 90, 110, 70};
sgl_barchart_set_data(chart, data, 7);
```

### 设置BarChart颜色数组
使用sgl_barchart_set_color_array()函数设置BarChart的颜色数组，如下：
```c
uint16_t colors[] = {SGL_COLOR_RED, SGL_COLOR_GREEN, SGL_COLOR_BLUE, 
                     SGL_COLOR_YELLOW, SGL_COLOR_ORANGE, SGL_COLOR_PURPLE, SGL_COLOR_CYAN};
sgl_barchart_set_color_array(chart, colors, 7);
```

### 设置BarChart透明度
使用sgl_barchart_set_alpha()函数设置BarChart的透明度，如下：
```c
sgl_barchart_set_alpha(chart, 128);
```
