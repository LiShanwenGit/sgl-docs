## dropdown控件
创建一个dropdown控件，使用如下代码：
```c
sgl_obj_t *dropdown = sgl_dropdown_create(NULL);
sgl_obj_set_pos(dropdown, 250, 100);
sgl_obj_set_size(dropdown, 150, 40);
```
上面代码在默认的活动页面上创建了一个大小为150x40的Dropdown控件，并设置其位置为250,100。

### 设置Dropdown颜色
使用sgl_dropdown_set_color()函数设置Dropdown的颜色，如下：
```c
sgl_obj_t *dropdown = sgl_dropdown_create(NULL);
sgl_obj_set_pos(dropdown, 250, 100);
sgl_obj_set_size(dropdown, 150, 40);
sgl_dropdown_set_color(dropdown, SGL_COLOR_WHITE);
```

### 设置Dropdown边框宽度
使用sgl_dropdown_set_border_width()函数设置Dropdown的边框宽度，如下：
```c
sgl_dropdown_set_border_width(dropdown, 2);
```

### 设置Dropdown边框颜色
使用sgl_dropdown_set_border_color()函数设置Dropdown的边框颜色，如下：
```c
sgl_dropdown_set_border_color(dropdown, SGL_COLOR_BLACK);
```

### 设置Dropdown选中颜色
使用sgl_dropdown_set_selected_color()函数设置Dropdown的选中颜色，如下：
```c
sgl_dropdown_set_selected_color(dropdown, SGL_COLOR_BLUE);
```

### 设置Dropdown圆角
使用sgl_dropdown_set_radius()函数设置Dropdown的圆角，如下：
```c
sgl_dropdown_set_radius(dropdown, 10);
```

### 设置Dropdown透明度
使用sgl_dropdown_set_alpha()函数设置Dropdown的透明度，如下：
```c
sgl_dropdown_set_alpha(dropdown, 128);
```

### 设置Dropdown文本颜色
使用sgl_dropdown_set_text_color()函数设置Dropdown的文本颜色，如下：
```c
sgl_dropdown_set_text_color(dropdown, SGL_COLOR_BLACK);
```

### 设置Dropdown字体
使用sgl_dropdown_set_text_font()函数设置Dropdown的字体，如下：
```c
sgl_dropdown_set_text_font(dropdown, &consolas24);
```

### 添加选项
使用sgl_dropdown_add_option()函数向Dropdown添加选项，如下：
```c
sgl_dropdown_add_option(dropdown, "选项1");
sgl_dropdown_add_option(dropdown, "选项2");
sgl_dropdown_add_option(dropdown, "选项3");
```

### 获取选中索引
使用sgl_dropdown_get_selected_index()函数获取Dropdown的选中索引，如下：
```c
int index = sgl_dropdown_get_selected_index(dropdown);
```

### 获取选中文本
使用sgl_dropdown_get_selected_text()函数获取Dropdown的选中文本，如下：
```c
const char *text = sgl_dropdown_get_selected_text(dropdown);
```

### 删除选项
使用sgl_dropdown_delete_option_by_text()或sgl_dropdown_delete_option_by_index()函数删除选项，如下：
```c
sgl_dropdown_delete_option_by_text(dropdown, "选项1");
sgl_dropdown_delete_option_by_index(dropdown, 0);
```
