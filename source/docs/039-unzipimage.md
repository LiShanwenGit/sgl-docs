## unzip_image控件
创建一个unzip_image控件，使用如下代码：
```c
sgl_obj_t *img = sgl_unzip_image_create(NULL);
sgl_obj_set_pos(img, 250, 100);
sgl_obj_set_size(img, 100, 100);
```
上面代码在默认的活动页面上创建了一个大小为100x100的UnzipImage控件，并设置其位置为250,100。

### 设置UnzipImage压缩包路径
使用sgl_unzip_image_set_zip_path()函数设置UnzipImage的压缩包路径，如下：
```c
sgl_obj_t *img = sgl_unzip_image_create(NULL);
sgl_obj_set_pos(img, 250, 100);
sgl_obj_set_size(img, 100, 100);
sgl_unzip_image_set_zip_path(img, "/sdcard/images.zip");
```

### 设置UnzipImage图片名称
使用sgl_unzip_image_set_image_name()函数设置UnzipImage的图片名称，如下：
```c
sgl_unzip_image_set_image_name(img, "icon.png");
```

### 设置UnzipImage透明度
使用sgl_unzip_image_set_alpha()函数设置UnzipImage的透明度，如下：
```c
sgl_unzip_image_set_alpha(img, 128);
```

### 设置UnzipImage对齐方式
使用sgl_unzip_image_set_align()函数设置UnzipImage的对齐方式，如下：
```c
sgl_unzip_image_set_align(img, SGL_ALIGN_CENTER);
```

### 设置UnzipImage缩放模式
使用sgl_unzip_image_set_scale()函数设置UnzipImage的缩放模式，如下：
```c
sgl_unzip_image_set_scale(img, SGL_SCALE_FIT);
```

UnzipImage支持以下缩放模式：
- SGL_SCALE_FIT：适应模式
- SGL_SCALE_FILL：填充模式
- SGL_SCALE_STRETCH：拉伸模式
