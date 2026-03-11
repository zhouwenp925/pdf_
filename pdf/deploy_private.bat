@echo off
chcp 65001 >nul
echo ========================================
echo 私有GitHub仓库部署助手
echo ========================================
echo.

echo 步骤1: 检查Git状态
git status
echo.

echo 步骤2: 添加所有文件
git add .
echo.

echo 步骤3: 提交代码
set /p commit_msg=请输入提交信息 (直接回车使用默认): 
if "%commit_msg%"=="" set commit_msg=Update code
git commit -m "%commit_msg%"
echo.

echo 步骤4: 检查远程仓库
git remote -v
echo.

echo 步骤5: 推送到GitHub
echo 如果提示需要认证，请使用Personal Access Token
git push origin main
echo.

echo ========================================
echo 代码已推送到GitHub！
echo.
echo 下一步：
echo 1. 访问 https://railway.app
echo 2. 登录并连接GitHub账号
echo 3. 选择你的私有仓库部署
echo ========================================
pause
