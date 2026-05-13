## polygon控件
创建一个polygon控件，使用如下代码：
```c
sgl_obj_t *polygon = sgl_polygon_create(NULL);
sgl_obj_set_pos(polygon, 250, 100);
sgl_obj_set_size(polygon, 100, 100);
```
上面代码在默认的活动页面上创建了一个大小为100x100的Polygon控件，并设置其位置为250,100。

### 设置Polygon顶点
使用sgl_polygon_set_points()函数设置Polygon的顶点，如下：
```c
sgl_obj_t *polygon = sgl_polygon_create(NULL);
sgl_obj_set_pos(polygon, 250, 100);
sgl_obj_set_size(polygon, 100, 100);
sgl_point_t points[] = {{50, 10}, {90, 90}, {10, 90}};
sgl_polygon_set_points(polygon, points, 3);
```

### 设置Polygon颜色
使用sgl_polygon_set_color()函数设置Polygon的颜色，如下：
```c
sgl_polygon_set_color(polygon, SGL_COLOR_RED);
```

### 设置Polygon透明度
使用sgl_polygon_set_alpha()函数设置Polygon的透明度，如下：
```c
sgl_polygon_set_alpha(polygon, 128);
```

### 设置Polygon边框颜色
使用sgl_polygon_set_border_color()函数设置Polygon的边框颜色，如下：
```c
sgl_polygon_set_border_color(polygon, SGL_COLOR_BLACK);
```

### 设置Polygon边框宽度
使用sgl_polygon_set_border_width()函数设置Polygon的边框宽度，如下：
```c
sgl_polygon_set_border_width(polygon, 2);
```
