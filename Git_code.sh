echo "welcome to Git_code"

# 需要配置git用户名与邮箱 (以后git所有的提交都要使用到的信息)  工作区 -> 暂存区 -> 仓库
git config --global user.name "Andy-Terry"
git config --global user.email "578224854@qq.com"
git init # 在当前文件夹创建一个git仓库

# 更新
git add --all # 从当前文件夹添加文件到暂存区域
git commit -m "V-0.0.1"  # 从暂存区域提交代码到代码仓库

# 将github上的仓库克隆到本地
git clone https://github.com/Andy-Terry/deeplearning_dataset.git

# 把本地项目文件夹下的所有文件（除了新多出的本地仓库文件夹不用），都复制到本地仓库文件夹下
# 进入本地仓库文件夹

git add . #（注：别忘记后面的.，此操作是把Test文件夹下面的文件都添加进来）
git commit -m "V-0.0.1"
git push -u origin master  # （注：此操作目的是把本地仓库push到github上面，此步骤需要你输入帐号和密码）

# https://www.cnblogs.com/cxk1995/p/5800196.html