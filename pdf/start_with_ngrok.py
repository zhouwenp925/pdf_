"""
使用ngrok快速启动公网访问
需要先安装ngrok: https://ngrok.com/download
"""
import subprocess
import time
import requests
import os
import sys

def get_ngrok_url():
    """获取ngrok的公网URL"""
    try:
        response = requests.get('http://127.0.0.1:4040/api/tunnels', timeout=2)
        data = response.json()
        tunnels = data.get('tunnels', [])
        if tunnels:
            # 优先使用https
            for tunnel in tunnels:
                if tunnel.get('proto') == 'https':
                    return tunnel.get('public_url')
            # 如果没有https，使用http
            return tunnels[0].get('public_url')
    except:
        return None

def main():
    print('=' * 60)
    print('🚀 启动PDF转二维码服务（公网访问模式）')
    print('=' * 60)
    
    # 检查ngrok是否安装
    try:
        result = subprocess.run(['ngrok', 'version'], 
                              capture_output=True, 
                              text=True, 
                              timeout=5)
        print('✅ ngrok已安装')
    except:
        print('❌ 错误：未找到ngrok')
        print('\n请先安装ngrok:')
        print('1. 访问 https://ngrok.com/download')
        print('2. 下载并解压ngrok.exe到系统PATH或当前目录')
        print('3. 注册账号获取authtoken（免费）')
        print('4. 运行: ngrok config add-authtoken <your-token>')
        sys.exit(1)
    
    # 启动ngrok
    print('\n📡 启动ngrok内网穿透...')
    ngrok_process = subprocess.Popen(
        ['ngrok', 'http', '5000'],
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE
    )
    
    # 等待ngrok启动
    print('⏳ 等待ngrok启动...')
    time.sleep(3)
    
    # 获取公网URL
    ngrok_url = None
    for i in range(10):
        ngrok_url = get_ngrok_url()
        if ngrok_url:
            break
        time.sleep(1)
    
    if not ngrok_url:
        print('❌ 无法获取ngrok公网地址')
        print('请检查ngrok是否正常运行')
        ngrok_process.terminate()
        sys.exit(1)
    
    print(f'✅ ngrok已启动')
    print(f'🌐 公网地址: {ngrok_url}')
    
    # 设置环境变量
    os.environ['PUBLIC_URL'] = ngrok_url
    print(f'✅ 已设置 PUBLIC_URL={ngrok_url}')
    
    print('\n' + '=' * 60)
    print('📱 现在任何人都可以扫描二维码访问PDF了！')
    print('=' * 60)
    print('\n按 Ctrl+C 停止服务\n')
    
    # 启动Flask应用
    try:
        from app import app
        app.run(host='0.0.0.0', port=5000, debug=False)
    except KeyboardInterrupt:
        print('\n\n正在关闭服务...')
    finally:
        ngrok_process.terminate()
        print('✅ 服务已停止')

if __name__ == '__main__':
    main()
