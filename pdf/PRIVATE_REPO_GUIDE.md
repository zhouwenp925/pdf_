# 🔒 使用私有GitHub仓库部署指南

使用私有GitHub仓库可以确保代码完全私有，只有你能看到代码和访问仓库。

## 📋 完整步骤

### 步骤1：创建私有GitHub仓库

1. **登录GitHub**
   - 访问：https://github.com
   - 登录你的账号

2. **创建新仓库**
   - 点击右上角的 **"+"** → **"New repository"**
   - 填写仓库信息：
     - **Repository name**: `pdf-qrcode`（或你喜欢的名字）
     - **Description**: PDF转二维码在线预览工具（可选）
     - **Visibility**: ⚠️ **重要！选择 "Private"**（私有）
     - **不要勾选** "Add a README file"（我们本地已有文件）
   - 点击 **"Create repository"**

3. **复制仓库地址**
   - 创建后会显示仓库地址，类似：`https://github.com/你的用户名/pdf-qrcode.git`
   - 复制这个地址，稍后会用到

### 步骤2：准备本地代码并推送到GitHub

1. **初始化Git仓库**（如果还没有）
   ```bash
   cd D:\GitHub_good_tool\pdf
   git init
   ```

2. **检查.gitignore文件**
   ```bash
   # 确认.gitignore包含以下内容（应该已经有了）
   # uploads/
   # qrcodes/
   ```
   这样可以确保PDF文件不会被上传到GitHub。

3. **添加所有文件到Git**
   ```bash
   git add .
   ```

4. **提交代码**
   ```bash
   git commit -m "Initial commit: PDF转二维码工具"
   ```

5. **设置主分支为main**
   ```bash
   git branch -M main
   ```

6. **添加远程仓库**
   ```bash
   git remote add origin https://github.com/你的用户名/pdf-qrcode.git
   ```
   （替换为你的实际仓库地址）

7. **推送到GitHub**
   ```bash
   git push -u origin main
   ```
   
   **如果提示需要认证：**
   - GitHub现在使用Personal Access Token而不是密码
   - 需要创建Token：GitHub → Settings → Developer settings → Personal access tokens → Tokens (classic)
   - 生成新token，勾选 `repo` 权限
   - 使用token作为密码推送

8. **验证上传**
   - 刷新GitHub仓库页面
   - 应该能看到所有代码文件
   - **确认没有 `uploads/` 和 `qrcodes/` 目录**（这些应该在.gitignore中）

### 步骤3：注册Railway账号并连接GitHub

1. **访问Railway**
   - 打开：https://railway.app
   - 点击 **"Start a New Project"**

2. **使用GitHub登录**
   - 选择 **"Login with GitHub"**
   - 授权Railway访问你的GitHub账号
   - Railway会请求访问私有仓库的权限，**点击授权**

3. **验证连接**
   - 登录后应该能看到你的GitHub账号信息

### 步骤4：在Railway部署项目

1. **创建新项目**
   - 在Railway Dashboard点击 **"New Project"**
   - 选择 **"Deploy from GitHub repo"**

2. **选择私有仓库**
   - 在仓库列表中找到你的 `pdf-qrcode` 仓库
   - 点击选择（私有仓库会显示一个锁图标🔒）
   - Railway会自动开始部署

3. **等待部署完成**
   - Railway会自动：
     - 检测Flask应用
     - 安装Python依赖
     - 运行gunicorn启动应用
   - 等待约2-3分钟

4. **查看部署状态**
   - 在项目页面可以看到部署进度
   - 绿色✅表示部署成功
   - 如果失败，点击查看日志了解错误信息

### 步骤5：获取域名并配置环境变量

1. **获取Railway域名**
   - 在项目页面，点击 **"Settings"** 标签
   - 找到 **"Domains"** 部分
   - 复制显示的域名（类似：`your-app.up.railway.app`）
   - 或者点击 **"Generate Domain"** 生成一个

2. **配置环境变量**
   - 在项目页面，点击 **"Variables"** 标签
   - 点击 **"New Variable"**
   - 添加变量：
     - **Key**: `PUBLIC_URL`
     - **Value**: `https://your-app.up.railway.app`（替换为你的实际域名）
     - ⚠️ **重要**：必须包含 `https://` 前缀
   - 点击 **"Add"**

3. **等待重启**
   - Railway会自动重启应用
   - 等待约1-2分钟

### 步骤6：测试部署

1. **访问网站**
   - 打开浏览器访问你的Railway域名
   - 应该能看到PDF上传页面

2. **测试上传**
   - 选择一个PDF文件上传
   - 等待生成二维码

3. **测试二维码**
   - 用手机扫描生成的二维码
   - 应该能正常打开PDF预览

4. **验证安全性**
   - ✅ 代码在私有GitHub仓库中（只有你能看到）
   - ✅ PDF文件在Railway服务器上（只有通过链接才能访问）
   - ✅ 二维码链接使用UUID，几乎不可能被猜到

## 🔍 验证清单

部署完成后，确认：

- [ ] GitHub仓库设置为Private（私有）
- [ ] 代码已推送到GitHub
- [ ] Railway已连接私有仓库
- [ ] Railway部署成功
- [ ] 设置了 `PUBLIC_URL` 环境变量
- [ ] 网站可以正常访问
- [ ] 可以上传PDF并生成二维码
- [ ] 手机扫描二维码可以正常访问

## ❓ 常见问题

### Q1: Railway无法访问私有仓库？

**解决方案：**
1. 检查Railway是否已授权访问GitHub私有仓库
2. 在GitHub → Settings → Applications → Authorized OAuth Apps
3. 找到Railway，确认已授权访问私有仓库

### Q2: 推送代码时提示需要认证？

**解决方案：**
1. GitHub已不再支持密码认证
2. 需要创建Personal Access Token：
   - GitHub → Settings → Developer settings → Personal access tokens → Tokens (classic)
   - 点击 "Generate new token"
   - 勾选 `repo` 权限
   - 复制生成的token
   - 推送时使用token作为密码

### Q3: 如何更新代码？

**步骤：**
```bash
# 修改代码后
git add .
git commit -m "更新说明"
git push origin main

# Railway会自动检测并重新部署
```

### Q4: 如何确认PDF文件没有上传到GitHub？

**检查方法：**
1. 在GitHub仓库页面查看文件列表
2. 确认没有 `uploads/` 目录
3. 确认没有 `qrcodes/` 目录
4. 如果看到这些目录，检查 `.gitignore` 文件

## 🔐 安全性确认

使用私有仓库后：

- ✅ **代码完全私有**：只有你能看到GitHub仓库
- ✅ **PDF文件私有**：存储在Railway服务器，不会上传到GitHub
- ✅ **访问控制**：只有通过二维码链接才能访问PDF
- ✅ **文件ID安全**：使用UUID，几乎不可能被猜到

## 📝 后续操作

### 更新代码
```bash
# 修改代码
git add .
git commit -m "更新说明"
git push origin main
# Railway会自动重新部署
```

### 查看日志
- Railway Dashboard → 项目 → Deployments → 选择部署 → Logs

### 管理文件
- PDF文件存储在Railway服务器的 `uploads/` 目录
- 可以通过Railway的终端访问（如果需要清理）

## 🎉 完成！

现在你的PDF转二维码服务已经：
- ✅ 使用私有GitHub仓库（代码完全私有）
- ✅ 部署到Railway（24/7在线运行）
- ✅ 任何人都可以扫描二维码访问PDF（但代码和PDF都私有）

**安全性总结：**
- 🔒 代码：私有GitHub仓库，只有你能看到
- 🔒 PDF文件：Railway服务器，只有链接可访问
- 🔒 文件ID：UUID生成，几乎不可能被猜到
