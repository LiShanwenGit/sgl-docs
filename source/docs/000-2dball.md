## 2dball控件
创建一个2dball控件，使用如下代码：
```c
sgl_obj_t *ball = sgl_2dball_create(NULL);
sgl_obj_set_pos(ball, 250, 100);
sgl_obj_set_size(ball, 200, 200);
```
上面代码在默认的活动页面上创建了一个大小为200x200的2DBall控件，并设置其位置为250,100。

### 设置2DBall颜色
使用sgl_2dball_set_color()函数设置2DBall的颜色，如下：
```c
sgl_obj_t *ball = sgl_2dball_create(NULL);
sgl_obj_set_pos(ball, 250, 100);
sgl_obj_set_size(ball, 200, 200);
sgl_2dball_set_color(ball, SGL_COLOR_RED);
```

### 设置2DBall透明度
使用sgl_2dball_set_alpha()函数设置2DBall的透明度，如下：
```c
sgl_2dball_set_alpha(ball, 128);
```

### 设置2DBall半径
使用sgl_2dball_set_radius()函数设置2DBall的半径，如下：
```c
sgl_2dball_set_radius(ball, 50);
```

### 设置2DBall初始位置
使用sgl_2dball_set_init_pos()函数设置2DBall的初始位置，如下：
```c
sgl_2dball_set_init_pos(ball, 100, 100);
```
