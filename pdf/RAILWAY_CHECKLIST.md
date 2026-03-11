# ✅ Railway部署检查清单

## 📦 部署前检查

### 1. 文件检查
确保以下文件存在：
- [x] `app.py` - Flask主应用
- [x] `requirements.txt` - Python依赖（包含gunicorn）
- [x] `Procfile` - Railway启动命令
- [x] `templates/` - HTML模板目录
- [x] `static/` - CSS样式目录
- [x] `.gitignore` - Git忽略文件

### 2. GitHub仓库
- [ ] 代码已推送到GitHub
- [ ] 所有文件已提交（`git add .` 和 `git commit`）
- [ ] 已推送到远程仓库（`git push`）

### 3. Railway账号
- [ ] 已注册Railway账号（https://railway.app）
- [ ] 已使用GitHub账号登录
- [ ] 已授权Railway访问GitHub

## 🚀 部署步骤

### 步骤1：创建项目
- [ ] 在Railway点击 "New Project"
- [ ] 选择 "Deploy from GitHub repo"
- [ ] 选择你的仓库

### 步骤2：等待部署
- [ ] Railway自动检测Flask应用
- [ ] 自动安装依赖
- [ ] 部署完成（约2-3分钟）

### 步骤3：获取域名
- [ ] 在项目设置中找到 "Domains"
- [ ] 复制显示的域名（如：`your-app.up.railway.app`）

### 步骤4：配置环境变量
- [ ] 进入项目 → "Variables"
- [ ] 添加变量：
  - Key: `PUBLIC_URL`
  - Value: `https://your-app.up.railway.app`（替换为你的实际域名）
- [ ] 确保包含 `https://` 前缀
- [ ] Railway自动重启应用

### 步骤5：测试
- [ ] 访问你的Railway域名
- [ ] 上传PDF文件
- [ ] 生成二维码
- [ ] 用手机扫描二维码测试

## 🔍 验证清单

部署成功后，检查：

- [ ] 网站可以正常访问
- [ ] 可以上传PDF文件
- [ ] 二维码可以正常生成
- [ ] 手机扫描二维码可以打开PDF预览
- [ ] PDF预览页面功能正常（缩放、翻页等）

## ❓ 常见问题

### 部署失败？
- [ ] 检查 `requirements.txt` 是否正确
- [ ] 检查 `Procfile` 格式是否正确
- [ ] 查看Railway日志了解错误信息

### 二维码扫不了？
- [ ] 确认设置了 `PUBLIC_URL` 环境变量
- [ ] 确认 `PUBLIC_URL` 包含 `https://` 前缀
- [ ] 尝试用手机浏览器直接访问Railway域名

### 文件上传失败？
- [ ] 检查文件大小（默认限制50MB）
- [ ] 检查文件格式是否为PDF
- [ ] 查看Railway日志

## 📝 部署后

部署成功后：

1. **保存你的Railway域名**（URL不会变化）
2. **可以分享给任何人使用**
3. **代码更新会自动部署**（推送代码到GitHub）

## 🎉 完成！

如果所有项目都打勾，恭喜你！PDF转二维码服务已经成功部署到Railway了！

现在任何人都可以：
- ✅ 访问你的网站上传PDF
- ✅ 扫描二维码在线查看PDF
- ✅ 无需下载、无需跳转、无广告
