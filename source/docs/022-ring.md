## ring控件
创建一个ring控件，使用如下代码：
```c
sgl_obj_t *ring = sgl_ring_create(NULL);
sgl_obj_set_pos(ring, 250, 100);
sgl_obj_set_size(ring, 100, 100);
```
上面代码在默认的活动页面上创建了一个大小为100x100的Ring控件，并设置其位置为250,100。

### 设置Ring颜色
使用sgl_ring_set_color()函数设置Ring的颜色，如下：
```c
sgl_obj_t *ring = sgl_ring_create(NULL);
sgl_obj_set_pos(ring, 250, 100);
sgl_obj_set_size(ring, 100, 100);
sgl_ring_set_color(ring, SGL_COLOR_RED);
```

### 设置Ring透明度
使用sgl_ring_set_alpha()函数设置Ring的透明度，如下：
```c
sgl_ring_set_alpha(ring, 128);
```

### 设置Ring半径
使用sgl_ring_set_radius()函数设置Ring的内半径和外半径，如下：
```c
sgl_ring_set_radius(ring, 20, 40);
```
