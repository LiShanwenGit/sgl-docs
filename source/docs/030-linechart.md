## linechart控件
创建一个linechart控件，使用如下代码：
```c
sgl_obj_t *chart = sgl_linechart_create(NULL);
sgl_obj_set_pos(chart, 250, 100);
sgl_obj_set_size(chart, 300, 200);
```
上面代码在默认的活动页面上创建了一个大小为300x200的LineChart控件，并设置其位置为250,100。

### 设置LineChart背景颜色
使用sgl_linechart_set_bg_color()函数设置LineChart的背景颜色，如下：
```c
sgl_obj_t *chart = sgl_linechart_create(NULL);
sgl_obj_set_pos(chart, 250, 100);
sgl_obj_set_size(chart, 300, 200);
sgl_linechart_set_bg_color(chart, SGL_COLOR_WHITE);
```

### 设置LineChart线条颜色
使用sgl_linechart_set_line_color()函数设置LineChart的线条颜色，如下：
```c
sgl_linechart_set_line_color(chart, SGL_COLOR_BLUE);
```

### 设置LineChart数据
使用sgl_linechart_set_data()函数设置LineChart的数据，如下：
```c
uint16_t data[] = {50, 80, 120, 60, 90, 110, 70};
sgl_linechart_set_data(chart, data, 7);
```

### 设置LineChart点大小
使用sgl_linechart_set_point_size()函数设置LineChart的点大小，如下：
```c
sgl_linechart_set_point_size(chart, 4);
```

### 设置LineChart线条宽度
使用sgl_linechart_set_line_width()函数设置LineChart的线条宽度，如下：
```c
sgl_linechart_set_line_width(chart, 2);
```

### 设置LineChart透明度
使用sgl_linechart_set_alpha()函数设置LineChart的透明度，如下：
```c
sgl_linechart_set_alpha(chart, 128);
```
