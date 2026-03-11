@echo off
chcp 65001 >nul
echo ========================================
echo 推送代码到GitHub
echo ========================================
echo.

echo 当前远程仓库地址:
git remote -v
echo.

echo 检查本地提交状态...
git status
echo.

echo 尝试推送到GitHub...
git push -u origin main

if %errorlevel% equ 0 (
    echo.
    echo ========================================
    echo ✅ 推送成功！
    echo ========================================
    echo.
    echo 下一步：
    echo 1. 访问 https://railway.app
    echo 2. 登录并连接GitHub账号
    echo 3. 选择你的私有仓库部署
    echo ========================================
) else (
    echo.
    echo ========================================
    echo ❌ 推送失败，可能的原因：
    echo ========================================
    echo 1. 网络连接问题（无法访问GitHub）
    echo 2. 需要配置代理
    echo 3. 需要配置SSH密钥
    echo.
    echo 解决方案：
    echo.
    echo 【方案1】配置代理（如果有代理）
    echo    git config --global http.proxy http://127.0.0.1:7890
    echo    git config --global https.proxy http://127.0.0.1:7890
    echo.
    echo 【方案2】使用SSH方式（推荐）
    echo    1. 生成SSH密钥: ssh-keygen -t ed25519 -C "your_email@example.com"
    echo    2. 添加SSH密钥到GitHub
    echo    3. 更改远程地址: git remote set-url origin git@github.com:zhouwenp925/pdf_.git
    echo.
    echo 【方案3】稍后重试
    echo    网络恢复后重新运行此脚本
    echo ========================================
)

pause
