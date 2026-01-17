## 图片取模数据生成
图片取模实际上是将图片数据转换为pixmap数据，但是针对不同的控件，其支持的pixmapdata格式不同，因此需要将图片数据转换为对应的pixmapdata数据。
### 普通控件的pixmap支持
普通控件(按钮，矩形，圆，进度条等)的pixmap仅支持相应颜色为的格式，不支持压缩，也不支持外部Flash，例如，屏幕的颜色是RGB565的，那么取模时选择的颜色格式必须为RGB565，否则会出错，如果屏幕是RGB888的，那么取模时选择的颜色格式必须为RGB888，否则会出错。
### ext_img控件的pixmap支持
ext_img控件即扩展图片控件的pixmap支持RGB332, RGB565，RGB888，并且支持RLE压缩格式，同时支持外部Flash。      
### 在线取模工具
下面是图片取模数据生成工具，请将图片拖入工具中，然后点击生成按钮，即可生成对应的pixmap数据。 
<iframe 
    src="../_static/image_conv_tool.html" 
    width="100%" 
    height="2000px" 
    frameborder="0">
</iframe>
