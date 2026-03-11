"""
PDF转二维码 - 在线预览工具
将PDF文件转换为二维码，扫码后可直接在浏览器中在线预览
"""
import os
import uuid
import socket
from flask import Flask, render_template, request, send_file, url_for, jsonify
import qrcode
from werkzeug.utils import secure_filename

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'uploads'
app.config['QRCODE_FOLDER'] = 'qrcodes'
app.config['MAX_CONTENT_LENGTH'] = 50 * 1024 * 1024  # 限制上传文件大小为50MB
app.config['ALLOWED_EXTENSIONS'] = {'pdf'}

# 公网URL配置（优先级最高）
# 可以通过环境变量 PUBLIC_URL 设置，例如：export PUBLIC_URL=https://your-domain.com
# Railway会自动设置 RAILWAY_PUBLIC_DOMAIN，如果没有设置PUBLIC_URL则使用它
PUBLIC_URL = os.environ.get('PUBLIC_URL', '').strip()
if not PUBLIC_URL:
    # Railway环境变量
    railway_domain = os.environ.get('RAILWAY_PUBLIC_DOMAIN', '').strip()
    if railway_domain:
        PUBLIC_URL = f'https://{railway_domain}'

# 确保目录存在
os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)
os.makedirs(app.config['QRCODE_FOLDER'], exist_ok=True)


def get_local_ip():
    """获取本机局域网IP地址"""
    try:
        # 连接到一个远程地址来获取本机IP（不会真正发送数据）
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.connect(('8.8.8.8', 80))
        ip = s.getsockname()[0]
        s.close()
        return ip
    except Exception:
        return '127.0.0.1'


def get_qrcode_url(file_id):
    """生成二维码URL，优先级：PUBLIC_URL > 请求host > 局域网IP"""
    # 1. 如果配置了公网URL，优先使用（任何人都可以访问）
    if PUBLIC_URL:
        # 确保URL以/结尾
        base_url = PUBLIC_URL.rstrip('/')
        return f'{base_url}/view/{file_id}'
    
    # 2. 尝试从请求中获取host（如果通过公网访问）
    try:
        host = request.host
        # 如果host不是localhost或127.0.0.1，说明可能是公网访问
        if host and 'localhost' not in host and '127.0.0.1' not in host:
            return url_for('view_pdf', file_id=file_id, _external=True)
    except:
        pass
    
    # 3. 默认使用局域网IP（同一WiFi下的手机可以访问）
    local_ip = get_local_ip()
    port = os.environ.get('PORT', '5000')
    return f'http://{local_ip}:{port}/view/{file_id}'


def allowed_file(filename):
    """检查文件扩展名是否允许"""
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in app.config['ALLOWED_EXTENSIONS']


def generate_qrcode(url, file_id):
    """生成二维码图片"""
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    qr.add_data(url)
    qr.make(fit=True)
    
    img = qr.make_image(fill_color="black", back_color="white")
    qrcode_path = os.path.join(app.config['QRCODE_FOLDER'], f'{file_id}.png')
    img.save(qrcode_path)
    return qrcode_path


@app.route('/')
def index():
    """首页 - PDF上传页面"""
    return render_template('index.html')


@app.route('/upload', methods=['POST'])
def upload_file():
    """处理PDF文件上传"""
    if 'file' not in request.files:
        return jsonify({'error': '没有选择文件'}), 400
    
    file = request.files['file']
    
    if file.filename == '':
        return jsonify({'error': '没有选择文件'}), 400
    
    if not allowed_file(file.filename):
        return jsonify({'error': '只支持PDF文件'}), 400
    
    # 生成唯一文件ID
    file_id = str(uuid.uuid4())
    filename = secure_filename(file.filename)
    file_extension = filename.rsplit('.', 1)[1].lower()
    saved_filename = f'{file_id}.{file_extension}'
    
    # 保存文件
    file_path = os.path.join(app.config['UPLOAD_FOLDER'], saved_filename)
    file.save(file_path)
    
    # 获取文件大小
    file_size = os.path.getsize(file_path)
    
    # 生成PDF访问URL（用于浏览器直接访问）
    pdf_url = url_for('view_pdf', file_id=file_id, _external=True)
    
    # 生成二维码URL（自动选择最佳URL：公网 > 请求host > 局域网IP）
    qrcode_url = get_qrcode_url(file_id)
    
    # 生成二维码
    qrcode_path = generate_qrcode(qrcode_url, file_id)
    
    return jsonify({
        'success': True,
        'file_id': file_id,
        'qrcode_url': url_for('get_qrcode', file_id=file_id),
        'pdf_url': pdf_url,
        'filename': filename,
        'file_size': file_size
    })


@app.route('/view/<file_id>')
def view_pdf(file_id):
    """PDF预览页面"""
    filename = f'{file_id}.pdf'
    file_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
    
    if not os.path.exists(file_path):
        return render_template('error.html', message='PDF文件不存在'), 404
    
    pdf_url = url_for('get_pdf', file_id=file_id)
    return render_template('viewer.html', pdf_url=pdf_url)


@app.route('/pdf/<file_id>')
def get_pdf(file_id):
    """返回PDF文件"""
    filename = f'{file_id}.pdf'
    file_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
    
    if not os.path.exists(file_path):
        return '文件不存在', 404
    
    return send_file(file_path, mimetype='application/pdf')


@app.route('/qrcode/<file_id>')
def get_qrcode(file_id):
    """返回二维码图片"""
    qrcode_path = os.path.join(app.config['QRCODE_FOLDER'], f'{file_id}.png')
    
    if not os.path.exists(qrcode_path):
        return '二维码不存在', 404
    
    return send_file(qrcode_path, mimetype='image/png')


@app.route('/favicon.ico')
def favicon():
    """返回favicon"""
    return '', 204  # 返回空响应，避免404错误


if __name__ == '__main__':
    # Railway使用环境变量PORT，本地开发使用5000
    port = int(os.environ.get('PORT', 5000))
    
    local_ip = get_local_ip()
    print('=' * 50)
    print('PDF转二维码服务启动中...')
    print(f'本地访问: http://localhost:{port}')
    print(f'局域网访问: http://{local_ip}:{port}')
    
    if PUBLIC_URL:
        print(f'✅ 公网访问已配置: {PUBLIC_URL}')
        print('💡 二维码将使用公网地址，任何人都可以扫描访问！')
    else:
        print('💡 提示：手机扫描二维码时，请确保手机和电脑在同一WiFi网络下')
        print('💡 如需公网访问，请设置环境变量 PUBLIC_URL 或使用内网穿透工具')
        print('   例如：set PUBLIC_URL=https://your-domain.com')
    
    print('=' * 50)
    app.run(host='0.0.0.0', port=port, debug=False)
