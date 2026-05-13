## textlist控件
创建一个textlist控件，使用如下代码：
```c
sgl_obj_t *textlist = sgl_textlist_create(NULL);
sgl_obj_set_pos(textlist, 250, 100);
sgl_obj_set_size(textlist, 200, 200);
```
上面代码在默认的活动页面上创建了一个大小为200x200的Textlist控件，并设置其位置为250,100。

### 设置Textlist圆角
使用sgl_textlist_set_radius()函数设置Textlist的圆角，如下：
```c
sgl_obj_t *textlist = sgl_textlist_create(NULL);
sgl_obj_set_pos(textlist, 250, 100);
sgl_obj_set_size(textlist, 200, 200);
sgl_textlist_set_radius(textlist, 10);
```

### 设置Textlist文本颜色
使用sgl_textlist_set_text_color()函数设置Textlist的文本颜色，如下：
```c
sgl_textlist_set_text_color(textlist, SGL_COLOR_BLACK);
```

### 设置Textlist选中颜色
使用sgl_textlist_set_selected_color()函数设置Textlist的选中颜色，如下：
```c
sgl_textlist_set_selected_color(textlist, SGL_COLOR_BLUE);
```

### 设置Textlist边框颜色
使用sgl_textlist_set_border_color()函数设置Textlist的边框颜色，如下：
```c
sgl_textlist_set_border_color(textlist, SGL_COLOR_BLACK);
```

### 设置Textlist背景颜色
使用sgl_textlist_set_bg_color()函数设置Textlist的背景颜色，如下：
```c
sgl_textlist_set_bg_color(textlist, SGL_COLOR_WHITE);
```

### 设置Textlist字体
使用sgl_textlist_set_text_font()函数设置Textlist的字体，如下：
```c
sgl_textlist_set_text_font(textlist, &consolas24);
```

### 设置Textlist背景图片
使用sgl_textlist_set_pixmap()函数设置Textlist的背景图片，如下：
```c
extern const sgl_pixmap_t textlist_pixmap;
sgl_textlist_set_pixmap(textlist, &textlist_pixmap);
```

### 设置Textlist透明度
使用sgl_textlist_set_alpha()函数设置Textlist的透明度，如下：
```c
sgl_textlist_set_alpha(textlist, 128);
```

### 设置Textlist边框宽度
使用sgl_textlist_set_border_width()函数设置Textlist的边框宽度，如下：
```c
sgl_textlist_set_border_width(textlist, 2);
```

### 添加列表项
使用sgl_textlist_add_item()函数向Textlist添加列表项，如下：
```c
sgl_textlist_add_item(textlist, "项目1");
sgl_textlist_add_item(textlist, "项目2");
sgl_textlist_add_item(textlist, "项目3");
```

### 获取选中文本
使用sgl_textlist_get_selected_text()函数获取Textlist的选中文本，如下：
```c
char *text = sgl_textlist_get_selected_text(textlist);
```

### 获取选中索引
使用sgl_textlist_get_selected_index()函数获取Textlist的选中索引，如下：
```c
int16_t index = sgl_textlist_get_selected_index(textlist);
```

### 删除列表项
使用sgl_textlist_delete_item_by_index()或sgl_textlist_delete_item_by_text()函数删除列表项，如下：
```c
sgl_textlist_delete_item_by_index(textlist, 0);
sgl_textlist_delete_item_by_text(textlist, "项目1");
```
