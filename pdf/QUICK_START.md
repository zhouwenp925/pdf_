# 🚀 快速开始 - 公网访问（任何人都可以扫描）

## 方案1：使用ngrok（最简单，5分钟搞定）⭐推荐

### 步骤1：安装ngrok

1. **下载ngrok**
   - 访问：https://ngrok.com/download
   - 选择Windows版本下载
   - 解压 `ngrok.exe` 到任意目录（建议放到系统PATH或项目目录）

2. **注册账号（免费）**
   - 访问：https://dashboard.ngrok.com/signup
   - 注册账号（免费版足够使用）

3. **配置authtoken**
   ```bash
   ngrok config add-authtoken <你的authtoken>
   ```
   authtoken在注册后的dashboard页面可以看到

### 步骤2：启动服务

**方式A：使用自动启动脚本（推荐）**

```bash
python start_with_ngrok.py
```

脚本会自动：
- 启动ngrok
- 获取公网地址
- 配置环境变量
- 启动Flask应用

**方式B：手动启动**

1. **启动ngrok**（新开一个命令行窗口）：
   ```bash
   ngrok http 5000
   ```

2. **复制ngrok显示的HTTPS地址**（类似：`https://xxxx-xx-xx-xx-xx.ngrok-free.app`）

3. **设置环境变量并启动Flask**：
   ```bash
   # Windows PowerShell
   $env:PUBLIC_URL="https://xxxx-xx-xx-xx-xx.ngrok-free.app"
   python app.py
   
   # Windows CMD
   set PUBLIC_URL=https://xxxx-xx-xx-xx-xx.ngrok-free.app
   python app.py
   
   # Linux/Mac
   export PUBLIC_URL=https://xxxx-xx-xx-xx-xx.ngrok-free.app
   python app.py
   ```

### 步骤3：使用

1. 访问 `http://localhost:5000` 上传PDF
2. 生成的二维码会自动使用ngrok的公网地址
3. **任何人都可以扫描二维码访问PDF**（无需同一WiFi）

---

## 方案2：使用Cloudflare Tunnel（免费，URL稳定）

### 步骤1：安装cloudflared

```bash
# Windows: 下载 https://github.com/cloudflare/cloudflared/releases
# 或使用包管理器
choco install cloudflared
```

### 步骤2：启动tunnel

```bash
cloudflared tunnel --url http://localhost:5000
```

### 步骤3：设置环境变量

复制显示的URL（类似：`https://xxxx.trycloudflare.com`），然后：

```bash
set PUBLIC_URL=https://xxxx.trycloudflare.com
python app.py
```

---

## 方案3：部署到免费云平台（永久免费）

### Railway（推荐）

1. 访问：https://railway.app
2. 使用GitHub账号登录
3. 点击"New Project" → "Deploy from GitHub repo"
4. 选择你的仓库
5. Railway会自动检测Flask应用并部署
6. 部署完成后，复制提供的域名
7. 在Railway的环境变量中添加：`PUBLIC_URL=https://your-app.railway.app`

### Render

1. 访问：https://render.com
2. 注册账号
3. 创建新的Web Service
4. 连接GitHub仓库
5. 设置：
   - Build Command: `pip install -r requirements.txt`
   - Start Command: `gunicorn -w 4 -b 0.0.0.0:$PORT app:app`
6. 部署后复制域名，设置环境变量 `PUBLIC_URL`

---

## 方案4：使用自己的域名和服务器

如果你有自己的域名和服务器：

1. **部署应用**（参考 DEPLOY.md）

2. **设置环境变量**：
   ```bash
   export PUBLIC_URL=https://your-domain.com
   ```

3. **重启应用**

---

## 🔍 验证配置

启动应用后，如果看到：
```
✅ 公网访问已配置: https://xxxx.ngrok-free.app
💡 二维码将使用公网地址，任何人都可以扫描访问！
```

说明配置成功！

---

## ❓ 常见问题

**Q: ngrok免费版有限制吗？**
- 免费版有连接时间限制（2小时），但足够日常使用
- 可以随时重启ngrok获取新的URL

**Q: ngrok的URL会变吗？**
- 免费版每次启动URL都会变化
- 如果需要固定URL，需要付费版或使用Railway/Render等平台

**Q: 如何让URL固定不变？**
- 使用Railway、Render等云平台（免费）
- 或购买ngrok付费版

**Q: 手机扫二维码还是打不开？**
- 检查是否设置了 PUBLIC_URL
- 检查ngrok是否正常运行
- 尝试用手机浏览器直接访问ngrok显示的地址

---

## 💡 推荐方案

- **临时测试**：使用ngrok（方案1）
- **长期使用**：部署到Railway（方案3）
- **有服务器**：使用自己的域名（方案4）
