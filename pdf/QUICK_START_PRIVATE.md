# 🚀 快速开始 - 私有仓库部署（5分钟）

## 步骤概览

1. ✅ 创建私有GitHub仓库
2. ✅ 推送代码到GitHub
3. ✅ Railway连接私有仓库并部署
4. ✅ 配置域名和环境变量
5. ✅ 测试完成

---

## 📝 详细步骤

### 1️⃣ 创建私有GitHub仓库（1分钟）

1. 访问：https://github.com/new
2. 填写：
   - **Repository name**: `pdf-qrcode`
   - **Visibility**: ⚠️ **选择 "Private"**
3. 点击 **"Create repository"**

### 2️⃣ 推送代码到GitHub（2分钟）

在项目目录执行：

```bash
cd D:\GitHub_good_tool\pdf

# 初始化Git（如果还没有）
git init

# 添加所有文件
git add .

# 提交
git commit -m "Initial commit"

# 设置主分支
git branch -M main

# 添加远程仓库（替换为你的实际地址）
git remote add origin https://github.com/你的用户名/pdf-qrcode.git

# 推送代码
git push -u origin main
```

**如果提示需要认证：**
- 使用Personal Access Token（不是密码）
- 创建Token：GitHub → Settings → Developer settings → Personal access tokens
- 勾选 `repo` 权限，生成token
- 推送时使用token作为密码

### 3️⃣ Railway部署（1分钟）

1. 访问：https://railway.app
2. 点击 **"Start a New Project"** → **"Login with GitHub"**
3. 授权Railway访问私有仓库
4. 点击 **"New Project"** → **"Deploy from GitHub repo"**
5. 选择你的 `pdf-qrcode` 仓库
6. 等待部署完成（约2-3分钟）

### 4️⃣ 配置域名（1分钟）

1. Railway项目 → **"Settings"** → **"Domains"**
2. 复制域名（或生成新域名）
3. 项目 → **"Variables"** → **"New Variable"**
4. 添加：
   - Key: `PUBLIC_URL`
   - Value: `https://your-app.up.railway.app`（你的实际域名）
5. Railway自动重启

### 5️⃣ 测试（1分钟）

1. 访问你的Railway域名
2. 上传PDF文件
3. 扫描二维码测试

---

## ✅ 完成检查

- [ ] GitHub仓库是Private（私有）
- [ ] 代码已推送
- [ ] Railway部署成功
- [ ] 设置了PUBLIC_URL
- [ ] 网站可以访问
- [ ] 二维码可以扫描

---

## 🔒 安全性确认

- ✅ 代码在私有GitHub仓库（只有你能看到）
- ✅ PDF文件在Railway服务器（不会上传到GitHub）
- ✅ 只有通过二维码链接才能访问PDF

---

## 📚 详细文档

- **完整指南**：查看 [PRIVATE_REPO_GUIDE.md](PRIVATE_REPO_GUIDE.md)
- **安全性说明**：查看 [SECURITY.md](SECURITY.md)
