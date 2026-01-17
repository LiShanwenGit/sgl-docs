## 字体生成
<!DOCTYPE html>
<html lang="zh-CN">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>图片取模工具</title>
    <style>
        * {
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }

        body {
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            min-height: 100vh;
            padding: 20px;
        }

        .container {
            max-width: 1200px;
            margin: 0 auto;
            background: white;
            border-radius: 20px;
            box-shadow: 0 20px 60px rgba(0, 0, 0, 0.3);
            overflow: hidden;
        }

        .header {
            background: linear-gradient(135deg, #4facfe 0%, #00f2fe 100%);
            padding: 30px;
            text-align: center;
            color: white;
        }

        .header h1 {
            font-size: 2.5em;
            font-weight: 700;
            text-shadow: 2px 2px 4px rgba(0, 0, 0, 0.2);
        }

        /* 标签页样式 */
        .tabs {
            display: flex;
            background: #f8f9fa;
            border-bottom: 2px solid #e0e0e0;
        }

        .tab-button {
            padding: 15px 30px;
            border: none;
            background: transparent;
            font-size: 1.1em;
            font-weight: 500;
            cursor: pointer;
            transition: all 0.3s ease;
            color: #666;
            border-bottom: 3px solid transparent;
        }

        .tab-button:hover {
            background: rgba(79, 172, 254, 0.1);
            color: #4facfe;
        }

        .tab-button.active {
            background: white;
            color: #4facfe;
            border-bottom-color: #4facfe;
            box-shadow: 0 2px 5px rgba(0, 0, 0, 0.1);
        }

        .tab-content {
            display: none;
            animation: fadeIn 0.3s ease;
        }

        .tab-content.active {
            display: block;
        }

        @keyframes fadeIn {
            from { opacity: 0; transform: translateY(10px); }
            to { opacity: 1; transform: translateY(0); }
        }

        .main-content {
            display: flex;
            gap: 30px;
            padding: 30px;
            flex-wrap: wrap;
        }

        .left-panel {
            flex: 1;
            min-width: 350px;
            display: flex;
            flex-direction: column;
            gap: 25px;
        }

        .right-panel {
            flex: 1;
            min-width: 350px;
            display: flex;
            flex-direction: column;
            gap: 25px;
        }

        .section {
            background: #f8f9fa;
            border-radius: 15px;
            padding: 25px;
            box-shadow: 0 5px 15px rgba(0, 0, 0, 0.1);
            transition: transform 0.5s cubic-bezier(0.25, 0.46, 0.45, 0.94), box-shadow 0.5s cubic-bezier(0.25, 0.46, 0.45, 0.94);
        }

        .section:hover {
            transform: translateY(-2px);
            box-shadow: 0 8px 20px rgba(0, 0, 0, 0.15);
        }

        .section h2 {
            color: #333;
            margin-bottom: 20px;
            font-size: 1.3em;
            font-weight: 600;
        }

        .file-input-container {
            position: relative;
            display: flex;
            justify-content: center;
            align-items: center;
            min-height: 50px;
            border: 2px dashed #ccc;
            border-radius: 8px;
            background: #fff;
            transition: all 0.3s ease;
        }

        .file-input-container:hover {
            border-color: #4facfe;
            background: #f0f8ff;
        }

        .file-input {
            position: absolute;
            width: 100%;
            height: 100%;
            opacity: 0;
            cursor: pointer;
        }

        .file-input-label {
            text-align: center;
            padding: 5px;
            color: #666;
            cursor: pointer;
            font-size: 0.9em;
        }

        .file-input-label i {
            font-size: 1.2em;
            display: inline-block;
            margin-right: 8px;
            color: #999;
            vertical-align: middle;
        }

        .file-input-label div {
            display: inline-block;
            vertical-align: middle;
        }

        .preview-container {
            display: flex;
            justify-content: center;
            align-items: center;
            min-height: 200px;
            background: #000;
            border-radius: 12px;
            overflow: hidden;
            box-shadow: inset 0 2px 10px rgba(0, 0, 0, 0.5);
        }

        #previewImage {
            max-width: 100%;
            max-height: 100%;
            object-fit: contain;
        }

        .size-controls {
            display: flex;
            gap: 15px;
            align-items: center;
            flex-wrap: wrap;
        }

        .size-input-group {
            flex: 1;
            min-width: 120px;
        }

        .size-input-group label {
            display: block;
            margin-bottom: 5px;
            color: #666;
            font-size: 0.9em;
        }

        .size-input-group input {
            width: 100%;
            padding: 12px;
            border: 2px solid #ddd;
            border-radius: 8px;
            font-size: 1em;
            transition: border-color 0.3s ease;
        }

        .size-input-group input:focus {
            outline: none;
            border-color: #4facfe;
            box-shadow: 0 0 0 3px rgba(79, 172, 254, 0.1);
        }

        .aspect-lock {
            display: flex;
            align-items: center;
            gap: 8px;
            margin-left: auto;
        }

        .aspect-lock input[type="checkbox"] {
            width: 18px;
            height: 18px;
            cursor: pointer;
        }

        .aspect-lock label {
            color: #666;
            font-size: 0.9em;
            cursor: pointer;
        }

        .select-group {
            margin-bottom: 20px;
        }

        .select-group label {
            display: block;
            margin-bottom: 8px;
            color: #666;
            font-weight: 500;
        }

        .select-group select {
            width: 100%;
            padding: 12px;
            border: 2px solid #ddd;
            border-radius: 8px;
            font-size: 1em;
            background: white;
            cursor: pointer;
            transition: border-color 0.3s ease;
        }

        .select-group select:focus {
            outline: none;
            border-color: #4facfe;
            box-shadow: 0 0 0 3px rgba(79, 172, 254, 0.1);
        }

        .filename-input-group {
            margin-bottom: 20px;
        }

        .filename-input-group label {
            display: block;
            margin-bottom: 8px;
            color: #666;
            font-weight: 500;
        }

        .filename-input-group input {
            width: 100%;
            padding: 12px;
            border: 2px solid #ddd;
            border-radius: 8px;
            font-size: 1em;
            transition: border-color 0.3s ease;
        }

        .filename-input-group input:focus {
            outline: none;
            border-color: #4facfe;
            box-shadow: 0 0 0 3px rgba(79, 172, 254, 0.1);
        }

        .convert-btn {
            width: 100%;
            padding: 18px;
            background: linear-gradient(135deg, #4facfe 0%, #00f2fe 100%);
            color: white;
            border: none;
            border-radius: 12px;
            font-size: 1.2em;
            font-weight: 600;
            cursor: pointer;
            transition: all 0.3s ease;
            box-shadow: 0 5px 15px rgba(79, 172, 254, 0.4);
        }

        .convert-btn:hover {
            transform: translateY(-2px);
            box-shadow: 0 8px 20px rgba(79, 172, 254, 0.6);
        }

        .convert-btn:active {
            transform: translateY(0);
        }

        .convert-btn:disabled {
            background: #ccc;
            cursor: not-allowed;
            transform: none;
            box-shadow: none;
        }

        /* 多卡片布局样式 */
        .header-section {
            margin-bottom: 20px;
        }

        .add-card-btn {
            padding: 10px 15px;
            background: linear-gradient(135deg, #4facfe 0%, #00f2fe 100%);
            color: white;
            border: none;
            border-radius: 8px;
            cursor: pointer;
            font-weight: 600;
            transition: all 0.3s ease;
        }

        .add-card-btn:hover {
            transform: translateY(-2px);
            box-shadow: 0 5px 15px rgba(79, 172, 254, 0.4);
        }

        #cardsContainer {
            display: flex;
            flex-direction: column;
            gap: 20px;
        }

        .image-card {
            position: relative;
        }

        .delete-card-btn {
            background: none;
            border: none;
            font-size: 1.2em;
            cursor: pointer;
            color: #999;
            transition: color 0.3s ease;
            padding: 5px;
            border-radius: 50%;
        }

        .delete-card-btn:hover {
            color: #ff4757;
            background: #ffebee;
        }

        .delete-card-btn:disabled {
            color: #e0e0e0;
            cursor: not-allowed;
        }

        .image-card h3 {
            color: #333;
            margin: 0;
            font-size: 1.1em;
        }

        .card-status {
            margin-top: 10px;
            font-size: 0.8em;
            color: #999;
            text-align: right;
        }

        /* 进度条样式 */
        .progress-container {
            margin-bottom: 20px;
        }

        .progress-info {
            display: flex;
            justify-content: space-between;
            margin-bottom: 8px;
            font-size: 0.9em;
            color: #666;
        }

        .progress-bar {
            width: 100%;
            height: 12px;
            background-color: #e0e0e0;
            border-radius: 6px;
            overflow: hidden;
            box-shadow: inset 0 2px 4px rgba(0, 0, 0, 0.1);
        }

        .progress-fill {
            height: 100%;
            background: linear-gradient(135deg, #4facfe 0%, #00f2fe 100%);
            border-radius: 6px;
            transition: width 0.3s ease;
            box-shadow: 0 2px 4px rgba(79, 172, 254, 0.3);
        }

        /* 滚动按钮样式 */
        .scroll-btn {
            opacity: 0 !important;
            transition: opacity 0.5s cubic-bezier(0.25, 0.46, 0.45, 0.94) !important;
        }

        /* 滚动按钮悬停显示效果 - 仅在图片数量大于3张时生效 */
        [data-card-index] .images-less-than-4 .scroll-btn {
            opacity: 0 !important;
            display: none !important;
        }

        /* 当图片数量足够时，悬停显示滚动按钮 */
        [data-card-index] :not(.images-less-than-4):hover .scroll-btn {
            opacity: 1 !important;
        }

        @media (max-width: 768px) {
            .main-content {
                flex-direction: column;
            }

            .size-controls {
                flex-direction: column;
                align-items: stretch;
            }

            .aspect-lock {
                margin-left: 0;
            }
        }
    </style>
</head>
<body>
    <div class="container">
        <div class="header">
            <h1>🎨 图片取模工具</h1>
        </div>

        <!-- 标签页 -->
        <div class="tabs">
            <button class="tab-button active" data-tab="image-molding">图片取模</button>
        </div>

        <!-- 图片取模标签内容 -->
        <div class="tab-content active" id="image-molding">
            <div class="main-content">
            <!-- 左侧面板：图片处理卡片 -->
            <div class="left-panel">
                <div class="section header-section">
                    <div style="display: flex; justify-content: space-between; align-items: center;">
                        <h2>图片处理 <span id="cardCount" style="color: #4facfe; font-weight: normal; font-size: 0.8em;">(1个图片选项卡)</span></h2>
                        <button id="addCardBtn" class="add-card-btn">+ 增加图片选项卡</button>
                    </div>
                </div>

                <!-- 图片处理卡片容器 -->
                <div id="cardsContainer">
                    <!-- 卡片模板 -->
                    <div class="image-card section" data-card-index="0">
                        <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 15px;">
                            <h3>图片 1</h3>
                            <button class="delete-card-btn" title="删除图片">🗑️</button>
                        </div>

                        <!-- 图片选择 -->
                        <div class="file-input-container">
                            <input type="file" class="image-file-input file-input" accept="image/jpg,image/jpeg,image/png,image/bmp" multiple>
                            <label class="file-input-label">
                                <i>📁</i>
                                <div>点击或拖拽图片到此处</div>
                                <div style="font-size: 0.8em; color: #999; margin-top: 5px;">支持格式：JPG、JPEG、PNG、BMP</div>
                                <div style="font-size: 0.8em; color: #999; margin-top: 5px;">已添加 <span class="image-count">0</span>/1024 张图片</div>
                            </label>
                        </div>

                        <!-- 原图预览 -->
                        <div style="margin-top: 15px;">
                            <h4 style="margin-bottom: 5px; color: #666;">原图预览</h4>
                            <div style="position: relative; border-radius: 8px; overflow: hidden; background: #000;">
                                <!-- 滚动按钮 -->
                                <button class="scroll-btn scroll-left" style="position: absolute; left: 5px; top: 50%; transform: translateY(-50%); background: linear-gradient(135deg, rgba(79, 172, 254, 0.8), rgba(0, 242, 254, 0.8)); color: white; border: none; border-radius: 50%; width: 32px; height: 32px; cursor: pointer; z-index: 10; box-shadow: 0 2px 8px rgba(0,0,0,0.3); transition: all 0.3s ease; display: flex; justify-content: center; align-items: center; font-size: 18px; font-weight: bold; opacity: 0;">
                                    ◀
                                </button>
                                <button class="scroll-btn scroll-right" style="position: absolute; right: 5px; top: 50%; transform: translateY(-50%); background: linear-gradient(135deg, rgba(79, 172, 254, 0.8), rgba(0, 242, 254, 0.8)); color: white; border: none; border-radius: 50%; width: 32px; height: 32px; cursor: pointer; z-index: 10; box-shadow: 0 2px 8px rgba(0,0,0,0.3); transition: all 0.3s ease; display: flex; justify-content: center; align-items: center; font-size: 18px; font-weight: bold; opacity: 0;">
                                    ▶
                                </button>
                                <!-- 图片容器 -->
                                <div class="preview-scroll-container" style="display: flex; overflow: hidden; height: 150px;">
                                    <div class="preview-images" style="display: flex; transition: transform 0.5s cubic-bezier(0.25, 0.46, 0.45, 0.94);"></div>
                                </div>
                            </div>
                        </div>
                        <!-- 输出预览 -->
                        <div style="margin-top: 15px;">
                            <h4 style="margin-bottom: 5px; color: #666;">输出预览</h4>
                            <div style="position: relative; border-radius: 8px; overflow: hidden; background: #000;">
                                <!-- 滚动按钮 -->
                                <button class="scroll-btn scroll-left" style="position: absolute; left: 5px; top: 50%; transform: translateY(-50%); background: linear-gradient(135deg, rgba(79, 172, 254, 0.8), rgba(0, 242, 254, 0.8)); color: white; border: none; border-radius: 50%; width: 32px; height: 32px; cursor: pointer; z-index: 10; box-shadow: 0 2px 8px rgba(0,0,0,0.3); transition: all 0.3s ease; display: flex; justify-content: center; align-items: center; font-size: 18px; font-weight: bold; opacity: 0;">
                                    ◀
                                </button>
                                <button class="scroll-btn scroll-right" style="position: absolute; right: 5px; top: 50%; transform: translateY(-50%); background: linear-gradient(135deg, rgba(79, 172, 254, 0.8), rgba(0, 242, 254, 0.8)); color: white; border: none; border-radius: 50%; width: 32px; height: 32px; cursor: pointer; z-index: 10; box-shadow: 0 2px 8px rgba(0,0,0,0.3); transition: all 0.3s ease; display: flex; justify-content: center; align-items: center; font-size: 18px; font-weight: bold; opacity: 0;">
                                    ▶
                                </button>
                                <!-- 图片容器 -->
                                <div class="preview-scroll-container" style="display: flex; overflow: hidden; height: 150px;">
                                    <div class="output-preview-images" style="display: flex; transition: transform 0.5s cubic-bezier(0.25, 0.46, 0.45, 0.94);"></div>
                                </div>
                            </div>
                        </div>

                        <!-- 尺寸调整 -->
                        <div style="margin-top: 15px;">
                            <h4 style="margin-bottom: 10px; color: #666;">尺寸调整</h4>
                            <div class="size-controls">
                                <div class="size-input-group">
                                    <label>宽度 (px)</label>
                                    <input type="number" class="width-input" min="1" step="1" disabled>
                                </div>
                                <div class="size-input-group">
                                    <label>高度 (px)</label>
                                    <input type="number" class="height-input" min="1" step="1" disabled>
                                </div>
                                <div class="aspect-lock" style="display: flex; align-items: center; gap: 8px;">
                    <input type="checkbox" class="lock-aspect" checked style="width: 18px; height: 18px; margin: 0; cursor: pointer;">
                    <span>锁定比例</span>
                </div>
                            </div>
                        </div>

                        <!-- 数组名前缀 -->
                        <div style="margin-top: 15px;">
                            <h4 style="margin-bottom: 10px; color: #666;">数组名前缀</h4>
                            <div class="filename-input-group">
                                <input type="text" class="array-prefix-input" placeholder="请输入数组名前缀">
                            </div>
                        </div>

                        <!-- 输出详情 -->
                        <div style="margin-top: 15px;">
                            <h4 style="margin-bottom: 10px; color: #666;">输出详情</h4>
                            <div style="background: #f0f0f0; padding: 15px; border-radius: 8px; font-size: 0.9em;">
                                <div style="display: flex; justify-content: space-between; margin-bottom: 8px;">
                                    <span style="color: #666;">原图数据大小：</span>
                                    <span class="original-size" style="font-weight: bold;">0 B</span>
                                </div>
                                <div style="display: flex; justify-content: space-between; margin-bottom: 8px;">
                                    <span style="color: #666;">输出图片数据大小：</span>
                                    <span class="output-size" style="font-weight: bold;">0 B</span>
                                </div>
                                <div style="display: flex; justify-content: space-between;">
                                    <span style="color: #666;">压缩率：</span>
                                    <span class="compression-ratio" style="font-weight: bold;">0%</span>
                                </div>
                            </div>
                            <div style="display: flex; align-items: center; gap: 10px; margin-top: 15px;">
                                <input type="checkbox" class="combine-as-array" checked style="width: 18px; height: 18px; margin: 0; cursor: pointer;">
                                <span>组合为数组</span>
                            </div>
                        </div>

                        <!-- 卡片状态 -->
                        <div class="card-status" style="margin-top: 10px; font-size: 0.8em; color: #999; text-align: right;"></div>
                    </div>
                </div>
            </div>

            <!-- 右侧面板：全局设置 -->
            <div class="right-panel">
                <!-- 取模设置 -->
                <div class="section">
                    <h2>取模设置</h2>
                    <div class="select-group">
                        <label for="colorFormat">颜色格式</label>
                        <select id="colorFormat">
                            <option value="rgb888">RGB888</option>
                            <option value="rgb565">RGB565</option>
                            <option value="rgb332">RGB332</option>
                        </select>
                    </div>
                    <div class="select-group">
                        <label for="outputFormat">输出格式</label>
                        <select id="outputFormat">
                            <option value=".c">.c 文件</option>
                            <option value=".bin">.bin 文件</option>
                        </select>
                    </div>
                    <div class="select-group">
                        <label for="compressionAlgorithm">压缩算法</label>
                        <select id="compressionAlgorithm">
                            <option value="none" selected>无压缩</option>
                            <option value="rle">RLE 压缩</option>
                        </select>
                    </div>
                    <div class="select-group">
                        <div style="display: flex; align-items: center; gap: 10px;">
                            <input type="checkbox" id="rgb888ReverseOrder" checked style="width: 18px; height: 18px; margin: 0; cursor: pointer;">
                            <span>RGB888反字序</span>
                        </div>
                    </div>
                    <div class="select-group">
                        <div style="display: flex; align-items: center; gap: 10px;">
                            <input type="checkbox" id="rgb565LittleEndian" checked style="width: 18px; height: 18px; margin: 0; cursor: pointer;">
                            <span>RGB565反字序</span>
                        </div>
                    </div>
                    <div class="select-group">
                        <div style="display: flex; align-items: center; gap: 10px; flex-wrap: wrap;">
                            <input type="checkbox" id="transparentFill" checked style="width: 18px; height: 18px; margin: 0; cursor: pointer;">
                            <span>透明填充</span>
                            <input type="text" id="fillColor" value="FFFFFF" placeholder="十六进制颜色值" style="width: 120px; padding: 5px; border: 1px solid #ddd; border-radius: 4px; font-family: monospace;">
                            <div id="colorPreview" style="width: 30px; height: 30px; background-color: #FFFFFF; border: 1px solid #ccc; border-radius: 8px; box-shadow: 0 2px 4px rgba(0,0,0,0.2); margin-left: 5px;"></div>
                        </div>
                    </div>
                    <div class="select-group">
                        <label>颜色深度</label>
                        <div style="display: flex; flex-direction: column; gap: 15px; margin-bottom: 5px;">
                            <!-- 当前RGB组合显示 -->
                            <div style="display: flex; justify-content: center; align-items: center;">
                                <span id="colorDepthValue" style="font-weight: bold; font-size: 1.2em; min-width: 80px; text-align: center; background: #f0f0f0; padding: 5px 15px; border-radius: 5px;">RGB888</span>
                            </div>

                            <!-- 红色通道 -->
                            <div style="display: flex; align-items: center; gap: 10px;">
                                <label for="rDepth" style="min-width: 30px; color: #ff4444;">R:</label>
                                <input type="range" id="rDepth" min="0" max="8" value="8" step="1" style="flex: 1;">
                                <span id="rDepthValue" style="font-weight: bold; min-width: 20px; text-align: center;">8</span>
                            </div>

                            <!-- 绿色通道 -->
                            <div style="display: flex; align-items: center; gap: 10px;">
                                <label for="gDepth" style="min-width: 30px; color: #44ff44;">G:</label>
                                <input type="range" id="gDepth" min="0" max="8" value="8" step="1" style="flex: 1;">
                                <span id="gDepthValue" style="font-weight: bold; min-width: 20px; text-align: center;">8</span>
                            </div>

                            <!-- 蓝色通道 -->
                            <div style="display: flex; align-items: center; gap: 10px;">
                                <label for="bDepth" style="min-width: 30px; color: #4444ff;">B:</label>
                                <input type="range" id="bDepth" min="0" max="8" value="8" step="1" style="flex: 1;">
                                <span id="bDepthValue" style="font-weight: bold; min-width: 20px; text-align: center;">8</span>
                            </div>
                        </div>
                    </div>
                </div>

                <!-- 文件名设置 -->
                <div class="section">
                    <h2>文件名设置</h2>
                    <div class="filename-input-group">
                        <label for="filename">文件名</label>
                        <input type="text" id="filename" value="images" placeholder="请输入文件名">
                    </div>
                </div>

                <!-- 转换按钮和进度条 -->
                <div class="section">
                    <!-- 进度条 -->
                    <div id="progressContainer" class="progress-container">
                        <div class="progress-info">
                            <span id="progressText">准备转换...</span>
                            <span id="progressPercent">0%</span>
                        </div>
                        <div class="progress-bar">
                            <div id="progressFill" class="progress-fill"></div>
                        </div>
                    </div>

                    <!-- 转换按钮 -->
                    <button id="convertBtn" class="convert-btn" disabled>开始转换</button>
                </div>
            </div>
        </div>


    </div>

    <script>
        // 标签页切换功能
        document.addEventListener('DOMContentLoaded', function() {
            const tabButtons = document.querySelectorAll('.tab-button');
            const tabContents = document.querySelectorAll('.tab-content');

            tabButtons.forEach(button => {
                button.addEventListener('click', () => {
                    const targetTab = button.getAttribute('data-tab');

                    // 移除所有活动状态
                    tabButtons.forEach(btn => btn.classList.remove('active'));
                    tabContents.forEach(content => content.classList.remove('active'));

                    // 添加当前活动状态
                    button.classList.add('active');
                    document.getElementById(targetTab).classList.add('active');
                });
            });
        });
        // 全局变量
        let cards = [];
        let nextCardId = 1;

        // 单张图片数据结构
        class ImageItem {
            constructor() {
                this.file = null;
                this.previewUrl = '';
                this.isValid = false;
            }
        }

        // 卡片数据结构
        class ImageCard {
            constructor(index) {
                this.index = index;
                this.images = []; // 存储多张图片
                this.originalWidth = 0;
                this.originalHeight = 0;
                this.aspectRatio = 1;
                this.width = 0;
                this.height = 0;
                this.arrayPrefix = `pic${index + 1}`;
                this.isValid = false;
            }
        }

        // 初始化事件监听
        document.addEventListener('DOMContentLoaded', function() {
            // 初始化第一张卡片
            cards.push(new ImageCard(0));
            initCard(0);
            updateArrayPrefix(0, `pic1`);

            // 添加卡片按钮事件
            document.getElementById('addCardBtn').addEventListener('click', addCard);

            // 文件名验证和调整
            const filenameInput = document.getElementById('filename');
            filenameInput.addEventListener('input', function(e) {
                let value = e.target.value;

                // 移除所有非字母数字和下划线的字符
                value = value.replace(/[^a-zA-Z0-9_]/g, '');

                // 如果以数字开头，添加下划线
                if (/^\d/.test(value)) {
                    value = '_' + value;
                }

                // 允许为空，不设置默认值
                e.target.value = value;
            });

            // 转换按钮事件
            const convertBtn = document.getElementById('convertBtn');
            convertBtn.addEventListener('click', convertAllImages);

            // 颜色格式变化事件
            const colorFormatSelect = document.getElementById('colorFormat');
            colorFormatSelect.addEventListener('change', function() {
                updateChannelValuesByFormat();
                updateAllOutputDetails();
            });

            // 输出格式变化事件
            const outputFormatSelect = document.getElementById('outputFormat');
            outputFormatSelect.addEventListener('change', function() {
                updateAllOutputDetails();
            });

            // 压缩算法变化事件
            const compressionAlgorithmSelect = document.getElementById('compressionAlgorithm');
            compressionAlgorithmSelect.addEventListener('change', function() {
                updateAllOutputDetails();
            });

            // 颜色深度滑块事件
            const rSlider = document.getElementById('rDepth');
            const gSlider = document.getElementById('gDepth');
            const bSlider = document.getElementById('bDepth');

            // 为每个滑块添加事件监听
            rSlider.addEventListener('input', function() {
                const { rMax } = getChannelMaxValue();
                if (parseInt(this.value) > rMax) {
                    this.value = rMax;
                }
                updateChannelValue('r');
                updateColorDepthValue();
                updateAllOutputPreviews();
                updateAllOutputDetails();
            });

            gSlider.addEventListener('input', function() {
                const { gMax } = getChannelMaxValue();
                if (parseInt(this.value) > gMax) {
                    this.value = gMax;
                }
                updateChannelValue('g');
                updateColorDepthValue();
                updateAllOutputPreviews();
                updateAllOutputDetails();
            });

            bSlider.addEventListener('input', function() {
                const { bMax } = getChannelMaxValue();
                if (parseInt(this.value) > bMax) {
                    this.value = bMax;
                }
                updateChannelValue('b');
                updateColorDepthValue();
                updateAllOutputPreviews();
                updateAllOutputDetails();
            });

            // 初始化颜色深度显示
            updateColorDepthValue();

            // 透明填充功能初始化
            const transparentFillCheckbox = document.getElementById('transparentFill');
            const fillColorInput = document.getElementById('fillColor');
            const colorPreview = document.getElementById('colorPreview');

            // 更新颜色预览
            function updateColorPreview() {
                let color = fillColorInput.value.trim().toUpperCase();

                // 验证颜色格式
                if (/^[0-9A-F]{6}$/.test(color)) {
                    // 有效的6位十六进制颜色
                    colorPreview.style.backgroundColor = `#${color}`;
                    fillColorInput.style.borderColor = '#ddd';
                } else {
                    // 无效颜色，显示错误边框
                    fillColorInput.style.borderColor = '#ff4444';
                }
            }

            // 初始化颜色预览
            updateColorPreview();

            // 颜色输入框事件监听
            fillColorInput.addEventListener('input', function(e) {
                // 只允许输入十六进制字符
                let value = e.target.value.toUpperCase().replace(/[^0-9A-F]/g, '');
                // 限制长度为6位
                if (value.length > 6) {
                    value = value.substring(0, 6);
                }
                e.target.value = value;
                updateColorPreview();
            });

            // 失去焦点时自动补全6位
            fillColorInput.addEventListener('blur', function(e) {
                let value = e.target.value.trim().toUpperCase();
                // 如果输入为空或不足6位，自动补全为FFFFFF
                if (value.length === 0 || !/^[0-9A-F]{6}$/.test(value)) {
                    e.target.value = 'FFFFFF';
                    updateColorPreview();
                }
            });
        });

        // 更新单个通道的值显示
        function updateChannelValue(channel) {
            const slider = document.getElementById(`${channel}Depth`);
            const valueDisplay = document.getElementById(`${channel}DepthValue`);
            valueDisplay.textContent = slider.value;
        }

        // 应用颜色深度过滤到图片数据
        function processImageData(imageData, format) {
            const data = imageData.data;

            // 获取当前颜色深度设置
            const rBits = parseInt(document.getElementById('rDepth').value);
            const gBits = parseInt(document.getElementById('gDepth').value);
            const bBits = parseInt(document.getElementById('bDepth').value);

            // 降低颜色深度
            for (let i = 0; i < data.length; i += 4) {
                // 红色通道
                const r = data[i];
                let newR;
                if (rBits === 0) {
                    newR = 0;
                } else {
                    const rShift = 8 - rBits;
                    newR = Math.round((r >> rShift) << rShift);
                }
                data[i] = newR;

                // 绿色通道
                const g = data[i + 1];
                let newG;
                if (gBits === 0) {
                    newG = 0;
                } else {
                    const gShift = 8 - gBits;
                    newG = Math.round((g >> gShift) << gShift);
                }
                data[i + 1] = newG;

                // 蓝色通道
                const b = data[i + 2];
                let newB;
                if (bBits === 0) {
                    newB = 0;
                } else {
                    const bShift = 8 - bBits;
                    newB = Math.round((b >> bShift) << bShift);
                }
                data[i + 2] = newB;

                // 透明度通道保持不变
            }

            return imageData;
        }

        // 将字节数转换为人类可读格式
        function formatBytes(bytes) {
            if (bytes === 0) return '0 B';
            const k = 1024;
            const sizes = ['B', 'KB', 'MB', 'GB'];
            const i = Math.floor(Math.log(bytes) / Math.log(k));
            return parseFloat((bytes / Math.pow(k, i)).toFixed(2)) + ' ' + sizes[i];
        }

        // 并发控制函数，用于限制同时处理的图片数量
        async function concurrencyControl(tasks, limit, callback) {
            const results = [];
            const executing = new Set();

            async function runNext() {
                if (tasks.length === 0) {
                    return;
                }

                const task = tasks.shift();
                const promise = task();
                results.push(promise);
                executing.add(promise);

                promise.finally(() => {
                    executing.delete(promise);
                    if (callback) callback();
                    runNext();
                });
            }

            // 启动初始任务
            const initialTasks = Math.min(limit, tasks.length);
            for (let i = 0; i < initialTasks; i++) {
                runNext();
            }

            return Promise.all(results);
        }

        // 获取设备的最佳并发数
        function getOptimalConcurrency() {
            // 获取CPU核心数，最少1个，最多16个
            const cpuCores = Math.min(16, navigator.hardwareConcurrency || 1);

            // 检测设备内存，根据内存大小调整并发数
            let memoryFactor = 1;
            if (navigator.deviceMemory) {
                if (navigator.deviceMemory < 4) {
                    // 内存小于4GB，降低并发数
                    memoryFactor = 0.5;
                } else if (navigator.deviceMemory < 8) {
                    // 内存4-8GB，保持默认
                    memoryFactor = 0.8;
                }
                // 内存大于8GB，保持默认或增加
            }

            // 计算最佳并发数，最少2个，最多根据CPU核心数调整
            const baseConcurrency = Math.max(2, Math.floor(cpuCores * memoryFactor));

            // 对于图片处理，我们再乘以一个系数，因为图片处理是IO密集型和CPU密集型的结合
            const optimalConcurrency = Math.min(16, Math.floor(baseConcurrency * 1.5));

            return optimalConcurrency;
        }

        // 更新单张卡片的输出详情
        function updateOutputDetails(cardIndex) {
            const card = cards[cardIndex];
            const cardElement = document.querySelector(`[data-card-index="${cardIndex}"]`);
            if (!cardElement) return;

            // 当卡片中没有图片时，重置输出详情为0
            if (!card.isValid || card.images.length === 0 || !card.images[0].previewUrl) {
                // 更新UI显示为0
                cardElement.querySelector('.original-size').textContent = formatBytes(0);
                cardElement.querySelector('.output-size').textContent = formatBytes(0);
                cardElement.querySelector('.compression-ratio').textContent = `0%`;
                return;
            }

            // 获取当前取模设置
            const colorFormat = document.getElementById('colorFormat').value;
            const compressionAlgorithm = document.getElementById('compressionAlgorithm').value;

            // 计算每像素字节数
            let bytesPerPixel = 3; // 默认RGB888
            if (colorFormat === 'rgb565') {
                bytesPerPixel = 2;
            } else if (colorFormat === 'rgb332') {
                bytesPerPixel = 1;
            }

            // 计算单张图片的大小
            const singleImageOriginalSize = card.width * card.height * bytesPerPixel;

            // 计算所有图片的原图总大小
            const totalOriginalSize = singleImageOriginalSize * card.images.length;

            // 如果使用RLE压缩，需要计算所有图片的压缩大小
            if (compressionAlgorithm === 'rle') {
                // 创建临时canvas获取图片数据
                const canvas = document.createElement('canvas');
                canvas.width = card.width;
                canvas.height = card.height;
                const ctx = canvas.getContext('2d');

                // 计算一张图片的压缩大小，然后乘以图片数量
                const img = new Image();
                img.onload = function() {
                    // 检查是否启用透明填充
                    const useTransparentFill = document.getElementById('transparentFill').checked;
                    let fillR = 255, fillG = 255, fillB = 255;

                    if (useTransparentFill) {
                        // 获取填充颜色
                        const fillColor = document.getElementById('fillColor').value.trim().toUpperCase();
                        if (/^[0-9A-F]{6}$/.test(fillColor)) {
                            // 解析RGB值
                            fillR = parseInt(fillColor.substring(0, 2), 16);
                            fillG = parseInt(fillColor.substring(2, 4), 16);
                            fillB = parseInt(fillColor.substring(4, 6), 16);
                        }
                    }

                    // 如果启用透明填充，先绘制填充颜色，再绘制图片
                    if (useTransparentFill) {
                        // 绘制填充颜色
                        ctx.fillStyle = `rgb(${fillR}, ${fillG}, ${fillB})`;
                        ctx.fillRect(0, 0, card.width, card.height);
                        // 绘制图片（会与背景色混合透明像素）
                        ctx.drawImage(img, 0, 0, card.width, card.height);
                    } else {
                        // 直接绘制图片
                        ctx.drawImage(img, 0, 0, card.width, card.height);
                    }

                    // 获取图片数据并应用颜色深度过滤
                    let imageData = ctx.getImageData(0, 0, card.width, card.height);
                    imageData = processImageData(imageData, colorFormat);
                    const data = imageData.data;

                    // 生成像素数据数组
                    const pixelBytes = [];

                    for (let i = 0; i < data.length; i += 4) {
                        const r = data[i];
                        const g = data[i + 1];
                        const b = data[i + 2];

                        if (colorFormat === 'rgb888') {
                            // 检查RGB888反字序设置
                            const isReverseOrder = document.getElementById('rgb888ReverseOrder').checked;
                            if (isReverseOrder) {
                                // BGR顺序
                                pixelBytes.push(b);
                                pixelBytes.push(g);
                                pixelBytes.push(r);
                            } else {
                                // RGB顺序
                                pixelBytes.push(r);
                                pixelBytes.push(g);
                                pixelBytes.push(b);
                            }
                        } else if (colorFormat === 'rgb565') {
                            const r5 = (r >> 3) & 0x1F;
                            const g6 = (g >> 2) & 0x3F;
                            const b5 = (b >> 3) & 0x1F;
                            const value = (r5 << 11) | (g6 << 5) | b5;
                            const lowByte = value & 0xFF;
                            const highByte = (value >> 8) & 0xFF;

                            // 检查字节顺序设置
                            const isLittleEndian = document.getElementById('rgb565LittleEndian').checked;
                            if (isLittleEndian) {
                                // 低字节在前，高字节在后（小端序）
                                pixelBytes.push(lowByte);
                                pixelBytes.push(highByte);
                            } else {
                                // 高字节在前，低字节在后（大端序）
                                pixelBytes.push(highByte);
                                pixelBytes.push(lowByte);
                            }
                        } else if (colorFormat === 'rgb332') {
                            const r3 = (r >> 5) & 0x07;
                            const g3 = (g >> 5) & 0x07;
                            const b2 = (b >> 6) & 0x03;
                            const value = (r3 << 5) | (g3 << 2) | b2;
                            pixelBytes.push(value);
                        }
                    }

                    // 应用RLE压缩
                    const compressed = rleCompress(pixelBytes, colorFormat);
                    const singleImageOutputSize = compressed.length;

                    // 计算所有图片的输出总大小
                    const totalOutputSize = singleImageOutputSize * card.images.length;

                    // 计算总压缩率
                    const compressionRatio = totalOriginalSize > 0 ? ((totalOriginalSize - totalOutputSize) / totalOriginalSize * 100).toFixed(2) : 0;

                    // 更新UI显示
                    cardElement.querySelector('.original-size').textContent = formatBytes(totalOriginalSize);
                    cardElement.querySelector('.output-size').textContent = formatBytes(totalOutputSize);
                    cardElement.querySelector('.compression-ratio').textContent = `${compressionRatio}%`;
                };
                img.src = card.images[0].previewUrl;
            } else {
                // 无压缩情况，所有图片输出大小等于原图大小
                const totalOutputSize = totalOriginalSize;
                const compressionRatio = 0;

                // 更新UI显示
                cardElement.querySelector('.original-size').textContent = formatBytes(totalOriginalSize);
                cardElement.querySelector('.output-size').textContent = formatBytes(totalOutputSize);
                cardElement.querySelector('.compression-ratio').textContent = `${compressionRatio}%`;
            }
        }

        // 更新所有卡片的输出详情
        function updateAllOutputDetails() {
            for (let i = 0; i < cards.length; i++) {
                updateOutputDetails(i);
            }
        }

        // 更新颜色深度显示值
        function updateColorDepthValue() {
            const r = document.getElementById('rDepth').value;
            const g = document.getElementById('gDepth').value;
            const b = document.getElementById('bDepth').value;
            const colorDepthValue = document.getElementById('colorDepthValue');
            colorDepthValue.textContent = `RGB${r}${g}${b}`;
        }

        // 获取各通道的最大允许值
        function getChannelMaxValue() {
            const colorFormat = document.getElementById('colorFormat').value;
            let rMax = 8, gMax = 8, bMax = 8;

            // 根据颜色格式设置各通道的最大允许值
            if (colorFormat === 'rgb565') {
                rMax = 5;
                gMax = 6;
                bMax = 5;
            } else if (colorFormat === 'rgb332') {
                rMax = 3;
                gMax = 3;
                bMax = 2;
            }

            return { rMax, gMax, bMax };
        }

        // 根据颜色格式更新各通道的值
        function updateChannelValuesByFormat() {
            const { rMax, gMax, bMax } = getChannelMaxValue();

            const rSlider = document.getElementById('rDepth');
            const gSlider = document.getElementById('gDepth');
            const bSlider = document.getElementById('bDepth');

            // 直接将各通道值重置到对应颜色格式的最大值
            rSlider.value = rMax;
            updateChannelValue('r');

            gSlider.value = gMax;
            updateChannelValue('g');

            bSlider.value = bMax;
            updateChannelValue('b');

            // 更新颜色深度显示和输出预览
            updateColorDepthValue();
            updateAllOutputPreviews();
        }

        // 更新所有卡片的输出预览
        function updateAllOutputPreviews() {
            for (let i = 0; i < cards.length; i++) {
                // 无论卡片是否有效，都更新预览，确保滚动按钮正确显示/隐藏
                updateOriginalPreviews(i);
                updateOutputPreview(i);
            }
        }

        // 调整预览窗口大小
        function adjustPreviewHeight(cardIndex, isExpanded) {
            const cardElement = document.querySelector(`[data-card-index="${cardIndex}"]`);
            if (!cardElement) return;

            // 获取原图预览和输出预览的容器
            const previewContainers = cardElement.querySelectorAll('.preview-scroll-container');
            if (previewContainers.length < 2) return;

            // 设置高度
            const height = isExpanded ? '150px' : '75px';
            previewContainers[0].style.height = height;
            previewContainers[1].style.height = height;
        }

        // 删除图片
        function deleteImage(cardIndex, imageIndex) {
            const card = cards[cardIndex];
            if (!card || imageIndex < 0 || imageIndex >= card.images.length) return;

            // 从数组中移除图片
            card.images.splice(imageIndex, 1);

            // 更新卡片状态
            card.isValid = card.images.length > 0;

            // 如果删除后没有图片了，重置卡片尺寸
            if (card.images.length === 0) {
                card.originalWidth = 0;
                card.originalHeight = 0;
                card.aspectRatio = 1;
                card.width = 0;
                card.height = 0;

                // 重置尺寸输入框
                const cardElement = document.querySelector(`[data-card-index="${cardIndex}"]`);
                const widthInput = cardElement.querySelector('.width-input');
                const heightInput = cardElement.querySelector('.height-input');
                widthInput.value = '';
                heightInput.value = '';
                widthInput.disabled = true;
                heightInput.disabled = true;
            }

            // 更新图片数量显示
            updateImageCountDisplay(cardIndex);

            // 更新原图预览
            updateOriginalPreviews(cardIndex);

            // 更新输出预览
            updateOutputPreview(cardIndex);

            // 更新输出详情
            updateOutputDetails(cardIndex);

            // 更新卡片状态显示
            const cardElement = document.querySelector(`[data-card-index="${cardIndex}"]`);
            if (card.images.length > 0) {
                updateCardStatus(cardIndex, `✅ 已添加 ${card.images.length} 张图片`);
            } else {
                updateCardStatus(cardIndex, '');
            }

            // 检查转换按钮状态
            checkConvertButtonState();
        }

        // 更新单张卡片的原图预览
        function updateOriginalPreviews(cardIndex) {
            const card = cards[cardIndex];
            const cardElement = document.querySelector(`[data-card-index="${cardIndex}"]`);
            const previewContainer = cardElement.querySelector('.preview-images');
            const scrollContainer = cardElement.querySelector('.preview-scroll-container');

            // 获取原图预览的父容器
            const originalPreviewParent = scrollContainer.parentElement;

            // 清空现有预览
            previewContainer.innerHTML = '';

            // 获取预览容器尺寸
            const containerHeight = 150;
            const containerWidth = scrollContainer.clientWidth;

            // 每张图片的宽度：容器宽度除以3，减去边距
            const imageWidth = (containerWidth / 3) - 10; // 减去10px的边距（5px * 2）

            card.images.forEach((imageItem, index) => {
                if (imageItem.previewUrl) {
                    // 创建图片容器
                    const imgContainer = document.createElement('div');
                    imgContainer.style.position = 'relative';
                    imgContainer.style.height = '100%';
                    imgContainer.style.width = `${imageWidth}px`;
                    imgContainer.style.margin = '0 5px';
                    imgContainer.style.flexShrink = '0';
                    imgContainer.style.display = 'flex';
                    imgContainer.style.justifyContent = 'center';
                    imgContainer.style.alignItems = 'center';
                    imgContainer.style.background = '#000';
                    imgContainer.style.borderRadius = '4px';
                    imgContainer.style.overflow = 'hidden';
                    imgContainer.style.transition = 'all 0.3s ease';

                    // 添加悬停效果
                    imgContainer.addEventListener('mouseenter', function() {
                        this.style.opacity = '0.8';
                        this.querySelector('.delete-icon').style.display = 'block';
                    });

                    imgContainer.addEventListener('mouseleave', function() {
                        this.style.opacity = '1';
                        this.querySelector('.delete-icon').style.display = 'none';
                    });

                    // 创建图片元素
                    const img = document.createElement('img');
                    img.src = imageItem.previewUrl;
                    img.alt = `原图 ${index + 1}`;
                    img.style.objectFit = 'contain';
                    img.style.imageRendering = 'pixelated';
                    img.style.imageRendering = 'crisp-edges';
                    img.style.height = '100%';
                    img.style.width = '100%';
                    img.style.transition = 'all 0.3s ease';

                    // 创建删除按钮
                    const deleteBtn = document.createElement('div');
                    deleteBtn.className = 'delete-icon';
                    deleteBtn.style.position = 'absolute';
                    deleteBtn.style.top = '5px';
                    deleteBtn.style.right = '5px';
                    deleteBtn.style.width = '24px';
                    deleteBtn.style.height = '24px';
                    deleteBtn.style.background = 'rgba(255, 0, 0, 0.8)';
                    deleteBtn.style.color = 'white';
                    deleteBtn.style.borderRadius = '50%';
                    deleteBtn.style.display = 'none';
                    deleteBtn.style.justifyContent = 'center';
                    deleteBtn.style.alignItems = 'center';
                    deleteBtn.style.cursor = 'pointer';
                    deleteBtn.style.fontSize = '18px';
                    deleteBtn.style.fontWeight = 'bold';
                    deleteBtn.style.lineHeight = '24px';
                    deleteBtn.style.textAlign = 'center';
                    deleteBtn.style.transition = 'all 0.3s ease';
                    deleteBtn.style.zIndex = '10';
                    deleteBtn.innerHTML = '×';

                    // 添加删除事件
                    deleteBtn.addEventListener('click', function(e) {
                        e.stopPropagation();
                        deleteImage(cardIndex, index);
                    });

                    // 组装图片容器
                    imgContainer.appendChild(img);
                    imgContainer.appendChild(deleteBtn);
                    previewContainer.appendChild(imgContainer);
                }
            });

            // 根据图片数量调整样式
            if (card.images.length < 4) {
                // 1-3张图片，居中对齐
                scrollContainer.style.justifyContent = 'center';
                scrollContainer.style.alignItems = 'center';
                previewContainer.style.transform = 'translateX(0)'; // 重置transform
                previewContainer.style.width = 'auto'; // 自动宽度，不超出父容器
                originalPreviewParent.classList.add('images-less-than-4');
            } else {
                // 4张及以上，左对齐
                scrollContainer.style.justifyContent = 'flex-start';
                previewContainer.style.width = 'fit-content'; // 适应内容宽度，允许滚动
                originalPreviewParent.classList.remove('images-less-than-4');

                // 检查并调整滚动位置，确保始终显示有效的图片内容
                adjustScrollPosition(cardIndex);
            }

            // 重新初始化滚动功能，确保滚动按钮正常工作
            initScrollFunctionality(cardIndex);
        }

        // 更新单张卡片的输出预览
        function updateOutputPreview(cardIndex) {
            const card = cards[cardIndex];
            const cardElement = document.querySelector(`[data-card-index="${cardIndex}"]`);
            const outputContainer = cardElement.querySelector('.output-preview-images');
            const scrollContainers = cardElement.querySelectorAll('.preview-scroll-container');

            // 获取输出预览的滚动容器和父容器
            const outputScrollContainer = scrollContainers[1];
            const outputPreviewParent = outputScrollContainer.parentElement;

            // 清空现有预览
            outputContainer.innerHTML = '';

            // 获取预览容器尺寸
            const containerHeight = 150;
            const containerWidth = scrollContainers[0].clientWidth;

            // 每张图片的宽度：容器宽度除以3，减去边距
            const imageWidth = (containerWidth / 3) - 10; // 减去10px的边距（5px * 2）

            // 计算缩放比例，确保图片高度适应容器
            const scale = containerHeight / card.height;
            const displayHeight = containerHeight;

            card.images.forEach((imageItem, index) => {
                if (imageItem.previewUrl) {
                    // 创建canvas容器
                    const canvasContainer = document.createElement('div');
                    canvasContainer.style.position = 'relative';
                    canvasContainer.style.height = '100%';
                    canvasContainer.style.width = `${imageWidth}px`;
                    canvasContainer.style.margin = '0 5px';
                    canvasContainer.style.flexShrink = '0';
                    canvasContainer.style.display = 'flex';
                    canvasContainer.style.justifyContent = 'center';
                    canvasContainer.style.alignItems = 'center';
                    canvasContainer.style.background = '#000';
                    canvasContainer.style.borderRadius = '4px';
                    canvasContainer.style.overflow = 'hidden';
                    canvasContainer.style.transition = 'all 0.3s ease';

                    // 添加悬停效果
                    canvasContainer.addEventListener('mouseenter', function() {
                        this.style.opacity = '0.8';
                        this.querySelector('.delete-icon').style.display = 'block';
                    });

                    canvasContainer.addEventListener('mouseleave', function() {
                        this.style.opacity = '1';
                        this.querySelector('.delete-icon').style.display = 'none';
                    });

                    // 创建canvas元素
                    const canvas = document.createElement('canvas');
                    canvas.style.height = '100%';
                    canvas.style.width = '100%';
                    canvas.style.transition = 'all 0.3s ease';

                    canvas.width = imageWidth;
                    canvas.height = displayHeight;

                    const ctx = canvas.getContext('2d');

                    // 加载图片并处理
                    const img = new Image();
                    img.onload = function() {
                        // 绘制原始图片到临时canvas
                        const tempCanvas = document.createElement('canvas');
                        tempCanvas.width = card.width;
                        tempCanvas.height = card.height;
                        const tempCtx = tempCanvas.getContext('2d');
                        tempCtx.drawImage(img, 0, 0, card.width, card.height);

                        // 获取原始像素数据
                        let imageData = tempCtx.getImageData(0, 0, card.width, card.height);
                        imageData = processImageData(imageData, document.getElementById('colorFormat').value);

                        // 将处理后的数据绘制到临时canvas
                        tempCtx.putImageData(imageData, 0, 0);

                        // 清空输出预览canvas
                        ctx.clearRect(0, 0, imageWidth, displayHeight);

                        // 设置图像平滑禁用，保持像素清晰
                        ctx.imageSmoothingEnabled = false;

                        // 绘制缩放后的图像
                        ctx.drawImage(tempCanvas, 0, 0, card.width, card.height, 0, 0, imageWidth, displayHeight);
                    };
                    img.src = imageItem.previewUrl;

                    // 创建删除按钮
                    const deleteBtn = document.createElement('div');
                    deleteBtn.className = 'delete-icon';
                    deleteBtn.style.position = 'absolute';
                    deleteBtn.style.top = '5px';
                    deleteBtn.style.right = '5px';
                    deleteBtn.style.width = '24px';
                    deleteBtn.style.height = '24px';
                    deleteBtn.style.background = 'rgba(255, 0, 0, 0.8)';
                    deleteBtn.style.color = 'white';
                    deleteBtn.style.borderRadius = '50%';
                    deleteBtn.style.display = 'none';
                    deleteBtn.style.justifyContent = 'center';
                    deleteBtn.style.alignItems = 'center';
                    deleteBtn.style.cursor = 'pointer';
                    deleteBtn.style.fontSize = '18px';
                    deleteBtn.style.fontWeight = 'bold';
                    deleteBtn.style.lineHeight = '24px';
                    deleteBtn.style.textAlign = 'center';
                    deleteBtn.style.transition = 'all 0.3s ease';
                    deleteBtn.style.zIndex = '10';
                    deleteBtn.innerHTML = '×';

                    // 添加删除事件
                    deleteBtn.addEventListener('click', function(e) {
                        e.stopPropagation();
                        deleteImage(cardIndex, index);
                    });

                    // 组装canvas容器
                    canvasContainer.appendChild(canvas);
                    canvasContainer.appendChild(deleteBtn);
                    outputContainer.appendChild(canvasContainer);
                }
            });

            // 根据图片数量调整样式
            if (card.images.length < 4) {
                // 1-3张图片，居中对齐
                outputScrollContainer.style.justifyContent = 'center';
                outputScrollContainer.style.alignItems = 'center';
                outputContainer.style.transform = 'translateX(0)'; // 重置transform
                outputContainer.style.width = 'auto'; // 自动宽度，不超出父容器
                outputPreviewParent.classList.add('images-less-than-4');
            } else {
                // 4张及以上，左对齐
                outputScrollContainer.style.justifyContent = 'flex-start';
                outputContainer.style.width = 'fit-content'; // 适应内容宽度，允许滚动
                outputPreviewParent.classList.remove('images-less-than-4');
            }
        }

        // 调整滚动位置，确保始终显示有效的图片内容
        function adjustScrollPosition(cardIndex) {
            const cardElement = document.querySelector(`[data-card-index="${cardIndex}"]`);

            // 获取两个预览容器
            const scrollContainers = cardElement.querySelectorAll('.preview-scroll-container');
            if (scrollContainers.length < 2) return;

            const originalPreviewContainer = scrollContainers[0];
            const originalImagesContainer = originalPreviewContainer.querySelector('.preview-images');
            const outputImagesContainer = scrollContainers[1].querySelector('.output-preview-images');

            // 获取容器尺寸和图片数量
            const containerWidth = originalPreviewContainer.clientWidth;
            const imageCount = cards[cardIndex].images.length;
            const firstImage = originalImagesContainer.firstElementChild;

            if (!firstImage) return;

            // 计算每张图片的宽度（包含边距）
            const imageWidthWithMargin = firstImage.clientWidth + 10; // 5px margin on each side

            // 计算可见图片数量（固定为3张）
            const visibleImages = 3;

            // 计算最大滚动位置（索引）
            const maxScrollIndex = Math.max(0, imageCount - visibleImages);

            // 计算当前滚动位置（像素）
            const currentTransform = originalImagesContainer.style.transform;
            let currentScrollPixels = 0;
            if (currentTransform) {
                const match = currentTransform.match(/translateX\((-?\d+)px\)/);
                if (match) {
                    currentScrollPixels = parseInt(match[1]);
                }
            }

            // 计算当前滚动索引
            let currentScrollIndex = Math.abs(Math.round(currentScrollPixels / imageWidthWithMargin));

            // 检查当前滚动位置是否超出最大滚动索引
            if (currentScrollIndex > maxScrollIndex) {
                // 调整滚动索引到最大有效值
                currentScrollIndex = maxScrollIndex;

                // 应用调整后的滚动位置
                const newTransform = `translateX(${-currentScrollIndex * imageWidthWithMargin}px)`;
                originalImagesContainer.style.transform = newTransform;
                outputImagesContainer.style.transform = newTransform;
            }
        }

        // 初始化滚动功能
        function initScrollFunctionality(cardIndex) {
            const cardElement = document.querySelector(`[data-card-index="${cardIndex}"]`);

            // 获取所有预览滚动容器和滚动按钮
            const previewContainers = cardElement.querySelectorAll('.preview-scroll-container');
            const scrollButtons = cardElement.querySelectorAll('.scroll-btn');

            if (previewContainers.length < 2 || scrollButtons.length < 4) return;

            // 原图预览滚动（第一个预览容器）
            const originalPreviewContainer = previewContainers[0];
            const originalImagesContainer = originalPreviewContainer.querySelector('.preview-images');

            // 输出预览滚动（第二个预览容器）
            const outputPreviewContainer = previewContainers[1];
            const outputImagesContainer = outputPreviewContainer.querySelector('.output-preview-images');

            // 获取所有滚动按钮
            const allLeftBtns = cardElement.querySelectorAll('.scroll-left');
            const allRightBtns = cardElement.querySelectorAll('.scroll-right');

            // 移除旧的事件监听器，避免多次绑定
            allLeftBtns.forEach(btn => {
                // 克隆按钮并保留class属性
                const clone = btn.cloneNode(true);
                // 确保克隆的按钮也有正确的初始样式
                clone.style.opacity = '0';
                btn.replaceWith(clone);
            });

            allRightBtns.forEach(btn => {
                // 克隆按钮并保留class属性
                const clone = btn.cloneNode(true);
                // 确保克隆的按钮也有正确的初始样式
                clone.style.opacity = '0';
                btn.replaceWith(clone);
            });

            // 更新按钮引用
            const updatedLeftBtns = cardElement.querySelectorAll('.scroll-left');
            const updatedRightBtns = cardElement.querySelectorAll('.scroll-right');

            // 计算可见图片数量（使用第一个容器作为参考）
            function getVisibleImageCount() {
                const containerWidth = originalPreviewContainer.clientWidth;
                const firstImage = originalImagesContainer.firstElementChild;
                if (!firstImage) return 0;
                const imageWidth = firstImage.clientWidth + 10; // 包含边距
                return Math.max(1, Math.floor(containerWidth / imageWidth));
            }

            // 获取当前滚动位置（从transform属性中读取）
            function getCurrentScrollIndex() {
                const firstImage = originalImagesContainer.firstElementChild;
                if (!firstImage) return 0;

                const imageWidth = firstImage.clientWidth + 10; // 包含边距
                const currentTransform = originalImagesContainer.style.transform;
                let currentScrollPixels = 0;

                if (currentTransform) {
                    const match = currentTransform.match(/translateX\((-?\d+)px\)/);
                    if (match) {
                        currentScrollPixels = parseInt(match[1]);
                    }
                }

                return Math.max(0, Math.round(Math.abs(currentScrollPixels) / imageWidth));
            }

            // 同步滚动到指定索引
            function scrollToIndex(index) {
                // 获取第一个图片的宽度作为参考
                const firstImage = originalImagesContainer.firstElementChild;
                if (!firstImage) return;

                const imageWidth = firstImage.clientWidth + 10; // 包含边距
                const visibleCount = getVisibleImageCount();
                const totalImages = Math.max(originalImagesContainer.children.length, outputImagesContainer.children.length);
                const maxScroll = Math.max(0, totalImages - visibleCount);

                // 获取当前实际滚动索引
                const currentIndex = getCurrentScrollIndex();

                // 检查是否需要回弹：只有当当前已经在边界，且尝试继续超出边界时才回弹
                const isAtLeftBoundary = currentIndex === 0;
                const isAtRightBoundary = currentIndex === maxScroll;
                const tryingToGoLeft = index < currentIndex;
                const tryingToGoRight = index > currentIndex;
                const needBounce = (isAtLeftBoundary && tryingToGoLeft) || (isAtRightBoundary && tryingToGoRight);

                if (needBounce) {
                    // 检查是否正在执行回弹动画，如果是则直接返回
                    if (originalImagesContainer.style.transition.includes('ease')) {
                        // 停止自动滚动，避免持续回弹
                        stopAutoScroll();
                        return;
                    }

                    let bounceOffset = 0;

                    // 计算回弹偏移量
                    if (isAtLeftBoundary) {
                        // 左边界回弹 - 向右移动
                        bounceOffset = 0.2 * imageWidth;
                    } else if (isAtRightBoundary) {
                        // 右边界回弹 - 向左移动
                        bounceOffset = -0.2 * imageWidth;
                    }

                    // 应用回弹效果，使用CSS过渡动画
                    const bouncePosition = -currentIndex * imageWidth + bounceOffset;
                    originalImagesContainer.style.transition = 'transform 0.15s ease';
                    outputImagesContainer.style.transition = 'transform 0.15s ease';
                    originalImagesContainer.style.transform = `translateX(${bouncePosition}px)`;
                    outputImagesContainer.style.transform = `translateX(${bouncePosition}px)`;

                    // 回弹后恢复到边界位置
                    setTimeout(() => {
                        originalImagesContainer.style.transform = `translateX(${-currentIndex * imageWidth}px)`;
                        outputImagesContainer.style.transform = `translateX(${-currentIndex * imageWidth}px)`;
                        // 清除过渡效果，避免影响后续滚动
                        setTimeout(() => {
                            originalImagesContainer.style.transition = '';
                            outputImagesContainer.style.transition = '';
                        }, 150);
                    }, 150);

                    // 停止自动滚动，避免持续回弹
                    stopAutoScroll();
                } else {
                    // 计算目标索引（限制在有效范围内）
                    let targetIndex = index;
                    if (targetIndex < 0) {
                        targetIndex = 0;
                    } else if (targetIndex > maxScroll) {
                        targetIndex = maxScroll;
                    }

                    // 正常滚动：只有当目标索引与当前索引不同时才执行滚动
                    if (targetIndex !== currentIndex) {
                        // 为正常滚动添加平滑过渡动画
                        originalImagesContainer.style.transition = 'transform 0.5s cubic-bezier(0.25, 0.46, 0.45, 0.94)';
                        outputImagesContainer.style.transition = 'transform 0.5s cubic-bezier(0.25, 0.46, 0.45, 0.94)';
                        const finalTransform = `translateX(${-targetIndex * imageWidth}px)`;
                        originalImagesContainer.style.transform = finalTransform;
                        outputImagesContainer.style.transform = finalTransform;
                    }
                }
            }

            // 滚动一个单位
            function scrollOneStep(direction) {
                const currentIndex = getCurrentScrollIndex();
                scrollToIndex(currentIndex + direction * 1);
            }

            // 开始自动滚动
            let isScrolling = false;
            let scrollInterval = null;
            const scrollSpeed = 200; // 滚动速度（毫秒/次）

            function startAutoScroll(direction) {
                if (isScrolling) return;

                isScrolling = true;

                scrollInterval = setInterval(() => {
                    scrollOneStep(direction);
                }, scrollSpeed);
            }

            // 停止自动滚动
            function stopAutoScroll() {
                isScrolling = false;
                if (scrollInterval) {
                    clearInterval(scrollInterval);
                    scrollInterval = null;
                }
            }

            // 长按状态跟踪
            let isLongPress = false;
            let longPressTimeout = null;

            // 为所有左按钮添加事件
            updatedLeftBtns.forEach(btn => {
                // 鼠标按下事件
                btn.addEventListener('mousedown', () => {
                    // 标记为可能的长按
                    isLongPress = false;
                    // 设置长按超时
                    longPressTimeout = setTimeout(() => {
                        isLongPress = true;
                        startAutoScroll(-1);
                    }, 200); // 200ms 后视为长按
                    // 立即执行一次滚动
                    scrollOneStep(-1);
                });

                // 点击事件（仅处理短按）
                btn.addEventListener('click', (e) => {
                    // 如果是长按，则忽略点击事件
                    if (isLongPress) {
                        e.preventDefault();
                        isLongPress = false;
                        return;
                    }
                    // 清除长按超时
                    if (longPressTimeout) {
                        clearTimeout(longPressTimeout);
                        longPressTimeout = null;
                    }
                });
            });

            // 为所有右按钮添加事件
            updatedRightBtns.forEach(btn => {
                // 鼠标按下事件
                btn.addEventListener('mousedown', () => {
                    // 标记为可能的长按
                    isLongPress = false;
                    // 设置长按超时
                    longPressTimeout = setTimeout(() => {
                        isLongPress = true;
                        startAutoScroll(1);
                    }, 200); // 200ms 后视为长按
                    // 立即执行一次滚动
                    scrollOneStep(1);
                });

                // 点击事件（仅处理短按）
                btn.addEventListener('click', (e) => {
                    // 如果是长按，则忽略点击事件
                    if (isLongPress) {
                        e.preventDefault();
                        isLongPress = false;
                        return;
                    }
                    // 清除长按超时
                    if (longPressTimeout) {
                        clearTimeout(longPressTimeout);
                        longPressTimeout = null;
                    }
                });
            });

            // 停止长按滚动
            function handleMouseUpOrLeave() {
                // 清除长按超时
                if (longPressTimeout) {
                    clearTimeout(longPressTimeout);
                    longPressTimeout = null;
                }
                // 停止自动滚动
                stopAutoScroll();
                // 重置长按状态
                isLongPress = false;
            }

            document.addEventListener('mouseup', handleMouseUpOrLeave);
            document.addEventListener('mouseleave', handleMouseUpOrLeave);

            // 为所有按钮添加鼠标离开事件
            [...updatedLeftBtns, ...updatedRightBtns].forEach(btn => {
                btn.addEventListener('mouseleave', handleMouseUpOrLeave);
            });
        }

        // 初始化卡片事件
        function initCard(cardIndex) {
            const card = document.querySelector(`[data-card-index="${cardIndex}"]`);

            // 初始化时将预览窗口高度设置为75px
            adjustPreviewHeight(cardIndex, false);

            // 初始化预览，确保滚动按钮正确显示/隐藏
            updateOriginalPreviews(cardIndex);
            updateOutputPreview(cardIndex);

            // 初始化滚动功能
            initScrollFunctionality(cardIndex);

            // 图片选择事件 - 动态获取当前索引
            const fileInput = card.querySelector('.image-file-input');
            fileInput.addEventListener('change', function(e) {
                const currentIndex = parseInt(this.closest('.image-card').getAttribute('data-card-index'));
                const card = cards[currentIndex];
                const maxImages = 1024;

                // 计算剩余可添加的图片数量
                const remainingSlots = maxImages - card.images.length;

                // 如果剩余数量不足，只处理部分文件
                if (e.target.files.length > remainingSlots) {
                    alert(`每个选项卡最多只能添加${maxImages}张图片，当前还可添加${remainingSlots}张！`);
                    return;
                }

                // 批量处理选中的文件
                const filesToProcess = Array.from(e.target.files);
                batchHandleImageSelect(currentIndex, filesToProcess);

                // 重置input值，允许再次选择同一文件
                this.value = '';
            });

            // 宽度输入变化 - 动态获取当前索引
            const widthInput = card.querySelector('.width-input');
            widthInput.addEventListener('input', function(e) {
                const currentIndex = parseInt(this.closest('.image-card').getAttribute('data-card-index'));
                handleWidthChange(currentIndex, parseInt(e.target.value) || 1);
            });

            // 高度输入变化 - 动态获取当前索引
            const heightInput = card.querySelector('.height-input');
            heightInput.addEventListener('input', function(e) {
                const currentIndex = parseInt(this.closest('.image-card').getAttribute('data-card-index'));
                handleHeightChange(currentIndex, parseInt(e.target.value) || 1);
            });

            // 锁定比例变化 - 动态获取当前索引
            const lockAspect = card.querySelector('.lock-aspect');
            lockAspect.addEventListener('change', function(e) {
                const currentIndex = parseInt(this.closest('.image-card').getAttribute('data-card-index'));
                handleAspectLockChange(currentIndex, e.target.checked);
            });

            // 数组名前缀变化 - 动态获取当前索引
            const arrayPrefixInput = card.querySelector('.array-prefix-input');
            arrayPrefixInput.addEventListener('input', function(e) {
                const currentIndex = parseInt(this.closest('.image-card').getAttribute('data-card-index'));
                handleArrayPrefixChange(currentIndex, e.target.value);
            });

            // 删除卡片事件 - 动态获取当前索引
            const deleteBtn = card.querySelector('.delete-card-btn');
            deleteBtn.addEventListener('click', function() {
                const currentIndex = parseInt(this.closest('.image-card').getAttribute('data-card-index'));
                deleteCard(currentIndex);
            });
        }

        // 添加新卡片
        function addCard() {
            const cardsContainer = document.getElementById('cardsContainer');
            const cardCount = cardsContainer.children.length;
            const newCardIndex = cardCount;

            // 创建新卡片
            const newCard = document.createElement('div');
            newCard.className = 'image-card section';
            newCard.setAttribute('data-card-index', newCardIndex);

            // 设置卡片内容
            newCard.innerHTML = `
                <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 15px;">
                    <h3>图片 ${newCardIndex + 1}</h3>
                    <button class="delete-card-btn" title="删除图片">🗑️</button>
                </div>

                <!-- 图片选择 -->
                <div class="file-input-container">
                    <input type="file" class="image-file-input file-input" accept="image/jpg,image/jpeg,image/png,image/bmp" multiple>
                    <label class="file-input-label">
                        <i>📁</i>
                        <div>点击或拖拽图片到此处</div>
                        <div style="font-size: 0.8em; color: #999; margin-top: 5px;">支持格式：JPG、JPEG、PNG、BMP</div>
                        <div style="font-size: 0.8em; color: #999; margin-top: 5px;">已添加 <span class="image-count">0</span>/1024 张图片</div>
                    </label>
                </div>

                <!-- 原图预览 -->
                        <div style="margin-top: 15px;">
                            <h4 style="margin-bottom: 5px; color: #666;">原图预览</h4>
                            <div style="position: relative; border-radius: 8px; overflow: hidden; background: #000;">
                                <!-- 滚动按钮 -->
                                <button class="scroll-btn scroll-left" style="position: absolute; left: 5px; top: 50%; transform: translateY(-50%); background: linear-gradient(135deg, rgba(79, 172, 254, 0.8), rgba(0, 242, 254, 0.8)); color: white; border: none; border-radius: 50%; width: 32px; height: 32px; cursor: pointer; z-index: 10; box-shadow: 0 2px 8px rgba(0,0,0,0.3); transition: all 0.3s ease; display: flex; justify-content: center; align-items: center; font-size: 18px; font-weight: bold; opacity: 0;">
                                    ◀
                                </button>
                                <button class="scroll-btn scroll-right" style="position: absolute; right: 5px; top: 50%; transform: translateY(-50%); background: linear-gradient(135deg, rgba(79, 172, 254, 0.8), rgba(0, 242, 254, 0.8)); color: white; border: none; border-radius: 50%; width: 32px; height: 32px; cursor: pointer; z-index: 10; box-shadow: 0 2px 8px rgba(0,0,0,0.3); transition: all 0.3s ease; display: flex; justify-content: center; align-items: center; font-size: 18px; font-weight: bold; opacity: 0;">
                                    ▶
                                </button>
                                <!-- 图片容器 -->
                                <div class="preview-scroll-container" style="display: flex; overflow: hidden; height: 150px;">
                                    <div class="preview-images" style="display: flex; transition: transform 0.3s ease;"></div>
                                </div>
                            </div>
                        </div>
                        <!-- 输出预览 -->
                        <div style="margin-top: 15px;">
                            <h4 style="margin-bottom: 5px; color: #666;">输出预览</h4>
                            <div style="position: relative; border-radius: 8px; overflow: hidden; background: #000;">
                                <!-- 滚动按钮 -->
                                <button class="scroll-btn scroll-left" style="position: absolute; left: 5px; top: 50%; transform: translateY(-50%); background: linear-gradient(135deg, rgba(79, 172, 254, 0.8), rgba(0, 242, 254, 0.8)); color: white; border: none; border-radius: 50%; width: 32px; height: 32px; cursor: pointer; z-index: 10; box-shadow: 0 2px 8px rgba(0,0,0,0.3); transition: all 0.3s ease; display: flex; justify-content: center; align-items: center; font-size: 18px; font-weight: bold; opacity: 0;">
                                    ◀
                                </button>
                                <button class="scroll-btn scroll-right" style="position: absolute; right: 5px; top: 50%; transform: translateY(-50%); background: linear-gradient(135deg, rgba(79, 172, 254, 0.8), rgba(0, 242, 254, 0.8)); color: white; border: none; border-radius: 50%; width: 32px; height: 32px; cursor: pointer; z-index: 10; box-shadow: 0 2px 8px rgba(0,0,0,0.3); transition: all 0.3s ease; display: flex; justify-content: center; align-items: center; font-size: 18px; font-weight: bold; opacity: 0;">
                                    ▶
                                </button>
                                <!-- 图片容器 -->
                                <div class="preview-scroll-container" style="display: flex; overflow: hidden; height: 150px;">
                                    <div class="output-preview-images" style="display: flex; transition: transform 0.3s ease;"></div>
                                </div>
                            </div>
                        </div>

                <!-- 尺寸调整 -->
                <div style="margin-top: 15px;">
                    <h4 style="margin-bottom: 10px; color: #666;">尺寸调整</h4>
                    <div class="size-controls">
                        <div class="size-input-group">
                            <label>宽度 (px)</label>
                            <input type="number" class="width-input" min="1" step="1" disabled>
                        </div>
                        <div class="size-input-group">
                            <label>高度 (px)</label>
                            <input type="number" class="height-input" min="1" step="1" disabled>
                        </div>
                        <div class="aspect-lock" style="display: flex; align-items: center; gap: 8px;">
                            <input type="checkbox" class="lock-aspect" checked style="width: 18px; height: 18px; margin: 0; cursor: pointer;">
                            <span>锁定比例</span>
                        </div>
                    </div>
                </div>

                <!-- 数组名前缀 -->
                <div style="margin-top: 15px;">
                    <h4 style="margin-bottom: 10px; color: #666;">数组名前缀</h4>
                    <div class="filename-input-group">
                        <input type="text" class="array-prefix-input" placeholder="请输入数组名前缀">
                    </div>
                </div>

                <!-- 输出详情 -->
                <div style="margin-top: 15px;">
                    <h4 style="margin-bottom: 10px; color: #666;">输出详情</h4>
                    <div style="background: #f0f0f0; padding: 15px; border-radius: 8px; font-size: 0.9em;">
                        <div style="display: flex; justify-content: space-between; margin-bottom: 8px;">
                            <span style="color: #666;">原图数据大小：</span>
                            <span class="original-size" style="font-weight: bold;">0 B</span>
                        </div>
                        <div style="display: flex; justify-content: space-between; margin-bottom: 8px;">
                            <span style="color: #666;">输出图片数据大小：</span>
                            <span class="output-size" style="font-weight: bold;">0 B</span>
                        </div>
                        <div style="display: flex; justify-content: space-between;">
                            <span style="color: #666;">压缩率：</span>
                            <span class="compression-ratio" style="font-weight: bold;">0%</span>
                        </div>
                    </div>
                    <div style="display: flex; align-items: center; gap: 10px; margin-top: 15px;">
                        <input type="checkbox" class="combine-as-array" checked style="width: 18px; height: 18px; margin: 0; cursor: pointer;">
                        <span>组合为数组</span>
                    </div>
                </div>

                <!-- 卡片状态 -->
                <div class="card-status" style="margin-top: 10px; font-size: 0.8em; color: #999; text-align: right;"></div>
            `;

            // 添加到容器
            cardsContainer.appendChild(newCard);

            // 创建卡片数据对象
            const newCardData = new ImageCard(newCardIndex);
            cards.push(newCardData);

            // 初始化卡片事件
            initCard(newCardIndex);

            // 设置默认数组名前缀，确保唯一
            const defaultPrefix = generateUniquePrefix(newCardIndex);
            updateArrayPrefix(newCardIndex, defaultPrefix);

            // 更新删除按钮状态
            updateDeleteButtons();

            // 更新卡片数量显示
            updateCardCountDisplay();
        }

        // 删除卡片
        function deleteCard(cardIndex) {
            const cardsContainer = document.getElementById('cardsContainer');
            const cardCount = cardsContainer.children.length;

            // 不能删除最后一张卡片
            if (cardCount <= 1) {
                alert('不能删除最后一张卡片！');
                return;
            }

            // 移除卡片元素
            const cardToDelete = document.querySelector(`[data-card-index="${cardIndex}"]`);
            cardsContainer.removeChild(cardToDelete);

            // 移除卡片数据
            cards.splice(cardIndex, 1);

            // 更新剩余卡片的索引和显示
            updateCardIndices();

            // 更新删除按钮状态
            updateDeleteButtons();

            // 检查是否可以转换
            checkConvertButtonState();

            // 更新卡片数量显示
            updateCardCountDisplay();
        }

        // 更新卡片数量显示
        function updateCardCountDisplay() {
            const cardCount = cards.length;
            const cardCountElement = document.getElementById('cardCount');
            cardCountElement.textContent = `(${cardCount}个图片选项卡)`;
        }

        // 更新已添加图片数量显示
        function updateImageCountDisplay(cardIndex) {
            const card = cards[cardIndex];
            const cardElement = document.querySelector(`[data-card-index="${cardIndex}"]`);
            const countElement = cardElement.querySelector('.image-count');
            if (countElement) {
                countElement.textContent = card.images.length;
            }
        }

        // 更新卡片索引
        function updateCardIndices() {
            const cardsContainer = document.getElementById('cardsContainer');
            const cardElements = cardsContainer.children;

            for (let i = 0; i < cardElements.length; i++) {
                const cardElement = cardElements[i];
                const cardData = cards[i];

                // 更新元素索引
                cardElement.setAttribute('data-card-index', i);

                // 更新标题
                const title = cardElement.querySelector('h3');
                title.textContent = `图片 ${i + 1}`;

                // 更新卡片数据索引
                cardData.index = i;

                // 检查并更新数组名前缀，确保唯一性
                const prefix = cardData.arrayPrefix;
                const expectedPrefix = `pic${i + 1}`;

                // 只有当前缀是默认格式（picX）且与当前索引不匹配时，才需要更新
                if (prefix === `pic${i + 2}` || (prefix.startsWith('pic') && !isNaN(prefix.slice(3)) && parseInt(prefix.slice(3)) !== i + 1)) {
                    // 检查是否与其他前缀冲突
                    if (checkPrefixConflict(expectedPrefix, i)) {
                        // 如果冲突，生成唯一前缀
                        const newPrefix = generateUniquePrefix(i);
                        updateArrayPrefix(i, newPrefix);
                    } else {
                        // 如果不冲突，使用预期前缀
                        updateArrayPrefix(i, expectedPrefix);
                    }
                }
            }

            // 更新卡片数量显示
            updateCardCountDisplay();
        }

        // 更新删除按钮状态
        function updateDeleteButtons() {
            const cardsContainer = document.getElementById('cardsContainer');
            const cardCount = cardsContainer.children.length;
            const deleteButtons = cardsContainer.querySelectorAll('.delete-card-btn');

            deleteButtons.forEach((btn, index) => {
                btn.disabled = (cardCount <= 1);
                if (cardCount <= 1) {
                    btn.style.opacity = '0.5';
                    btn.style.cursor = 'not-allowed';
                } else {
                    btn.style.opacity = '1';
                    btn.style.cursor = 'pointer';
                }
            });
        }

        // 处理图片选择
        // 批量处理图片选择
        function batchHandleImageSelect(cardIndex, files) {
            if (!files || files.length === 0) return;

            const card = cards[cardIndex];
            const maxImages = 1024;
            const originalImageCount = card.images.length;

            // 过滤掉已存在的图片
            const newFiles = files.filter(file => {
                // 检查图片是否已存在（通过文件名和大小判断）
                const existingImage = card.images.find(image =>
                    image.file &&
                    image.file.name === file.name &&
                    image.file.size === file.size
                );
                return !existingImage;
            });

            if (newFiles.length === 0) {
                return; // 没有新图片需要添加
            }

            // 创建处理队列
            const processPromises = [];

            // 第一张图片用于确定尺寸
            let referenceWidth = card.originalWidth;
            let referenceHeight = card.originalHeight;
            let hasReferenceSize = card.images.length > 0;

            // 批量读取图片数据
            for (const file of newFiles) {
                const processPromise = new Promise((resolve, reject) => {
                    // 预览图片
                    const reader = new FileReader();
                    reader.onload = function(e) {
                        const previewUrl = e.target.result;

                        // 创建临时图片对象获取尺寸
                        const tempImg = new Image();
                        tempImg.onload = function() {
                            const imgWidth = tempImg.naturalWidth;
                            const imgHeight = tempImg.naturalHeight;

                            // 验证尺寸一致性
                            if (hasReferenceSize) {
                                if (imgWidth !== referenceWidth || imgHeight !== referenceHeight) {
                                    reject(new Error('不允许添加不同尺寸图片到图片组'));
                                    return;
                                }
                            } else {
                                // 第一张图片，设置参考尺寸
                                referenceWidth = imgWidth;
                                referenceHeight = imgHeight;
                                hasReferenceSize = true;
                            }

                            // 返回处理好的图片数据
                            resolve({
                                file: file,
                                previewUrl: previewUrl,
                                width: imgWidth,
                                height: imgHeight
                            });
                        };
                        tempImg.onerror = () => reject(new Error('图片加载失败'));
                        tempImg.src = previewUrl;
                    };
                    reader.onerror = () => reject(new Error('文件读取失败'));
                    reader.readAsDataURL(file);
                });

                processPromises.push(processPromise);
            }

            // 执行批量处理
            Promise.all(processPromises)
                .then(processedImages => {
                    // 批量添加图片到卡片
                    for (const processedImage of processedImages) {
                        // 创建新的图片项
                        const imageItem = new ImageItem();
                        imageItem.file = processedImage.file;
                        imageItem.previewUrl = processedImage.previewUrl;
                        imageItem.isValid = true;

                        // 添加到卡片的图片数组
                        card.images.push(imageItem);
                    }

                    // 更新卡片状态
                    card.isValid = card.images.length > 0;

                    // 初始化卡片尺寸（如果是首次添加图片）
                    if (card.images.length === processedImages.length) {
                        card.originalWidth = referenceWidth;
                        card.originalHeight = referenceHeight;
                        card.aspectRatio = referenceWidth / referenceHeight;
                        card.width = referenceWidth;
                        card.height = referenceHeight;

                        // 更新UI尺寸输入框
                        const cardElement = document.querySelector(`[data-card-index="${cardIndex}"]`);
                        if (cardElement) {
                            const widthInput = cardElement.querySelector('.width-input');
                            const heightInput = cardElement.querySelector('.height-input');
                            widthInput.value = card.width;
                            heightInput.value = card.height;
                            widthInput.disabled = false;
                            heightInput.disabled = false;
                        }
                    }

                    // 批量更新UI，只更新一次
                    const cardElement = document.querySelector(`[data-card-index="${cardIndex}"]`);
                    if (cardElement) {
                        // 更新已添加图片数量显示
                        updateImageCountDisplay(cardIndex);

                        // 恢复预览窗口大小
                        adjustPreviewHeight(cardIndex, true);

                        // 更新原图预览
                        updateOriginalPreviews(cardIndex);

                        // 更新输出预览
                        updateOutputPreview(cardIndex);

                        // 更新卡片状态
                        updateCardStatus(cardIndex, `✅ 已添加 ${card.images.length} 张图片`);

                        // 更新输出详情
                        updateOutputDetails(cardIndex);

                        // 检查是否可以转换
                        checkConvertButtonState();
                    }
                })
                .catch(error => {
                    alert(error.message);
                });
        }

        function handleImageSelect(cardIndex, file) {
            // 调用批量处理函数，传入包含单个文件的数组
            batchHandleImageSelect(cardIndex, [file]);
        }

        // 处理宽度变化
        function handleWidthChange(cardIndex, newWidth) {
            const card = cards[cardIndex];
            const cardElement = document.querySelector(`[data-card-index="${cardIndex}"]`);
            const lockAspect = cardElement.querySelector('.lock-aspect').checked;

            // 限制最小宽度
            newWidth = Math.max(1, Math.min(newWidth, card.originalWidth));
            card.width = newWidth;

            // 如果锁定比例，更新高度
            if (lockAspect) {
                const newHeight = Math.round(newWidth / card.aspectRatio);
                card.height = Math.max(1, Math.min(newHeight, card.originalHeight));

                // 更新高度输入框
                const heightInput = cardElement.querySelector('.height-input');
                heightInput.value = card.height;
            }

            // 更新宽度输入框
            const widthInput = cardElement.querySelector('.width-input');
            widthInput.value = newWidth;

            // 更新输出预览和输出详情
            updateOutputPreview(cardIndex);
            updateOutputDetails(cardIndex);
        }

        // 处理高度变化
        function handleHeightChange(cardIndex, newHeight) {
            const card = cards[cardIndex];
            const cardElement = document.querySelector(`[data-card-index="${cardIndex}"]`);
            const lockAspect = cardElement.querySelector('.lock-aspect').checked;

            // 限制最小高度
            newHeight = Math.max(1, Math.min(newHeight, card.originalHeight));
            card.height = newHeight;

            // 如果锁定比例，更新宽度
            if (lockAspect) {
                const newWidth = Math.round(newHeight * card.aspectRatio);
                card.width = Math.max(1, Math.min(newWidth, card.originalWidth));

                // 更新宽度输入框
                const widthInput = cardElement.querySelector('.width-input');
                widthInput.value = card.width;
            }

            // 更新高度输入框
            const heightInput = cardElement.querySelector('.height-input');
            heightInput.value = newHeight;

            // 更新输出预览和输出详情
            updateOutputPreview(cardIndex);
            updateOutputDetails(cardIndex);
        }

        // 处理锁定比例变化
        function handleAspectLockChange(cardIndex, isLocked) {
            const card = cards[cardIndex];
            if (isLocked) {
                // 重新计算尺寸，保持比例
                const newHeight = Math.round(card.width / card.aspectRatio);
                card.height = Math.max(1, Math.min(newHeight, card.originalHeight));

                const cardElement = document.querySelector(`[data-card-index="${cardIndex}"]`);
                const heightInput = cardElement.querySelector('.height-input');
                heightInput.value = card.height;
            }
        }

        // 检查前缀是否冲突
        function checkPrefixConflict(prefix, excludeIndex = -1) {
            for (let i = 0; i < cards.length; i++) {
                if (i === excludeIndex) continue;
                if (cards[i].arrayPrefix === prefix) {
                    return true;
                }
            }
            return false;
        }

        // 生成唯一前缀
        function generateUniquePrefix(cardIndex) {
            let prefix = `pic${cardIndex + 1}`;
            let counter = 1;

            // 如果前缀已存在，尝试使用递增数字生成新前缀
            while (checkPrefixConflict(prefix)) {
                prefix = `pic${cardIndex + 1}_${counter}`;
                counter++;
            }

            return prefix;
        }

        // 处理数组名前缀变化
        function handleArrayPrefixChange(cardIndex, value) {
            // 验证和调整数组名前缀
            let prefix = value;

            // 移除所有非字母数字和下划线的字符
            prefix = prefix.replace(/[^a-zA-Z0-9_]/g, '');

            // 如果以数字开头，添加下划线
            if (/^\d/.test(prefix)) {
                prefix = '_' + prefix;
            }

            // 如果为空，设置默认值
            if (prefix === '') {
                prefix = generateUniquePrefix(cardIndex);
            } else {
                // 检查前缀是否与其他卡片冲突
                if (checkPrefixConflict(prefix, cardIndex)) {
                    // 如果冲突，使用生成的唯一前缀
                    prefix = generateUniquePrefix(cardIndex);
                }
            }

            // 更新数组名前缀
            updateArrayPrefix(cardIndex, prefix);
        }

        // 更新数组名前缀
        function updateArrayPrefix(cardIndex, prefix) {
            const card = cards[cardIndex];
            card.arrayPrefix = prefix;

            // 更新输入框
            const cardElement = document.querySelector(`[data-card-index="${cardIndex}"]`);
            const arrayPrefixInput = cardElement.querySelector('.array-prefix-input');
            arrayPrefixInput.value = prefix;
        }

        // 更新卡片状态
        function updateCardStatus(cardIndex, status) {
            const cardElement = document.querySelector(`[data-card-index="${cardIndex}"]`);
            const statusElement = cardElement.querySelector('.card-status');
            statusElement.textContent = status;
        }

        // 检查数组名前缀是否唯一
        function checkArrayPrefixUnique() {
            const prefixes = new Set();
            for (const card of cards) {
                if (prefixes.has(card.arrayPrefix)) {
                    return false;
                }
                prefixes.add(card.arrayPrefix);
            }
            return true;
        }

        // 检查是否可以转换
        function checkConvertButtonState() {
            const convertBtn = document.getElementById('convertBtn');

            // 检查是否所有卡片都有有效图片
            const allValid = cards.every(card => card.isValid);

            convertBtn.disabled = !allValid;
        }

        // 并发控制函数 - 限制同时处理的任务数量
        async function concurrencyControl(tasks, concurrencyLimit) {
            const results = [];
            const executing = new Set();

            async function executeNext() {
                if (tasks.length === 0) return;

                const task = tasks.shift();
                const promise = task();

                executing.add(promise);

                try {
                    const result = await promise;
                    results.push(result);
                } catch (error) {
                    throw error;
                } finally {
                    executing.delete(promise);
                    await executeNext();
                }
            }

            // 启动初始并发任务
            const initialTasks = Math.min(concurrencyLimit, tasks.length);
            const promises = Array.from({ length: initialTasks }, executeNext);

            await Promise.all(promises);
            return results;
        }

        // 进度条控制函数
        function updateProgress(progress, text) {
            const progressFill = document.getElementById('progressFill');
            const progressText = document.getElementById('progressText');
            const progressPercent = document.getElementById('progressPercent');

            // 确保进度不超过100%
            const percentage = Math.max(0, Math.min(100, Math.round(progress)));
            progressFill.style.width = `${percentage}%`;
            progressText.textContent = text;
            progressPercent.textContent = `${percentage}%`;
        }

        // 重置进度条
        function resetProgress() {
            updateProgress(0, '准备转换...');
        }

        // 设备性能检测 - 自动调整并发数
        function getOptimalConcurrency() {
            try {
                // 获取CPU核心数
                const cpuCores = navigator.hardwareConcurrency || 4;

                // 获取可用内存（近似值）
                const memory = navigator.deviceMemory || 4;

                // 根据CPU核心数和内存调整并发数
                let concurrency = Math.min(cpuCores * 2, 16); // 最多16个并发

                // 内存不足时降低并发数
                if (memory < 2) {
                    concurrency = Math.min(cpuCores, 4); // 内存小于2GB时最多4个并发
                } else if (memory < 4) {
                    concurrency = Math.min(cpuCores * 1.5, 8); // 内存小于4GB时最多8个并发
                }

                return concurrency;
            } catch (error) {
                // 性能检测失败时使用保守值
                return 4;
            }
        }

        // 单张图片处理 - 用于生成C文件
        async function processImageForC(imageItem, card, imgIndex, format, useRle) {
            // 创建canvas进行图片处理
            const canvas = document.createElement('canvas');
            const ctx = canvas.getContext('2d');
            canvas.width = card.width;
            canvas.height = card.height;

            // 绘制图片
            const img = new Image();
            await new Promise((resolve) => {
                img.onload = resolve;
                img.src = imageItem.previewUrl;
            });

            // 检查是否启用透明填充
            const useTransparentFill = document.getElementById('transparentFill').checked;
            let fillR = 255, fillG = 255, fillB = 255;

            if (useTransparentFill) {
                // 获取填充颜色
                const fillColor = document.getElementById('fillColor').value.trim().toUpperCase();
                if (/^[0-9A-F]{6}$/.test(fillColor)) {
                    // 解析RGB值
                    fillR = parseInt(fillColor.substring(0, 2), 16);
                    fillG = parseInt(fillColor.substring(2, 4), 16);
                    fillB = parseInt(fillColor.substring(4, 6), 16);
                }
            }

            // 创建临时canvas处理透明度
            const tempCanvas = document.createElement('canvas');
            tempCanvas.width = card.width;
            tempCanvas.height = card.height;
            const tempCtx = tempCanvas.getContext('2d');

            // 如果启用透明填充，先绘制填充颜色，再绘制图片
            if (useTransparentFill) {
                // 绘制填充颜色
                tempCtx.fillStyle = `rgb(${fillR}, ${fillG}, ${fillB})`;
                tempCtx.fillRect(0, 0, card.width, card.height);
                // 绘制图片（会与背景色混合透明像素）
                tempCtx.drawImage(img, 0, 0, card.width, card.height);
            } else {
                // 直接绘制图片
                tempCtx.drawImage(img, 0, 0, card.width, card.height);
            }

            // 获取图片数据
            let imageData = tempCtx.getImageData(0, 0, card.width, card.height);
            // 应用颜色深度过滤
            imageData = processImageData(imageData, format);
            const data = imageData.data;

            // 生成像素数据数组
            const pixelBytes = [];

            // 逐行处理像素数据
            for (let y = 0; y < card.height; y++) {
                for (let x = 0; x < card.width; x++) {
                    const index = (y * card.width + x) * 4;
                    const r = data[index];
                    const g = data[index + 1];
                    const b = data[index + 2];

                    if (format === 'rgb888') {
                        // 检查RGB888反字序设置
                        const isReverseOrder = document.getElementById('rgb888ReverseOrder').checked;
                        if (isReverseOrder) {
                            // BGR顺序
                            pixelBytes.push(b);
                            pixelBytes.push(g);
                            pixelBytes.push(r);
                        } else {
                            // RGB顺序
                            pixelBytes.push(r);
                            pixelBytes.push(g);
                            pixelBytes.push(b);
                        }
                    } else if (format === 'rgb565') {
                        // RGB565格式：2字节
                        const r5 = (r >> 3) & 0x1F;
                        const g6 = (g >> 2) & 0x3F;
                        const b5 = (b >> 3) & 0x1F;
                        const value = (r5 << 11) | (g6 << 5) | b5;
                        const lowByte = value & 0xFF;
                        const highByte = (value >> 8) & 0xFF;

                        // 检查字节顺序设置
                        const isLittleEndian = document.getElementById('rgb565LittleEndian').checked;
                        if (isLittleEndian) {
                            // 低字节在前，高字节在后（小端序）
                            pixelBytes.push(lowByte);
                            pixelBytes.push(highByte);
                        } else {
                            // 高字节在前，低字节在后（大端序）
                            pixelBytes.push(highByte);
                            pixelBytes.push(lowByte);
                        }
                    } else if (format === 'rgb332') {
                        // RGB332格式：1字节
                        const r3 = (r >> 5) & 0x07;
                        const g3 = (g >> 5) & 0x07;
                        const b2 = (b >> 6) & 0x03;
                        const value = (r3 << 5) | (g3 << 2) | b2;
                        pixelBytes.push(value);
                    }
                }
            }

            // 应用RLE压缩
            let finalBytes = pixelBytes;
            if (useRle) {
                finalBytes = rleCompress(pixelBytes, format);
            }

            return { finalBytes, pixelBytes, format };
        }

        // 单张图片处理 - 用于生成BIN文件
        async function processImageForBin(imageItem, card, imgIndex, format, useRle) {
            // 绘制图片
            const img = new Image();
            await new Promise((resolve) => {
                img.onload = resolve;
                img.src = imageItem.previewUrl;
            });

            // 检查是否启用透明填充
            const useTransparentFill = document.getElementById('transparentFill').checked;
            let fillR = 255, fillG = 255, fillB = 255;

            if (useTransparentFill) {
                // 获取填充颜色
                const fillColor = document.getElementById('fillColor').value.trim().toUpperCase();
                if (/^[0-9A-F]{6}$/.test(fillColor)) {
                    // 解析RGB值
                    fillR = parseInt(fillColor.substring(0, 2), 16);
                    fillG = parseInt(fillColor.substring(2, 4), 16);
                    fillB = parseInt(fillColor.substring(4, 6), 16);
                }
            }

            // 创建临时canvas处理透明度
            const tempCanvas = document.createElement('canvas');
            tempCanvas.width = card.width;
            tempCanvas.height = card.height;
            const tempCtx = tempCanvas.getContext('2d');

            // 如果启用透明填充，先绘制填充颜色，再绘制图片
            if (useTransparentFill) {
                // 绘制填充颜色
                tempCtx.fillStyle = `rgb(${fillR}, ${fillG}, ${fillB})`;
                tempCtx.fillRect(0, 0, card.width, card.height);
                // 绘制图片（会与背景色混合透明像素）
                tempCtx.drawImage(img, 0, 0, card.width, card.height);
            } else {
                // 直接绘制图片
                tempCtx.drawImage(img, 0, 0, card.width, card.height);
            }

            // 获取图片数据
            let imageData = tempCtx.getImageData(0, 0, card.width, card.height);
            // 应用颜色深度过滤
            imageData = processImageData(imageData, format);
            const data = imageData.data;

            // 计算当前图片的字节数
            let pixelCount = card.width * card.height;
            let bytesPerPixel = 3;
            if (format === 'rgb565') {
                bytesPerPixel = 2;
            } else if (format === 'rgb332') {
                bytesPerPixel = 1;
            }

            // 直接计算数据，避免使用push方法
            let imageBytes = new Uint8Array(pixelCount * bytesPerPixel);
            let byteIndex = 0;

            // 逐行处理像素数据
            for (let y = 0; y < card.height; y++) {
                for (let x = 0; x < card.width; x++) {
                    const index = (y * card.width + x) * 4;
                    const r = data[index];
                    const g = data[index + 1];
                    const b = data[index + 2];

                    if (format === 'rgb888') {
                        // 检查RGB888反字序设置
                        const isReverseOrder = document.getElementById('rgb888ReverseOrder').checked;
                        if (isReverseOrder) {
                            // BGR顺序
                            imageBytes[byteIndex++] = b;
                            imageBytes[byteIndex++] = g;
                            imageBytes[byteIndex++] = r;
                        } else {
                            // RGB顺序
                            imageBytes[byteIndex++] = r;
                            imageBytes[byteIndex++] = g;
                            imageBytes[byteIndex++] = b;
                        }
                    } else if (format === 'rgb565') {
                        // RGB565格式：2字节
                        const r5 = (r >> 3) & 0x1F;
                        const g6 = (g >> 2) & 0x3F;
                        const b5 = (b >> 3) & 0x1F;
                        const value = (r5 << 11) | (g6 << 5) | b5;
                        const lowByte = value & 0xFF;
                        const highByte = (value >> 8) & 0xFF;

                        // 检查字节顺序设置
                        const isLittleEndian = document.getElementById('rgb565LittleEndian').checked;
                        if (isLittleEndian) {
                            // 低字节在前，高字节在后（小端序）
                            imageBytes[byteIndex++] = lowByte;
                            imageBytes[byteIndex++] = highByte;
                        } else {
                            // 高字节在前，低字节在后（大端序）
                            imageBytes[byteIndex++] = highByte;
                            imageBytes[byteIndex++] = lowByte;
                        }
                    } else if (format === 'rgb332') {
                        // RGB332格式：1字节
                        const r3 = (r >> 5) & 0x07;
                        const g3 = (g >> 5) & 0x07;
                        const b2 = (b >> 6) & 0x03;
                        const value = (r3 << 5) | (g3 << 2) | b2;
                        imageBytes[byteIndex++] = value;
                    }
                }
            }

            // 应用RLE压缩
            let finalBytes = Array.from(imageBytes);
            if (useRle) {
                finalBytes = rleCompress(finalBytes, format);
            }

            return { finalBytes, imageBytes, format };
        }

        // 转换所有图片
        async function convertAllImages() {
            // 获取全局设置
            const colorFormat = document.getElementById('colorFormat').value;
            const outputFormat = document.getElementById('outputFormat').value;
            const filename = document.getElementById('filename').value;

            // 检查文件名是否为空
            if (!filename) {
                alert('错误：文件名不能为空！请输入有效的文件名。');
                return;
            }

            // 检查是否所有卡片都选择了图片
            for (const card of cards) {
                if (!card.isValid) {
                    alert(`错误：图片 ${card.index + 1} 没有选择图片！`);
                    return;
                }
            }

            // 检查数组名前缀是否唯一
            if (!checkArrayPrefixUnique()) {
                alert('错误：数组名前缀必须唯一！请修改重复的数组名前缀。');
                return;
            }

            // 重置并显示进度条
            resetProgress();

            // 禁用转换按钮
            const convertBtn = document.getElementById('convertBtn');
            convertBtn.disabled = true;

            try {
                if (outputFormat === '.c') {
                    await generateCFileForAllImages(filename, colorFormat);
                } else {
                    // 生成bin文件和对应的.c文件
                    await generateBinFiles(filename, colorFormat);
                }

                // 转换完成
                updateProgress(100, '转换完成！');
            } catch (error) {
                // 转换失败
                updateProgress(0, '转换失败：' + error.message);
                alert('转换失败：' + error.message);
            } finally {
                // 恢复转换按钮状态
                convertBtn.disabled = false;
            }
        }

        // 生成bin文件和对应的.c文件
        async function generateBinFiles(filename, format) {
            // 生成bin文件并获取图片数据信息
            const imageInfo = await generateBinFileForAllImages(filename, format);

            // 生成对应的.c文件
            generateBinCFile(filename, format, imageInfo);
        }

        // 生成所有图片的C文件
        async function generateCFileForAllImages(filename, format) {
            let content = `#include <stdint.h>\n`;
            content += `#include <sgl_core.h>\n\n`;
            content += `// ${filename} - Generated by Image To Array Tool\n\n`;

            // 存储所有sgl_pixmap_t结构体定义
            let pixmapStructures = '';
            // 存储需要组合为数组的结构体信息
            const structArrays = [];
            // 存储卡片的“组合为数组”设置
            const cardCombineSettings = [];

            // 收集所有需要处理的图片任务
            const imageTasks = [];
            const totalImages = cards.reduce((sum, card) => sum + card.images.length, 0);
            let processedImages = 0;

            // 收集任务和卡片设置
            for (let cardIndex = 0; cardIndex < cards.length; cardIndex++) {
                const card = cards[cardIndex];
                const cardElement = document.querySelector(`[data-card-index="${cardIndex}"]`);
                // 获取“组合为数组”单选框状态，默认选中
                const combineAsArray = cardElement.querySelector('.combine-as-array')?.checked ?? true;
                cardCombineSettings[cardIndex] = combineAsArray;

                // 添加当前卡片的所有图片处理任务
                for (let imgIndex = 0; imgIndex < card.images.length; imgIndex++) {
                    const imageItem = card.images[imgIndex];
                    // 创建图片处理任务
                    imageTasks.push(async () => {
                        return await processImageForC(card, imageItem, imgIndex, cardIndex, format);
                    });
                }
            }

            // 定义进度更新回调
            const updateProgressCallback = () => {
                processedImages++;
                const progress = Math.min(90, (processedImages / totalImages) * 90); // 90%用于图片处理，留10%给文件生成
                updateProgress(progress, `正在处理图片 ${processedImages}/${totalImages}...`);
            };

            // 获取最佳并发数
            const optimalConcurrency = getOptimalConcurrency();
            // 执行并发任务
            const results = await concurrencyControl(imageTasks, optimalConcurrency, updateProgressCallback);

            // 处理结果，按顺序生成内容
            // 首先按卡片和图片索引排序结果，确保生成的顺序正确
            results.sort((a, b) => {
                if (a.cardIndex !== b.cardIndex) {
                    return a.cardIndex - b.cardIndex;
                }
                return a.imgIndex - b.imgIndex;
            });

            // 遍历处理结果
            let currentCardIndex = -1;
            const cardStructs = {};

            for (const result of results) {
                const { cardIndex, imgIndex } = result;

                // 初始化当前卡片的结构体数组
                if (currentCardIndex !== cardIndex) {
                    currentCardIndex = cardIndex;
                    cardStructs[currentCardIndex] = [];
                }

                // 添加数组定义
                content += `// ${result.arrayPrefix} - ${result.width}x${result.height} ${format.toUpperCase()}${result.useRle ? ' (RLE压缩)' : ''}\n`;
                content += `static const uint8_t ${result.arrayPrefix}_data[${result.arraySize}] = {\n    ${result.pixelData}\n};\n\n`;

                // 生成结构体名称
                const structName = `${result.arrayPrefix}_pixmap`;

                // 存储结构体信息
                cardStructs[currentCardIndex].push({
                    name: structName,
                    arrayPrefix: result.arrayPrefix,
                    formatValue: result.formatValue,
                    width: result.width,
                    height: result.height,
                    imgIndex: result.imgIndex
                });
            }

            // 处理结构体生成逻辑
            for (let cardIndex = 0; cardIndex < cards.length; cardIndex++) {
                const combineAsArray = cardCombineSettings[cardIndex];
                const structs = cardStructs[cardIndex] || [];
                const card = cards[cardIndex];

                if (combineAsArray) {
                    // 勾选了"组合为数组"
                    if (structs.length >= 2) {
                        // 图片数量>=2，生成结构体数组
                        structArrays.push({
                            card: card,
                            structs: structs
                        });
                    } else {
                        // 图片数量=1，生成单个结构体
                        const struct = structs[0];
                        if (struct) {
                            pixmapStructures += `// 选项卡 ${cardIndex + 1} 图片 ${struct.imgIndex + 1} 的sgl_pixmap_t结构体\n`;
                            pixmapStructures += `const sgl_pixmap_t ${struct.name} = {\n`;
                            pixmapStructures += `    .width = ${struct.width},\n`;
                            pixmapStructures += `    .height = ${struct.height},\n`;
                            pixmapStructures += `    .bitmap = ${struct.arrayPrefix}_data,\n`;
                            pixmapStructures += `    .format = ${struct.formatValue},\n`;
                            pixmapStructures += `};\n\n`;
                        }
                    }
                } else {
                    // 取消勾选"组合为数组"，生成单个结构体
                    for (const struct of structs) {
                        pixmapStructures += `// 选项卡 ${cardIndex + 1} 图片 ${struct.imgIndex + 1} 的sgl_pixmap_t结构体\n`;
                        pixmapStructures += `const sgl_pixmap_t ${struct.name} = {\n`;
                        pixmapStructures += `    .width = ${struct.width},\n`;
                        pixmapStructures += `    .height = ${struct.height},\n`;
                        pixmapStructures += `    .bitmap = ${struct.arrayPrefix}_data,\n`;
                        pixmapStructures += `    .format = ${struct.formatValue},\n`;
                        pixmapStructures += `};\n\n`;
                    }
                }
            }

            // 将所有单独的sgl_pixmap_t结构体定义添加到文件
            if (pixmapStructures) {
                content += `// 所有图片的sgl_pixmap_t结构体定义\n`;
                content += pixmapStructures;
            }

            // 生成结构体数组定义
            for (const structArray of structArrays) {
                const card = structArray.card;
                const structs = structArray.structs;

                // 生成数组名称
                const arrayName = `${card.arrayPrefix}_array`;

                // 添加结构体数组定义
                content += `// ${card.arrayPrefix} 结构体数组 - ${structs.length}张图片\n`;
                content += `const sgl_pixmap_t ${arrayName}[${structs.length}] = {\n`;

                for (let i = 0; i < structs.length; i++) {
                    const struct = structs[i];
                    content += `    {\n`;
                    content += `        .width = ${struct.width},\n`;
                    content += `        .height = ${struct.height},\n`;
                    content += `        .bitmap = ${struct.arrayPrefix}_data,\n`;
                    content += `        .format = ${struct.formatValue}\n`;
                    content += `    }${i < structs.length - 1 ? ',' : ''}\n`;
                }

                content += `};\n\n`;
            }

            updateProgress(90, '正在生成文件...');

            // 下载文件
            downloadFile(`${filename}.c`, content);
        }

        // 生成所有图片的BIN文件
        async function generateBinFileForAllImages(filename, format) {
            // 先收集所有卡片的像素数据
            const allCardsData = [];

            // 存储每张图片的信息
            const imageInfo = [];

            // 计算总图片数量（所有选项卡的图片总和）
            const totalImages = cards.reduce((sum, card) => sum + card.images.length, 0);
            let processedImages = 0;

            // 收集所有需要处理的图片任务
            const imageTasks = [];

            // 收集任务
            for (let cardIndex = 0; cardIndex < cards.length; cardIndex++) {
                const card = cards[cardIndex];

                // 添加当前卡片的所有图片处理任务
                for (let imgIndex = 0; imgIndex < card.images.length; imgIndex++) {
                    const imageItem = card.images[imgIndex];
                    // 创建图片处理任务
                    imageTasks.push(async () => {
                        return await processImageForBin(card, imageItem, imgIndex, cardIndex, format);
                    });
                }
            }

            // 定义进度更新回调
            const updateProgressCallback = () => {
                processedImages++;
                const progress = Math.min(90, (processedImages / totalImages) * 90); // 90%用于图片处理，留10%给文件生成
                updateProgress(progress, `正在处理图片 ${processedImages}/${totalImages}...`);
            };

            // 获取最佳并发数
            const optimalConcurrency = getOptimalConcurrency();
            // 执行并发任务
            const results = await concurrencyControl(imageTasks, optimalConcurrency, updateProgressCallback);

            // 处理结果，按顺序生成内容
            // 首先按卡片和图片索引排序结果，确保生成的顺序正确
            results.sort((a, b) => {
                if (a.cardIndex !== b.cardIndex) {
                    return a.cardIndex - b.cardIndex;
                }
                return a.imgIndex - b.imgIndex;
            });

            // 遍历处理结果，收集数据
            for (const result of results) {
                // 记录当前图片的起始地址
                const startAddress = allCardsData.length;

                // 高效添加到总数据，避免使用扩展运算符
                for (let i = 0; i < result.finalBytes.length; i++) {
                    allCardsData.push(result.finalBytes[i]);
                }

                // 存储图片信息
                imageInfo.push({
                    card: result.card,
                    name: result.arrayPrefix,
                    startAddress: startAddress,
                    dataSize: result.finalBytes.length,
                    format: result.formatValue,
                    width: result.width,
                    height: result.height
                });
            }

            // 创建ArrayBuffer
            const arrayBuffer = new ArrayBuffer(allCardsData.length);
            const view = new DataView(arrayBuffer);

            // 将所有数据写入ArrayBuffer
            for (let i = 0; i < allCardsData.length; i++) {
                view.setUint8(i, allCardsData[i]);
            }

            updateProgress(90, '正在生成文件...');

            // 下载文件
            const blob = new Blob([arrayBuffer], { type: 'application/octet-stream' });
            downloadFile(`${filename}.bin`, blob);

            // 返回图片信息数组
            return imageInfo;
        }

        // 生成BIN格式对应的C文件
        function generateBinCFile(filename, format, imageInfo) {
            let content = `#include <stdint.h>
`;
            content += `#include <sgl_core.h>

`;
            content += `// ${filename} - Generated by Image To Array Tool

`;

            // 生成图片地址数组
            content += `// 图片在BIN文件中的起始地址数组
`;
            content += `static const uint32_t ${filename}_img_addresses[] = {
`;

            for (let i = 0; i < imageInfo.length; i++) {
                content += `    0x${imageInfo[i].startAddress.toString(16).padStart(8, '0')}`;
                if (i < imageInfo.length - 1) {
                    content += `,`;
                }
                content += ` // ${imageInfo[i].name}
`;
            }

            content += `};

`;

            // 生成sgl_pixmap_t结构体
            content += `// 图片数据结构体定义
`;

            // 按卡片分组图片信息
            const cardGroups = {};
            imageInfo.forEach(info => {
                if (!cardGroups[info.card.arrayPrefix]) {
                    cardGroups[info.card.arrayPrefix] = [];
                }
                cardGroups[info.card.arrayPrefix].push(info);
            });

            // 遍历每个卡片组
            for (const [prefix, infos] of Object.entries(cardGroups)) {
                const card = infos[0].card;
                const cardElement = document.querySelector(`[data-card-index="${card.index}"]`);
                // 获取“组合为数组”单选框状态，默认选中
                const combineAsArray = cardElement.querySelector('.combine-as-array')?.checked ?? true;

                if (combineAsArray && infos.length > 1) {
                    // 组合为数组
                    content += `// ${prefix} 结构体数组 - ${infos.length}张图片
`;
                    content += `const sgl_pixmap_t ${prefix}_array[${infos.length}] = {
`;

                    for (let i = 0; i < infos.length; i++) {
                        const info = infos[i];
                        content += `    {
`;
                        content += `        .width = ${info.width},
`;
                        content += `        .height = ${info.height},
`;
                        content += `        .bitmap = (const uint8_t*)&${filename}_img_addresses[${imageInfo.indexOf(info)}],
`;
                        content += `        .format = ${info.format}
`;
                        content += `    }${i < infos.length - 1 ? ',' : ''}
`;
                    }

                    content += `};

`;
                } else {
                    // 单独输出
                    for (const info of infos) {
                        content += `// ${info.name} - ${info.width}x${info.height} ${format.toUpperCase()}${info.format.includes('RLE') ? ' (RLE压缩)' : ''}
`;
                        content += `const sgl_pixmap_t ${info.name}_pixmap = {
`;
                        content += `    .width = ${info.width},
`;
                        content += `    .height = ${info.height},
`;
                        content += `    .bitmap = (const uint8_t*)&${filename}_img_addresses[${imageInfo.indexOf(info)}],
`;
                        content += `    .format = ${info.format},
`;
                        content += `};

`;
                    }
                }
            }

            // 下载文件
            downloadFile(`${filename}.c`, content);
        }

        // RLE压缩算法 - 按像素为单位压缩
        function rleCompress(data, colorFormat) {
            if (!data || data.length === 0) {
                return [];
            }

            // 根据颜色格式确定每个像素的字节数
            let bytesPerPixel = 3; // 默认RGB888
            if (colorFormat === 'rgb565') {
                bytesPerPixel = 2;
            } else if (colorFormat === 'rgb332') {
                bytesPerPixel = 1;
            }

            const compressed = [];
            const dataLength = data.length;

            // 确保数据长度是像素字节数的整数倍
            if (dataLength % bytesPerPixel !== 0) {
                return data; // 数据格式错误，返回原始数据
            }

            // 计算总像素数
            const pixelCount = dataLength / bytesPerPixel;
            if (pixelCount === 0) {
                return [];
            }

            // 遍历所有像素，直接比较原始数据，避免创建临时数组
            let count = 1;

            // 遍历所有像素
            for (let i = bytesPerPixel; i < dataLength; i += bytesPerPixel) {
                // 检查当前像素是否与前一个像素相同
                let isSamePixel = true;
                for (let j = 0; j < bytesPerPixel; j++) {
                    if (data[i + j] !== data[i - bytesPerPixel + j]) {
                        isSamePixel = false;
                        break;
                    }
                }

                if (isSamePixel && count < 255) {
                    // 相同像素且计数未达上限，继续计数
                    count++;
                } else {
                    // 遇到不同像素或计数上限，输出压缩单元
                    compressed.push(count); // 存储连续像素数量
                    // 存储像素数据，直接访问原始数据
                    for (let j = 0; j < bytesPerPixel; j++) {
                        compressed.push(data[i - bytesPerPixel + j]);
                    }

                    // 重置计数
                    count = 1;
                }
            }

            // 添加最后一组像素数据
            compressed.push(count);
            // 存储最后一组像素数据
            for (let j = 0; j < bytesPerPixel; j++) {
                compressed.push(data[dataLength - bytesPerPixel + j]);
            }

            return compressed;
        }

        // 单张图片处理函数 - 用于C文件生成
        async function processImageForC(card, imageItem, imgIndex, cardIndex, format) {
            // 创建canvas进行图片处理
            const canvas = document.createElement('canvas');
            const ctx = canvas.getContext('2d');
            canvas.width = card.width;
            canvas.height = card.height;

            // 绘制图片
            const img = new Image();
            await new Promise((resolve) => {
                img.onload = resolve;
                img.src = imageItem.previewUrl;
            });

            // 检查是否启用透明填充
            const useTransparentFill = document.getElementById('transparentFill').checked;
            let fillR = 255, fillG = 255, fillB = 255;

            if (useTransparentFill) {
                // 获取填充颜色
                const fillColor = document.getElementById('fillColor').value.trim().toUpperCase();
                if (/^[0-9A-F]{6}$/.test(fillColor)) {
                    // 解析RGB值
                    fillR = parseInt(fillColor.substring(0, 2), 16);
                    fillG = parseInt(fillColor.substring(2, 4), 16);
                    fillB = parseInt(fillColor.substring(4, 6), 16);
                }
            }

            // 创建临时canvas处理透明度
            const tempCanvas = document.createElement('canvas');
            tempCanvas.width = card.width;
            tempCanvas.height = card.height;
            const tempCtx = tempCanvas.getContext('2d');

            // 如果启用透明填充，先绘制填充颜色，再绘制图片
            if (useTransparentFill) {
                // 绘制填充颜色
                tempCtx.fillStyle = `rgb(${fillR}, ${fillG}, ${fillB})`;
                tempCtx.fillRect(0, 0, card.width, card.height);
                // 绘制图片（会与背景色混合透明像素）
                tempCtx.drawImage(img, 0, 0, card.width, card.height);
            } else {
                // 直接绘制图片
                tempCtx.drawImage(img, 0, 0, card.width, card.height);
            }

            // 获取图片数据
            let imageData = tempCtx.getImageData(0, 0, card.width, card.height);
            // 应用颜色深度过滤
            imageData = processImageData(imageData, format);
            const data = imageData.data;

            // 生成像素数据数组
            const pixelBytes = [];

            // 逐行处理像素数据
            for (let y = 0; y < card.height; y++) {
                for (let x = 0; x < card.width; x++) {
                    const index = (y * card.width + x) * 4;
                    const r = data[index];
                    const g = data[index + 1];
                    const b = data[index + 2];

                    if (format === 'rgb888') {
                        // 检查RGB888反字序设置
                        const isReverseOrder = document.getElementById('rgb888ReverseOrder').checked;
                        if (isReverseOrder) {
                            // BGR顺序
                            pixelBytes.push(b);
                            pixelBytes.push(g);
                            pixelBytes.push(r);
                        } else {
                            // RGB顺序
                            pixelBytes.push(r);
                            pixelBytes.push(g);
                            pixelBytes.push(b);
                        }
                    } else if (format === 'rgb565') {
                        // RGB565格式：2字节
                        const r5 = (r >> 3) & 0x1F;
                        const g6 = (g >> 2) & 0x3F;
                        const b5 = (b >> 3) & 0x1F;
                        const value = (r5 << 11) | (g6 << 5) | b5;
                        const lowByte = value & 0xFF;
                        const highByte = (value >> 8) & 0xFF;

                        // 检查字节顺序设置
                        const isLittleEndian = document.getElementById('rgb565LittleEndian').checked;
                        if (isLittleEndian) {
                            // 低字节在前，高字节在后（小端序）
                            pixelBytes.push(lowByte);
                            pixelBytes.push(highByte);
                        } else {
                            // 高字节在前，低字节在后（大端序）
                            pixelBytes.push(highByte);
                            pixelBytes.push(lowByte);
                        }
                    } else if (format === 'rgb332') {
                        // RGB332格式：1字节
                        const r3 = (r >> 5) & 0x07;
                        const g3 = (g >> 5) & 0x07;
                        const b2 = (b >> 6) & 0x03;
                        const value = (r3 << 5) | (g3 << 2) | b2;
                        pixelBytes.push(value);
                    }
                }
            }

            // 检查是否启用压缩
            const useRle = document.getElementById('compressionAlgorithm').value === 'rle';
            // 应用RLE压缩
            let finalBytes = pixelBytes;
            if (useRle) {
                finalBytes = rleCompress(pixelBytes, format);
            }

            // 将压缩后的数据转换为C数组格式
            let pixelData = '';
            let count = 0;

            for (let j = 0; j < finalBytes.length; j++) {
                const byte = finalBytes[j];
                pixelData += `0x${byte.toString(16).padStart(2, '0')}`;
                count++;

                if (count >= 24) {
                    pixelData += ',\n    ';
                    count = 0;
                } else if (j < finalBytes.length - 1) {
                    pixelData += ', ';
                }
            }

            // 计算数组大小
            const arraySize = finalBytes.length;

            // 生成数组名称，第一张图片直接使用前缀，后续图片添加_1,_2等
            const arrayPrefix = imgIndex === 0 ? card.arrayPrefix : `${card.arrayPrefix}_${imgIndex}`;

            // 确定format字段值
            let formatValue = 'SGL_PIXMAP_FMT_NONE';
            if (useRle) {
                if (format === 'rgb888') {
                    formatValue = 'SGL_PIXMAP_FMT_RLE_RGB888';
                } else if (format === 'rgb565') {
                    formatValue = 'SGL_PIXMAP_FMT_RLE_RGB565';
                } else if (format === 'rgb332') {
                    formatValue = 'SGL_PIXMAP_FMT_RLE_RGB332';
                }
            } else {
                if (format === 'rgb888') {
                    formatValue = 'SGL_PIXMAP_FMT_RGB888';
                } else if (format === 'rgb565') {
                    formatValue = 'SGL_PIXMAP_FMT_RGB565';
                } else if (format === 'rgb332') {
                    formatValue = 'SGL_PIXMAP_FMT_RGB332';
                }
            }

            // 返回处理结果
            return {
                arrayPrefix: arrayPrefix,
                pixelData: pixelData,
                arraySize: arraySize,
                formatValue: formatValue,
                imgIndex: imgIndex,
                cardIndex: cardIndex,
                width: card.width,
                height: card.height,
                useRle: useRle
            };
        }

        // 单张图片处理函数 - 用于BIN文件生成
        async function processImageForBin(card, imageItem, imgIndex, cardIndex, format) {
            // 创建canvas进行图片处理
            const canvas = document.createElement('canvas');
            const ctx = canvas.getContext('2d');
            canvas.width = card.width;
            canvas.height = card.height;

            // 绘制图片
            const img = new Image();
            await new Promise((resolve) => {
                img.onload = resolve;
                img.src = imageItem.previewUrl;
            });

            // 检查是否启用透明填充
            const useTransparentFill = document.getElementById('transparentFill').checked;
            let fillR = 255, fillG = 255, fillB = 255;

            if (useTransparentFill) {
                // 获取填充颜色
                const fillColor = document.getElementById('fillColor').value.trim().toUpperCase();
                if (/^[0-9A-F]{6}$/.test(fillColor)) {
                    // 解析RGB值
                    fillR = parseInt(fillColor.substring(0, 2), 16);
                    fillG = parseInt(fillColor.substring(2, 4), 16);
                    fillB = parseInt(fillColor.substring(4, 6), 16);
                }
            }

            // 创建临时canvas处理透明度
            const tempCanvas = document.createElement('canvas');
            tempCanvas.width = card.width;
            tempCanvas.height = card.height;
            const tempCtx = tempCanvas.getContext('2d');

            // 如果启用透明填充，先绘制填充颜色，再绘制图片
            if (useTransparentFill) {
                // 绘制填充颜色
                tempCtx.fillStyle = `rgb(${fillR}, ${fillG}, ${fillB})`;
                tempCtx.fillRect(0, 0, card.width, card.height);
                // 绘制图片（会与背景色混合透明像素）
                tempCtx.drawImage(img, 0, 0, card.width, card.height);
            } else {
                // 直接绘制图片
                tempCtx.drawImage(img, 0, 0, card.width, card.height);
            }

            // 获取图片数据
            let imageData = tempCtx.getImageData(0, 0, card.width, card.height);
            // 应用颜色深度过滤
            imageData = processImageData(imageData, format);
            const data = imageData.data;

            // 计算当前图片的字节数
            let pixelCount = card.width * card.height;
            let bytesPerPixel = 3;
            if (format === 'rgb565') {
                bytesPerPixel = 2;
            } else if (format === 'rgb332') {
                bytesPerPixel = 1;
            }

            // 直接计算数据，避免使用push方法
            let imageBytes = new Uint8Array(pixelCount * bytesPerPixel);
            let byteIndex = 0;

            // 逐行处理像素数据
            for (let y = 0; y < card.height; y++) {
                for (let x = 0; x < card.width; x++) {
                    const index = (y * card.width + x) * 4;
                    const r = data[index];
                    const g = data[index + 1];
                    const b = data[index + 2];

                    if (format === 'rgb888') {
                        // 检查RGB888反字序设置
                        const isReverseOrder = document.getElementById('rgb888ReverseOrder').checked;
                        if (isReverseOrder) {
                            // BGR顺序
                            imageBytes[byteIndex++] = b;
                            imageBytes[byteIndex++] = g;
                            imageBytes[byteIndex++] = r;
                        } else {
                            // RGB顺序
                            imageBytes[byteIndex++] = r;
                            imageBytes[byteIndex++] = g;
                            imageBytes[byteIndex++] = b;
                        }
                    } else if (format === 'rgb565') {
                        // RGB565格式：2字节
                        const r5 = (r >> 3) & 0x1F;
                        const g6 = (g >> 2) & 0x3F;
                        const b5 = (b >> 3) & 0x1F;
                        const value = (r5 << 11) | (g6 << 5) | b5;
                        const lowByte = value & 0xFF;
                        const highByte = (value >> 8) & 0xFF;

                        // 检查字节顺序设置
                        const isLittleEndian = document.getElementById('rgb565LittleEndian').checked;
                        if (isLittleEndian) {
                            // 低字节在前，高字节在后（小端序）
                            imageBytes[byteIndex++] = lowByte;
                            imageBytes[byteIndex++] = highByte;
                        } else {
                            // 高字节在前，低字节在后（大端序）
                            imageBytes[byteIndex++] = highByte;
                            imageBytes[byteIndex++] = lowByte;
                        }
                    } else if (format === 'rgb332') {
                        // RGB332格式：1字节
                        const r3 = (r >> 5) & 0x07;
                        const g3 = (g >> 5) & 0x07;
                        const b2 = (b >> 6) & 0x03;
                        const value = (r3 << 5) | (g3 << 2) | b2;
                        imageBytes[byteIndex++] = value;
                    }
                }
            }

            // 检查是否启用压缩
            const useRle = document.getElementById('compressionAlgorithm').value === 'rle';
            // 应用RLE压缩
            let finalBytes;
            if (useRle) {
                finalBytes = rleCompress(Array.from(imageBytes), format);
            } else {
                finalBytes = Array.from(imageBytes);
            }

            // 生成数组名称，第一张图片直接使用前缀，后续图片添加_1,_2等
            const arrayPrefix = imgIndex === 0 ? card.arrayPrefix : `${card.arrayPrefix}_${imgIndex}`;

            // 确定format字段值
            let formatValue = 'SGL_PIXMAP_FMT_NONE';
            if (useRle) {
                if (format === 'rgb888') {
                    formatValue = 'SGL_PIXMAP_FMT_RLE_RGB888';
                } else if (format === 'rgb565') {
                    formatValue = 'SGL_PIXMAP_FMT_RLE_RGB565';
                } else if (format === 'rgb332') {
                    formatValue = 'SGL_PIXMAP_FMT_RLE_RGB332';
                }
            } else {
                if (format === 'rgb888') {
                    formatValue = 'SGL_PIXMAP_FMT_RGB888';
                } else if (format === 'rgb565') {
                    formatValue = 'SGL_PIXMAP_FMT_RGB565';
                } else if (format === 'rgb332') {
                    formatValue = 'SGL_PIXMAP_FMT_RGB332';
                }
            }

            // 返回处理结果
            return {
                card: card,
                arrayPrefix: arrayPrefix,
                finalBytes: finalBytes,
                formatValue: formatValue,
                width: card.width,
                height: card.height,
                imgIndex: imgIndex,
                cardIndex: cardIndex
            };
        }

        // 文件下载函数
        function downloadFile(filename, content) {
            const a = document.createElement('a');

            if (typeof content === 'string') {
                const blob = new Blob([content], { type: 'text/plain' });
                a.href = URL.createObjectURL(blob);
            } else {
                a.href = URL.createObjectURL(content);
            }

            a.download = filename;
            document.body.appendChild(a);
            a.click();
            document.body.removeChild(a);
            URL.revokeObjectURL(a.href);
        }
    </script>
</body>
</html>
