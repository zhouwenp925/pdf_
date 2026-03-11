# PDF转二维码 - 在线预览工具

## 📋 项目简介

将PDF文件转换为二维码，扫码后可直接在浏览器中在线预览PDF，无需下载、无需跳转、无需注册，干净无广告。

### ✨ 核心特性

- ✅ **扫码即看** - 扫描二维码直接打开PDF预览
- ✅ **无需下载** - 浏览器内直接查看，不下载文件
- ✅ **无需跳转** - 不跳转第三方网盘或网站
- ✅ **无广告** - 干净简洁的预览界面
- ✅ **无限制** - 任何人都可以访问，无需注册登录
- ✅ **离线可用** - 支持本地部署，完全自主控制

## 🚀 技术方案

### 架构设计

```
PDF文件 → 上传到服务器 → 生成唯一URL → 生成二维码 → 扫码访问 → PDF.js在线预览
```

### 技术栈

- **后端**: Python Flask
- **PDF预览**: PDF.js (Mozilla开源PDF查看器)
- **二维码生成**: qrcode库
- **前端**: HTML + JavaScript (PDF.js)

### 工作流程

1. 用户上传PDF文件
2. 服务器保存PDF并生成唯一访问ID
3. 生成二维码（包含PDF访问URL）
4. 用户扫描二维码
5. 浏览器打开PDF预览页面（使用PDF.js）
6. 直接在线查看PDF，无需下载

## 📁 项目结构

```
pdf/
├── README.md              # 项目说明文档
├── requirements.txt       # Python依赖包
├── app.py                 # Flask主应用
├── templates/
│   ├── index.html         # 上传页面
│   └── viewer.html        # PDF预览页面
├── static/
│   ├── pdfjs/             # PDF.js库文件
│   └── style.css          # 样式文件
├── uploads/               # PDF文件存储目录
└── qrcodes/               # 二维码图片存储目录
```

## 🛠️ 安装与使用

### 环境要求

- Python 3.7+
- pip

### 安装步骤

1. **克隆或下载项目**
```bash
cd pdf
```

2. **安装依赖**
```bash
pip install -r requirements.txt
```

3. **运行应用**
```bash
python app.py
```

4. **访问应用**
- 打开浏览器访问: `http://localhost:5000`
- 上传PDF文件
- 下载生成的二维码
- 扫描二维码即可在线查看PDF

### 📱 二维码访问说明

#### 方式1：局域网访问（手机需在同一WiFi）

1. 确保手机和电脑连接**同一个WiFi网络**
2. 启动应用时会显示局域网IP（如：`http://172.27.218.32:5000`）
3. 上传PDF后生成的二维码会自动使用局域网IP
4. 手机扫描二维码即可直接访问PDF预览

#### 方式2：公网访问（任何人都可以扫描）⭐推荐

**🚂 Railway部署（推荐，永久免费，固定域名）**

**🔒 使用私有GitHub仓库（推荐，代码完全私有）**

1. **创建私有GitHub仓库**：选择"Private"创建仓库
2. **推送代码到GitHub**：`git push` 推送代码
3. **注册Railway**：访问 https://railway.app，使用GitHub登录并授权访问私有仓库
4. **部署项目**：选择"Deploy from GitHub repo"，选择你的私有仓库
5. **配置域名**：Railway会自动分配域名，在环境变量中设置 `PUBLIC_URL`
6. **完成！** 现在任何人都可以扫描二维码访问PDF了，但代码完全私有！

**快速开始（5分钟）：** [QUICK_START_PRIVATE.md](QUICK_START_PRIVATE.md) ⭐  
**详细步骤：** [PRIVATE_REPO_GUIDE.md](PRIVATE_REPO_GUIDE.md)  
**公开仓库部署：** [RAILWAY_DEPLOY.md](RAILWAY_DEPLOY.md)

**其他快速方案：**
- **ngrok**（临时测试）：`python start_with_ngrok.py` - 详见 [QUICK_START.md](QUICK_START.md)
- **Render**（免费云平台）- 详见 [QUICK_START.md](QUICK_START.md)
- **Cloudflare Tunnel**（免费内网穿透）- 详见 [QUICK_START.md](QUICK_START.md)
- **自己的服务器** - 详见 [DEPLOY.md](DEPLOY.md)

## 📖 使用说明

### 上传PDF

1. 访问 `http://localhost:5000`
2. 点击"选择文件"按钮，选择PDF文件
3. 点击"上传并生成二维码"
4. 页面会显示二维码图片，可以下载保存

### 查看PDF

1. 使用手机扫描二维码
2. 浏览器自动打开PDF预览页面
3. 直接在线查看PDF内容
4. 支持缩放、翻页等操作

## 🔧 配置说明

### 修改端口

在 `app.py` 中修改：
```python
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
```

### 修改文件大小限制

在 `app.py` 中修改：
```python
app.config['MAX_CONTENT_LENGTH'] = 50 * 1024 * 1024  # 50MB
```

### 修改存储路径

在 `app.py` 中修改：
```python
UPLOAD_FOLDER = 'uploads'
QRCODE_FOLDER = 'qrcodes'
```

## 🌐 部署说明

### 本地部署

直接运行 `python app.py` 即可，适合内网使用。

### 公网部署

1. **使用云服务器**
   - 上传代码到服务器
   - 安装依赖
   - 使用gunicorn或uwsgi运行
   - 配置Nginx反向代理

2. **使用Docker** (可选)
   ```dockerfile
   FROM python:3.9
   WORKDIR /app
   COPY requirements.txt .
   RUN pip install -r requirements.txt
   COPY . .
   CMD ["python", "app.py"]
   ```

3. **配置HTTPS**
   - 使用Let's Encrypt免费证书
   - 配置SSL/TLS加密

## 🔒 安全考虑

### 当前安全措施

- ✅ **PDF文件私有**：PDF文件存储在Railway服务器，不会上传到GitHub
- ✅ **唯一ID访问**：使用UUID生成文件ID，几乎不可能被猜到
- ✅ **Git忽略**：`uploads/` 目录已在`.gitignore`中，PDF文件不会进入Git仓库
- ✅ **只有链接可访问**：没有二维码链接的人无法访问PDF

### 可选安全增强

- 🔐 **使用私有GitHub仓库**：代码完全私有（推荐）
- 🔐 **访问密码保护**：为PDF添加密码（可选功能）
- 🔐 **访问次数限制**：限制访问次数后自动删除（可选功能）
- 🔐 **过期时间**：设置文件过期时间（可选功能）

**详细安全性说明请参考：** [SECURITY.md](SECURITY.md)

## 📝 待实现功能

- [ ] 访问密码保护
- [ ] 访问次数限制
- [ ] 文件过期时间
- [ ] 批量上传
- [ ] 文件管理后台
- [ ] 访问统计
- [ ] 移动端优化

## 🤝 贡献

欢迎提交Issue和Pull Request！

## 📄 许可证

MIT License

## 🙏 致谢

- [PDF.js](https://mozilla.github.io/pdf.js/) - Mozilla开源PDF查看器
- [Flask](https://flask.palletsprojects.com/) - Python Web框架
- [qrcode](https://github.com/lincolnloop/python-qrcode) - 二维码生成库
