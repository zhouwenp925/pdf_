"""
配置文件示例
复制此文件为 config.py 并修改配置
"""

# 公网访问URL（如果设置了，二维码将使用此地址，任何人都可以访问）
# 示例：
# PUBLIC_URL = 'https://your-domain.com'
# PUBLIC_URL = 'https://xxxx.ngrok-free.app'  # ngrok地址
# PUBLIC_URL = 'https://your-app.railway.app'  # Railway地址
PUBLIC_URL = ''

# 服务器配置
HOST = '0.0.0.0'  # 监听所有网络接口
PORT = 5000       # 端口号

# 文件上传配置
MAX_CONTENT_LENGTH = 50 * 1024 * 1024  # 最大文件大小（50MB）
ALLOWED_EXTENSIONS = {'pdf'}  # 允许的文件扩展名

# 存储路径
UPLOAD_FOLDER = 'uploads'
QRCODE_FOLDER = 'qrcodes'
