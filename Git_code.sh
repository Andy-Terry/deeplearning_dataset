echo "welcome to Git_code"

# 需要配置git用户名与邮箱 (以后git所有的提交都要使用到的信息)
git config --global user.name "Andy-Terry"
git config --global user.email "578224854@qq.com"
git init # 在当前文件夹创建一个git仓库
git add --all # 从当前文件夹添加文件到暂存区域
git commit -m "V-0.0.1"  # 从暂存区域提交代码到代码仓库

# 将github上的仓库克隆到本地
git clone https://github.com/Andy-Terry/deeplearning_dataset.git