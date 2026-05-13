## qrcode控件
创建一个qrcode控件，使用如下代码：
```c
sgl_obj_t *qrcode = sgl_qrcode_create(NULL);
sgl_obj_set_pos(qrcode, 250, 100);
sgl_obj_set_size(qrcode, 150, 150);
```
上面代码在默认的活动页面上创建了一个大小为150x150的QRCode控件，并设置其位置为250,100。

### 设置QRCode数据
使用sgl_qrcode_set_data()函数设置QRCode的数据，如下：
```c
sgl_obj_t *qrcode = sgl_qrcode_create(NULL);
sgl_obj_set_pos(qrcode, 250, 100);
sgl_obj_set_size(qrcode, 150, 150);
sgl_qrcode_set_data(qrcode, "https://github.com/sgl-org/sgl");
```

### 设置QRCode前景颜色
使用sgl_qrcode_set_fg_color()函数设置QRCode的前景颜色，如下：
```c
sgl_qrcode_set_fg_color(qrcode, SGL_COLOR_BLACK);
```

### 设置QRCode背景颜色
使用sgl_qrcode_set_bg_color()函数设置QRCode的背景颜色，如下：
```c
sgl_qrcode_set_bg_color(qrcode, SGL_COLOR_WHITE);
```

### 设置QRCode透明度
使用sgl_qrcode_set_alpha()函数设置QRCode的透明度，如下：
```c
sgl_qrcode_set_alpha(qrcode, 128);
```
