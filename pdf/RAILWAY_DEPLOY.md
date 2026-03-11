# 🚂 Railway 部署指南

Railway是一个现代化的云平台，可以免费部署Flask应用，非常适合这个项目！

## ✨ Railway的优势

- ✅ **完全免费**（有免费额度，足够使用）
- ✅ **自动HTTPS**（无需配置SSL证书）
- ✅ **固定域名**（URL不会变化）
- ✅ **自动部署**（连接GitHub，代码推送自动部署）
- ✅ **简单易用**（5分钟完成部署）

## 📋 部署步骤

### 步骤1：准备GitHub仓库

1. **创建GitHub仓库**（如果还没有）
   ```bash
   git init
   git add .
   git commit -m "Initial commit"
   git branch -M main
   git remote add origin https://github.com/你的用户名/pdf-qrcode.git
   git push -u origin main
   ```

2. **🔒 重要：选择仓库类型**
   - **公开仓库**：代码公开，但PDF文件仍然私有（推荐大多数场景）
   - **私有仓库**：代码和PDF都完全私有（推荐敏感场景）
   - 创建仓库时选择 **"Private"** 即可

3. **确保所有文件已提交**
   - ✅ `app.py`
   - ✅ `requirements.txt`
   - ✅ `Procfile`
   - ✅ `templates/` 目录
   - ✅ `static/` 目录
   - ✅ `.gitignore`（确保PDF文件不会被上传）
   
   **注意：** `uploads/` 和 `qrcodes/` 目录已在`.gitignore`中，**PDF文件不会上传到GitHub**

### 步骤2：注册Railway账号

1. 访问：https://railway.app
2. 点击 **"Start a New Project"**
3. 选择 **"Login with GitHub"**（使用GitHub账号登录）
4. 授权Railway访问你的GitHub账号

### 步骤3：部署项目

1. **创建新项目**
   - 在Railway Dashboard点击 **"New Project"**
   - 选择 **"Deploy from GitHub repo"**

2. **选择仓库**
   - 选择你的 `pdf-qrcode` 仓库
   - Railway会自动检测到Flask应用

3. **等待部署**
   - Railway会自动：
     - 安装Python依赖
     - 运行 `gunicorn` 启动应用
     - 分配公网域名

4. **获取域名**
   - 部署完成后，在项目设置中找到 **"Domains"**
   - 复制显示的域名（类似：`your-app.up.railway.app`）

### 步骤4：配置环境变量（重要！）

**方式A：自动配置（推荐）**

代码已自动检测Railway环境，如果Railway分配了域名，会自动使用。但为了确保二维码正确，建议手动设置：

1. **进入项目设置**
   - 点击项目名称进入详情页
   - 点击 **"Variables"** 标签

2. **设置 PUBLIC_URL**
   - 点击 **"New Variable"**
   - Key: `PUBLIC_URL`
   - Value: `https://your-app.up.railway.app`（替换为你的实际域名）
   - ⚠️ **重要**：必须包含 `https://` 前缀
   - 点击 **"Add"**

3. **验证配置**
   - Railway会自动重启应用
   - 等待部署完成（约1-2分钟）
   - 查看日志确认启动成功

**方式B：使用Railway自动域名**

Railway会自动设置 `RAILWAY_PUBLIC_DOMAIN` 环境变量，代码会自动检测并使用。但为了确保稳定性，建议还是手动设置 `PUBLIC_URL`。

### 步骤5：测试部署

1. **访问应用**
   - 打开浏览器访问：`https://your-app.up.railway.app`
   - 应该能看到上传页面

2. **上传PDF测试**
   - 上传一个PDF文件
   - 生成二维码
   - 用手机扫描二维码，应该能正常访问！

## 🔧 高级配置

### 自定义域名（可选）

Railway支持绑定自定义域名：

1. 在项目设置 → **"Domains"** → **"Custom Domain"**
2. 输入你的域名（如：`pdf.example.com`）
3. 按照提示配置DNS记录
4. 更新 `PUBLIC_URL` 环境变量为新域名

### 增加文件大小限制

如果需要上传更大的PDF文件：

1. 在Railway项目设置 → **"Variables"**
2. 添加环境变量：
   - Key: `MAX_CONTENT_LENGTH`
   - Value: `104857600`（100MB，单位：字节）

### 查看日志

- 在Railway Dashboard点击项目
- 点击 **"Deployments"** 标签
- 选择最新的部署
- 查看 **"Logs"** 了解运行状态

## 📱 使用说明

部署完成后：

1. **访问你的Railway域名**：`https://your-app.up.railway.app`
2. **上传PDF文件**
3. **下载二维码**
4. **任何人都可以扫描二维码访问PDF**（无需同一WiFi）

## 🔒 安全性说明

**重要：** GitHub仓库只存储代码，**不存储PDF文件**！

- ✅ PDF文件存储在Railway服务器上，不会上传到GitHub
- ✅ `uploads/` 目录已在`.gitignore`中，Git不会跟踪PDF文件
- ✅ 只有通过二维码链接才能访问PDF，没有链接的人无法访问
- ✅ 文件ID使用UUID生成，几乎不可能被猜到

**如果担心代码隐私：**
- 使用**私有GitHub仓库**（创建时选择Private）
- Railway可以连接私有仓库（需要授权）

**详细安全性说明请参考：** [SECURITY.md](SECURITY.md)

## 🔍 故障排查

### 问题1：部署失败

**检查：**
- `requirements.txt` 是否包含所有依赖
- `Procfile` 格式是否正确
- 代码是否有语法错误

**查看日志：**
- Railway Dashboard → 项目 → Deployments → Logs

### 问题2：二维码扫不了

**检查：**
- 是否设置了 `PUBLIC_URL` 环境变量
- `PUBLIC_URL` 是否正确（包含 `https://`）
- 尝试用手机浏览器直接访问Railway域名

### 问题3：文件上传失败

**检查：**
- 文件大小是否超过限制（默认50MB）
- 文件格式是否为PDF
- 查看Railway日志了解错误信息

## 💰 免费额度说明

Railway免费版提供：
- **$5/月免费额度**
- **500小时运行时间**
- **足够个人使用**

如果超出免费额度，可以：
- 升级到付费计划
- 或使用其他免费平台（Render、Fly.io等）

## 🎉 完成！

现在你的PDF转二维码服务已经部署到Railway了！

**特点：**
- ✅ 24/7在线运行
- ✅ 固定域名，URL不会变化
- ✅ 自动HTTPS加密
- ✅ 任何人都可以扫描二维码访问
- ✅ 代码更新自动部署

## 📚 相关文档

- [Railway官方文档](https://docs.railway.app)
- [Flask部署指南](https://docs.railway.app/guides/flask)
- [环境变量配置](https://docs.railway.app/develop/variables)
