## textline控件
创建一个textline控件，使用如下代码：
```c
sgl_obj_t *textline = sgl_textline_create(NULL);
sgl_obj_set_pos(textline, 250, 100);
sgl_obj_set_size(textline, 200, 40);
```
上面代码在默认的活动页面上创建了一个大小为200x40的Textline控件，并设置其位置为250,100。

### 设置Textline文本
使用sgl_textline_set_text()函数设置Textline的文本，如下：
```c
sgl_obj_t *textline = sgl_textline_create(NULL);
sgl_obj_set_pos(textline, 250, 100);
sgl_obj_set_size(textline, 200, 40);
sgl_textline_set_text(textline, "这是一行文本");
```

### 设置Textline字体
使用sgl_textline_set_text_font()函数设置Textline的字体，如下：
```c
sgl_textline_set_text_font(textline, &consolas24);
```

### 设置Textline文本颜色
使用sgl_textline_set_text_color()函数设置Textline的文本颜色，如下：
```c
sgl_textline_set_text_color(textline, SGL_COLOR_BLACK);
```

### 设置Textline背景颜色
使用sgl_textline_set_bg_color()函数设置Textline的背景颜色，如下：
```c
sgl_textline_set_bg_color(textline, SGL_COLOR_WHITE);
```

### 设置Textline背景透明
使用sgl_textline_set_bg_transparent()函数设置Textline的背景透明，如下：
```c
sgl_textline_set_bg_transparent(textline);
```

### 设置Textline圆角
使用sgl_textline_set_radius()函数设置Textline的圆角，如下：
```c
sgl_textline_set_radius(textline, 10);
```

### 设置Textline透明度
使用sgl_textline_set_alpha()函数设置Textline的透明度，如下：
```c
sgl_textline_set_alpha(textline, 128);
```

### 设置Textline边缘边距
使用sgl_textline_set_edge_margin()函数设置Textline的边缘边距，如下：
```c
sgl_textline_set_edge_margin(textline, 10);
```

### 设置Textline行间距
使用sgl_textline_set_line_margin()函数设置Textline的行间距，如下：
```c
sgl_textline_set_line_margin(textline, 5);
```
