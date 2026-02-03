## msgbox控件
### 创建基本的msgbox控件
这个控件用于显示消息框，使用如下代码：
```c
sgl_obj_t *msgbox = sgl_msgbox_create(NULL);
sgl_obj_set_size(msgbox, 200, 150);
sgl_obj_set_pos_align(msgbox, SGL_ALIGN_CENTER);
sgl_msgbox_set_font(msgbox, &consolas24_compress);
```
上面的代码中sgl_obj_set_pos_align函数设置了消息框的位置，SGL_ALIGN_CENTER表示居中，sgl_msgbox_set_font函数设置消息框的字体，consolas24_compress表示Consolas字体，24号，压缩字体。效果如下：          
![alt text](imgs/msgbox/img-1.jpg)             

### 设置消息框的标题和内容
使用sgl_msgbox_set_title_text函数设置消息框的标题，使用sgl_msgbox_set_msg_text函数设置消息框的内容，如下： 
```c
sgl_obj_t *msgbox = sgl_msgbox_create(NULL);
sgl_obj_set_size(msgbox, 200, 150);
sgl_obj_set_pos_align(msgbox, SGL_ALIGN_CENTER);
sgl_msgbox_set_font(msgbox, &consolas24_compress);
sgl_msgbox_set_title_text(msgbox, "SGL");
sgl_msgbox_set_msg_text(msgbox, "SGL is cool");
```
效果如下:       
![alt text](imgs/msgbox/img-2.jpg)       

### 设置消息框的圆角半径
使用sgl_msgbox_set_radius函数设置消息框的圆角半径，如下：
```c
sgl_obj_t *msgbox = sgl_msgbox_create(NULL);
sgl_obj_set_size(msgbox, 200, 150);
sgl_obj_set_pos_align(msgbox, SGL_ALIGN_CENTER);
sgl_msgbox_set_font(msgbox, &consolas24_compress);
sgl_msgbox_set_title_text(msgbox, "SGL");
sgl_msgbox_set_msg_text(msgbox, "SGL is cool");
sgl_msgbox_set_radius(msgbox, 10);
```
上面使用sgl_msgbox_set_radius函数设置消息框的圆角半径为10，效果如下：     
![alt text](imgs/msgbox/img-3.jpg)           

### 设置消息框的颜色
使用sgl_msgbox_set_color函数设置消息框的颜色，使用sgl_msgbox_set_left_btn_color函数设置消息框的按钮颜色，使用sgl_msgbox_set_right_btn_color函数设置消息框的关闭按钮颜色，如下：
```c
sgl_obj_t *msgbox = sgl_msgbox_create(NULL);
sgl_obj_set_size(msgbox, 200, 150);
sgl_obj_set_pos_align(msgbox, SGL_ALIGN_CENTER);
sgl_msgbox_set_font(msgbox, &consolas24_compress);
sgl_msgbox_set_title_text(msgbox, "SGL");
sgl_msgbox_set_msg_text(msgbox, "SGL is cool");
sgl_msgbox_set_radius(msgbox, 10);
sgl_msgbox_set_color(msgbox, SGL_COLOR_RED_ORANGE);
sgl_msgbox_set_left_btn_color(msgbox, SGL_COLOR_GOLD);
sgl_msgbox_set_right_btn_color(msgbox, SGL_COLOR_BLUE);
```
效果如下：     
![alt text](imgs/msgbox/img-4.jpg)         

### 设置消息框的按钮文本
使用sgl_msgbox_set_left_btn_text函数设置消息框的按钮文本，使用sgl_msgbox_set_right_btn_text函数设置消息框的关闭按钮文本，如下：
```c
sgl_obj_t *msgbox = sgl_msgbox_create(NULL);
sgl_obj_set_size(msgbox, 200, 150);
sgl_obj_set_pos_align(msgbox, SGL_ALIGN_CENTER);
sgl_msgbox_set_font(msgbox, &consolas24_compress);
sgl_msgbox_set_title_text(msgbox, "SGL");
sgl_msgbox_set_msg_text(msgbox, "SGL is cool");
sgl_msgbox_set_radius(msgbox, 10);
sgl_msgbox_set_color(msgbox, SGL_COLOR_RED_ORANGE);
sgl_msgbox_set_left_btn_color(msgbox, SGL_COLOR_GOLD);
sgl_msgbox_set_right_btn_color(msgbox, SGL_COLOR_BLUE);
sgl_msgbox_set_left_btn_text(msgbox, "Know");
sgl_msgbox_set_right_btn_text(msgbox, "What?");
```
效果如下：      
![alt text](imgs/msgbox/img-5.jpg)           

#### 获取消息框退出状态
获取消息退出状态有两种方式，如下：
1. 通过设置回调函数，使用sgl_msgbox_get_current_btn函数获取当前状态
```c
void msgbox_event_cb(sgl_event_t *event)
{
    sgl_obj_t *msgbox = event->obj; 
    if (strcmp(sgl_msgbox_get_current_btn(msgbox), "YES") == 0) {
        SGL_LOG_INFO("msgbox_event_cb: OK\n");
    }
    else if (strcmp(sgl_msgbox_get_current_btn(msgbox), "NO") == 0) {
        SGL_LOG_INFO("msgbox_event_cb: NO\n");
    }
}
```
2. 设置退出返回状态，使用sgl_msgbox_set_exit_answer函数设置退出返回状态，返回状态指向退出时的按钮文本，如下：
```c
sgl_obj_t *msgbox = sgl_msgbox_create(NULL);
sgl_obj_set_size(msgbox, 300, 150);
sgl_obj_set_pos_align(msgbox, SGL_ALIGN_CENTER);
sgl_msgbox_set_font(msgbox, &consolas24_compress);
sgl_msgbox_set_exit_answer(msgbox, &exit);
sgl_msgbox_set_msg_x_offset(msgbox, 50);
```

#### 按键切换状态
使用sgl_event_send_obj(msgbox, SGL_EVENT_OPTION_WALK)方式可切换当前选中的按钮，然后使用sgl_event_send_obj(msgbox, SGL_EVENT_OPTION_TAP)方式模拟点击按钮       

```c
sgl_event_send_obj(msgbox, SGL_EVENT_OPTION_WALK)
```
这个函数每发送一次，就会切换当前选中的按钮
```c
sgl_event_send_obj(msgbox, SGL_EVENT_OPTION_TAP)
```
这个函数每发送一次，就会模拟点击按钮，msgbox就会退出
