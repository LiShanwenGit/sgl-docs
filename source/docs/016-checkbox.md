## checkbox控件
创建一个checkbox控件，使用如下代码：
```c
sgl_obj_t *checkbox = sgl_checkbox_create(NULL);
sgl_obj_set_pos(checkbox, 250, 100);
sgl_obj_set_size(checkbox, 40, 40);
```
上面代码在默认的活动页面上创建了一个大小为40x40的Checkbox控件，并设置其位置为250,100。

### 设置Checkbox颜色
使用sgl_checkbox_set_color()函数设置Checkbox的颜色，如下：
```c
sgl_obj_t *checkbox = sgl_checkbox_create(NULL);
sgl_obj_set_pos(checkbox, 250, 100);
sgl_obj_set_size(checkbox, 40, 40);
sgl_checkbox_set_color(checkbox, SGL_COLOR_RED);
```

### 设置Checkbox透明度
使用sgl_checkbox_set_alpha()函数设置Checkbox的透明度，如下：
```c
sgl_checkbox_set_alpha(checkbox, 128);
```

### 设置Checkbox文本
使用sgl_checkbox_set_text()函数设置Checkbox的文本，如下：
```c
sgl_checkbox_set_text(checkbox, "选项");
```

### 设置Checkbox字体
使用sgl_checkbox_set_font()函数设置Checkbox的字体，如下：
```c
sgl_checkbox_set_font(checkbox, &consolas24);
```

### 设置Checkbox状态
使用sgl_checkbox_set_status()函数设置Checkbox的选中状态，如下：
```c
sgl_checkbox_set_status(checkbox, true);
```

### 获取Checkbox状态
使用sgl_checkbox_get_status()函数获取Checkbox的当前状态，如下：
```c
bool status = sgl_checkbox_get_status(checkbox);
```
