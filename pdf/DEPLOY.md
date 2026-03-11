# 部署指南

## 📱 为什么二维码扫不了？

**问题原因：** 二维码中的链接是 `http://localhost:5000`，手机无法访问电脑的 localhost。

## ✅ 解决方案

### 方案1：局域网访问（最简单，推荐）

**适用场景：** 手机和电脑在同一WiFi网络下

**使用方法：**
1. 确保手机和电脑连接**同一个WiFi**
2. 重启应用（代码已自动修改，会使用局域网IP）
3. 扫描二维码即可访问

**验证：**
- 启动应用时会显示：`局域网访问: http://172.27.218.32:5000`
- 用手机浏览器直接访问这个地址，能打开说明配置成功

---

### 方案2：部署到云服务器（公网访问）

**适用场景：** 需要让任何人（不在同一网络）都能访问

#### 步骤1：准备云服务器

推荐平台：
- **阿里云** / **腾讯云** / **华为云**（国内）
- **AWS** / **DigitalOcean** / **Vultr**（国外）

#### 步骤2：上传代码到服务器

```bash
# 方式1：使用Git
git clone <你的仓库地址>
cd pdf

# 方式2：使用SCP上传
scp -r pdf/ user@服务器IP:/path/to/
```

#### 步骤3：服务器上安装依赖

```bash
# SSH连接到服务器
ssh user@服务器IP

# 进入项目目录
cd pdf

# 安装Python和依赖
sudo apt update
sudo apt install python3 python3-pip
pip3 install -r requirements.txt
```

#### 步骤4：使用Gunicorn运行（生产环境）

```bash
# 安装Gunicorn
pip3 install gunicorn

# 运行应用
gunicorn -w 4 -b 0.0.0.0:5000 app:app
```

#### 步骤5：配置Nginx反向代理（可选但推荐）

```nginx
server {
    listen 80;
    server_name your-domain.com;  # 你的域名

    location / {
        proxy_pass http://127.0.0.1:5000;
        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
    }
}
```

#### 步骤6：配置HTTPS（推荐）

使用Let's Encrypt免费证书：

```bash
sudo apt install certbot python3-certbot-nginx
sudo certbot --nginx -d your-domain.com
```

---

### 方案3：使用内网穿透（临时测试）

**适用场景：** 快速测试，不想买服务器

#### 使用 ngrok（推荐）

1. **注册账号**：访问 https://ngrok.com 注册

2. **下载ngrok**：
   ```bash
   # Windows: 下载 ngrok.exe
   # 或使用包管理器
   choco install ngrok  # 需要Chocolatey
   ```

3. **启动Flask应用**：
   ```bash
   python app.py
   ```

4. **启动ngrok**：
   ```bash
   ngrok http 5000
   ```

5. **获取公网地址**：
   ngrok会显示类似：`https://xxxx-xx-xx-xx-xx.ngrok.io`
   
6. **修改代码使用ngrok地址**（临时方案）

#### 使用 frp（自建内网穿透）

1. 需要一台有公网IP的服务器
2. 配置frp服务端和客户端
3. 详细教程：https://github.com/fatedier/frp

---

### 方案4：使用Docker部署

#### 创建 Dockerfile

```dockerfile
FROM python:3.9-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

EXPOSE 5000

CMD ["gunicorn", "-w", "4", "-b", "0.0.0.0:5000", "app:app"]
```

#### 构建和运行

```bash
# 构建镜像
docker build -t pdf-qrcode .

# 运行容器
docker run -d -p 5000:5000 \
  -v $(pwd)/uploads:/app/uploads \
  -v $(pwd)/qrcodes:/app/qrcodes \
  --name pdf-qrcode \
  pdf-qrcode
```

---

## 🔧 修改代码使用固定域名/IP

如果需要使用固定的公网地址，可以修改 `app.py`：

```python
# 在 app.py 顶部添加配置
PUBLIC_URL = 'https://your-domain.com'  # 或 'http://your-server-ip:5000'

# 修改 get_qrcode_url 函数
def get_qrcode_url(file_id, use_local_ip=False):
    if PUBLIC_URL:
        return f'{PUBLIC_URL}/view/{file_id}'
    # ... 其他代码
```

---

## 📝 关于GitHub Pages

**GitHub Pages 不支持运行 Flask 应用**，它只能托管静态网站。

**但是可以：**
- ✅ 将代码上传到 GitHub 仓库（用于版本控制）
- ✅ 使用 GitHub Actions 自动部署到服务器
- ❌ 不能直接在 GitHub Pages 上运行这个应用

---

## 🚀 快速测试（局域网）

1. **重启应用**：
   ```bash
   python app.py
   ```

2. **查看启动信息**，会显示局域网IP：
   ```
   局域网访问: http://172.27.218.32:5000
   ```

3. **用手机浏览器访问**这个地址，确认能打开

4. **上传PDF并扫描二维码**，现在应该可以正常访问了！

---

## ❓ 常见问题

**Q: 手机还是扫不了？**
- 检查手机和电脑是否在同一WiFi
- 检查电脑防火墙是否允许5000端口
- 尝试用手机浏览器直接访问显示的局域网地址

**Q: 如何让外网访问？**
- 使用方案2（云服务器）或方案3（内网穿透）

**Q: 需要购买服务器吗？**
- 局域网使用：不需要
- 公网访问：需要（或使用免费的内网穿透服务）
