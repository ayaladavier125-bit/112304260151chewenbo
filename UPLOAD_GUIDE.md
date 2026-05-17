# GitHub 上传指南

## 准备工作

1. **安装 Git**
   - 下载地址：https://git-scm.com/download/win
   - 安装完成后重启终端

2. **创建 GitHub 仓库**
   - 访问：https://github.com/new
   - Repository name: `112304260151chewenbo`
   - 选择 Private（私有）
   - **不要**勾选 "Initialize this repository with a README"
   - 点击 Create repository

3. **生成 GitHub Token（可选但推荐）**
   - 访问：https://github.com/settings/tokens
   - 点击 "Generate new token"
   - 勾选 repo 权限
   - 复制生成的 token（只显示一次）

## 上传步骤

打开 **命令提示符** 或 **PowerShell**，依次运行以下命令：

```bash
# 1. 进入项目目录
cd c:\Users\36886\Desktop\word2vec-nlp-tutorial

# 2. 初始化 Git 仓库
git init

# 3. 配置用户名和邮箱（首次使用）
git config user.name "ayaladavier125-bit"
git config user.email "your_email@example.com"

# 4. 添加所有文件
git add .

# 5. 提交更改
git commit -m "Initial commit: 情感分析项目 - 车文博 112304260151"

# 6. 添加远程仓库
git remote add origin https://github.com/ayaladavier125-bit/112304260151chewenbo.git

# 7. 推送到 GitHub（如果提示输入密码，使用 GitHub Token）
git push -u origin main
```

## 如果遇到冲突

如果仓库已存在文件，先拉取再推送：

```bash
# 拉取远程内容（如果仓库已有文件）
git pull origin main --allow-unrelated-histories

# 解决冲突后重新提交
git add .
git commit -m "Merge with remote"
git push -u origin main
```

## 使用 GitHub CLI（可选）

如果安装了 GitHub CLI：

```bash
# 登录
gh auth login

# 创建仓库（如果还没有）
gh repo create 112304260151chewenbo --private

# 推送
git push -u origin main
```

## 验证上传

上传成功后访问：
https://github.com/ayaladavier125-bit/112304260151chewenbo

确保能看到以下结构：
```
112304260151chewenbo/
├─ src/
│   ├─ sentiment_analysis.py
│   └─ sentiment_analysis_basic.py
├─ submission/
│   └─ submission.csv
├─ data/
├─ notebooks/
├─ images/
├─ .gitignore
└─ README.md
```

## 常见问题

1. **Git 命令找不到**
   - 确保 Git 已安装并添加到系统 PATH
   - 重启终端或电脑

2. **权限错误**
   - 使用 GitHub Token 代替密码
   - 确保仓库名称正确

3. **连接超时**
   - 检查网络连接
   - 尝试使用 HTTPS 而非 SSH

---

**作者**：车文博  
**学号**：112304260151  
**日期**：2026-05-17