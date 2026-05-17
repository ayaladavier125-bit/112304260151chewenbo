@echo off
echo ========================================
echo GitHub Push Script
echo 项目: 112304260151chewenbo
echo ========================================

cd /d "%~dp0"

echo.
echo [1/5] 初始化 Git 仓库...
git init

echo.
echo [2/5] 添加所有文件...
git add .

echo.
echo [3/5] 提交更改...
git commit -m "Initial commit: 情感分析项目 - 车文博 112304260151"

echo.
echo [4/5] 添加远程仓库...
git remote add origin https://github.com/ayaladavier125-bit/112304260151chewenbo.git

echo.
echo [5/5] 推送到 GitHub...
git push -u origin main --force

echo.
echo ========================================
echo 完成！请检查 GitHub 仓库确认上传结果。
echo ========================================
pause