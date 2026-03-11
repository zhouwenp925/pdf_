@echo off
chcp 65001 >nul
echo ========================================
echo PDF转二维码服务启动脚本
echo ========================================
echo.
echo 请选择启动方式：
echo 1. 局域网访问（手机需在同一WiFi）
echo 2. 公网访问（使用ngrok，任何人都可以扫描）
echo.
set /p choice=请输入选项 (1 或 2): 

if "%choice%"=="1" (
    echo.
    echo 启动局域网模式...
    python app.py
) else if "%choice%"=="2" (
    echo.
    echo 启动公网模式（ngrok）...
    python start_with_ngrok.py
) else (
    echo 无效选项，启动默认模式...
    python app.py
)

pause
