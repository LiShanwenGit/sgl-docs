## scope控件
创建一个scope控件，使用如下代码：
```c
sgl_obj_t *scope = sgl_scope_create(NULL);
sgl_obj_set_pos(scope, 250, 100);
sgl_obj_set_size(scope, 300, 200);
```
上面代码在默认的活动页面上创建了一个大小为300x200的Scope控件，并设置其位置为250,100。

### 设置Scope背景颜色
使用sgl_scope_set_bg_color()函数设置Scope的背景颜色，如下：
```c
sgl_obj_t *scope = sgl_scope_create(NULL);
sgl_obj_set_pos(scope, 250, 100);
sgl_obj_set_size(scope, 300, 200);
sgl_scope_set_bg_color(scope, SGL_COLOR_BLACK);
```

### 设置Scope线条颜色
使用sgl_scope_set_line_color()函数设置Scope的线条颜色，如下：
```c
sgl_scope_set_line_color(scope, SGL_COLOR_GREEN);
```

### 设置Scope网格颜色
使用sgl_scope_set_grid_color()函数设置Scope的网格颜色，如下：
```c
sgl_scope_set_grid_color(scope, SGL_COLOR_DARK_GRAY);
```

### 设置Scope透明度
使用sgl_scope_set_alpha()函数设置Scope的透明度，如下：
```c
sgl_scope_set_alpha(scope, 128);
```

### 设置Scope采样数据
使用sgl_scope_set_sample()函数设置Scope的采样数据，如下：
```c
uint16_t sample[] = {100, 150, 200, 150, 100, 50, 0, 50};
sgl_scope_set_sample(scope, sample, 8);
```

### 设置Scope网格间距
使用sgl_scope_set_grid_space()函数设置Scope的网格间距，如下：
```c
sgl_scope_set_grid_space(scope, 20, 20);
```
