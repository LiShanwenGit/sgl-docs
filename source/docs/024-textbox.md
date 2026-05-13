## textbox控件
创建一个textbox控件，使用如下代码：
```c
sgl_obj_t *textbox = sgl_textbox_create(NULL);
sgl_obj_set_pos(textbox, 250, 100);
sgl_obj_set_size(textbox, 200, 150);
```
上面代码在默认的活动页面上创建了一个大小为200x150的Textbox控件，并设置其位置为250,100。

### 设置Textbox文本
使用sgl_textbox_set_text()函数设置Textbox的文本，如下：
```c
sgl_obj_t *textbox = sgl_textbox_create(NULL);
sgl_obj_set_pos(textbox, 250, 100);
sgl_obj_set_size(textbox, 200, 150);
sgl_textbox_set_text(textbox, "这是一段文本内容\n支持多行显示");
```

### 设置Textbox文本颜色
使用sgl_textbox_set_text_color()函数设置Textbox的文本颜色，如下：
```c
sgl_textbox_set_text_color(textbox, SGL_COLOR_BLACK);
```

### 设置Textbox字体
使用sgl_textbox_set_text_font()函数设置Textbox的字体，如下：
```c
sgl_textbox_set_text_font(textbox, &consolas24);
```

### 设置Textbox背景颜色
使用sgl_textbox_set_bg_color()函数设置Textbox的背景颜色，如下：
```c
sgl_textbox_set_bg_color(textbox, SGL_COLOR_WHITE);
```

### 设置Textbox圆角
使用sgl_textbox_set_radius()函数设置Textbox的圆角，如下：
```c
sgl_textbox_set_radius(textbox, 10);
```

### 设置Textbox边框颜色
使用sgl_textbox_set_border_color()函数设置Textbox的边框颜色，如下：
```c
sgl_textbox_set_border_color(textbox, SGL_COLOR_BLACK);
```

### 设置Textbox边框宽度
使用sgl_textbox_set_border_width()函数设置Textbox的边框宽度，如下：
```c
sgl_textbox_set_border_width(textbox, 2);
```

### 设置Textbox背景图片
使用sgl_textbox_set_pixmap()函数设置Textbox的背景图片，如下：
```c
extern const sgl_pixmap_t textbox_pixmap;
sgl_textbox_set_pixmap(textbox, &textbox_pixmap);
```

### 设置Textbox行间距
使用sgl_textbox_set_line_margin()函数设置Textbox的行间距，如下：
```c
sgl_textbox_set_line_margin(textbox, 5);
```
