## ext_img控件
创建一个ext_img控件，使用如下代码：
```c
sgl_obj_t *img = sgl_ext_img_create(NULL);
sgl_obj_set_pos(img, 250, 100);
sgl_obj_set_size(img, 100, 100);
```
上面代码在默认的活动页面上创建了一个大小为100x100的ExtImg控件，并设置其位置为250,100。

### 设置ExtImg图片路径
使用sgl_ext_img_set_path()函数设置ExtImg的图片路径，如下：
```c
sgl_obj_t *img = sgl_ext_img_create(NULL);
sgl_obj_set_pos(img, 250, 100);
sgl_obj_set_size(img, 100, 100);
sgl_ext_img_set_path(img, "/sdcard/image.png");
```

### 设置ExtImg透明度
使用sgl_ext_img_set_alpha()函数设置ExtImg的透明度，如下：
```c
sgl_ext_img_set_alpha(img, 128);
```

### 设置ExtImg对齐方式
使用sgl_ext_img_set_align()函数设置ExtImg的对齐方式，如下：
```c
sgl_ext_img_set_align(img, SGL_ALIGN_CENTER);
```

### 设置ExtImg缩放模式
使用sgl_ext_img_set_scale()函数设置ExtImg的缩放模式，如下：
```c
sgl_ext_img_set_scale(img, SGL_SCALE_FIT);
```

ExtImg支持以下缩放模式：
- SGL_SCALE_FIT：适应模式
- SGL_SCALE_FILL：填充模式
- SGL_SCALE_STRETCH：拉伸模式
