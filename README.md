# 🖋️ CNN 手写数字识别系统

基于 PyTorch 和 Gradio 构建的手写数字识别 Web 应用。

## ✨ 功能特性

- **手写识别**：在画板上直接书写数字进行识别
- **图片上传**：支持上传手写数字图片进行识别
- **实时预测**：毫秒级响应，显示 Top-3 预测结果及置信度

## 🚀 快速开始

### 本地运行

```bash
pip install -r requirements.txt
python app.py
```

### 访问地址

打开浏览器访问 `http://localhost:7860`

## 🛠️ 技术栈

- **框架**: PyTorch 2.0+
- **界面**: Gradio 4.0+
- **模型**: 轻量级 CNN（99.1% 准确率）

## 📁 项目结构

```
├── app.py          # 主应用代码
├── requirements.txt # 依赖清单
├── cnn_best_model.pth # 预训练模型权重
└── README.md       # 项目说明
```

## 📊 模型架构

```
Conv2d(1→32) → ReLU → Conv2d(32→32) → ReLU → MaxPool → Dropout
Conv2d(32→64) → ReLU → Conv2d(64→64) → ReLU → MaxPool → Dropout
Conv2d(64→128) → ReLU → MaxPool → Dropout
Flatten → Linear(1152→256) → ReLU → Dropout → Linear(256→10)
```

## 🔧 部署到 HuggingFace Spaces

1. Fork 此仓库
2. 在 [HuggingFace Spaces](https://huggingface.co/spaces) 创建新 Space
3. 选择 "Gradio" 作为 SDK
4. 连接你的 GitHub 仓库
5. 等待自动部署完成

## 📝 使用说明

1. 选择"手写识别"选项卡，在画板上书写数字
2. 或选择"图片上传"选项卡，上传手写数字图片
3. 点击识别按钮获取预测结果

## 📄 许可证

MIT License