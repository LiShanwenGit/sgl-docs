## piechart控件
创建一个piechart控件，使用如下代码：
```c
sgl_obj_t *chart = sgl_piechart_create(NULL);
sgl_obj_set_pos(chart, 250, 100);
sgl_obj_set_size(chart, 200, 200);
```
上面代码在默认的活动页面上创建了一个大小为200x200的PieChart控件，并设置其位置为250,100。

### 设置PieChart数据
使用sgl_piechart_set_data()函数设置PieChart的数据，如下：
```c
sgl_obj_t *chart = sgl_piechart_create(NULL);
sgl_obj_set_pos(chart, 250, 100);
sgl_obj_set_size(chart, 200, 200);
uint16_t data[] = {30, 20, 50};
sgl_piechart_set_data(chart, data, 3);
```

### 设置PieChart颜色数组
使用sgl_piechart_set_color_array()函数设置PieChart的颜色数组，如下：
```c
uint16_t colors[] = {SGL_COLOR_RED, SGL_COLOR_GREEN, SGL_COLOR_BLUE};
sgl_piechart_set_color_array(chart, colors, 3);
```

### 设置PieChart透明度
使用sgl_piechart_set_alpha()函数设置PieChart的透明度，如下：
```c
sgl_piechart_set_alpha(chart, 128);
```
