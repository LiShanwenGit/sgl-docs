## page概念
SGL中的page表示一个绘制页面，其大小为屏幕的宽和高，无法改变，所有的控件都绘制在page中，也就是page是所有的控件的根控件。在调用sgl_init()时就默认创建一个page，作为一个活动的page。
用户也可以自己创建一个page，用来做多页面切换显示。

### 页面创建（根控件创建）
使用sgl_obj_create(NULL)函数创建一个pag，函数原型如下：
```c
sgl_obj_t* sgl_obj_create(sgl_obj_t *parent);
```
例如下面创建两个页面，然后将第二个页面作为活动页面：
```c
sgl_obj_t *page1 = sgl_obj_create(NULL);
sgl_obj_t *page2 = sgl_obj_create(NULL);
sgl_screen_load(page2);
```
  
### 设置背景色
使用sgl_page_set_color()函数设置页面的背景色，函数原型如下：
```c
void sgl_page_set_color(sgl_obj_t* obj, sgl_color_t color);
```

### 设置页面背景图片
使用sgl_page_set_pixmap()函数设置页面的背景图片，函数原型如下：
```c
void sgl_page_set_pixmap(sgl_obj_t* obj, const sgl_pixmap_t *pixmap);
```
例如下面创建一个页面，并设置其背景图片为test_pixmap：
```c
extern const unsigned char gImage_test[7080];
const sgl_pixmap_t test_pixmap = {
    .width = 60,
    .height = 59,
    .bitmap = gImage_test,
};

sgl_obj_t *page = sgl_obj_create(NULL);
sgl_page_set_pixmap(page, &test_pixmap);
```
