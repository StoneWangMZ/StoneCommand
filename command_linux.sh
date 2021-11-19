#开启ssh服务
sudo apt-get install openssh-server
dpkg -l | grep ssh
ps -e | grep ssh

ssh username@192.168.1.103 #访问ssh

#查看本地ip
apt-get update
sudo apt install net-tools
sudo apt install iputils-ping
ifconfig

sudo apt-get install terminator #一个好用的终端工具

sudo apt install git-all #安装git
git config --global user.name StoneWang
git config --global user.email stone.wang@aihuishou.com
ssh-keygen -C 'stone.wang@aihuishou.com' -t rsa
cd ~/.ssh

#install anotapad++
sudo add-apt-repository  ppa:notepadqq-team/notepadqq 
sudo apt-get update
sudo apt-get install notepadqq

sudo apt-get remove notepadqq
sudo add-apt-repository --remove ppa:notepadqq-team/notepadqq

#docker相关指令，免sudo使用docker
sudo groupadd docker #创建docker组
sudo gpasswd -a 用户名 docker #将普通用户添加到docker组
sudo systemctl restart docker #重启docker服务后，退出连接重新登录ssh
# 在阿里云创建docker私有仓库 https://blog.csdn.net/lingdi2000/article/details/109694285

watch -n 1 nvidia-smi

cd /    # 回到主目录nvid
df -h   # 10进制显示磁盘情况
rm -rf folder   # 强制删除文件夹及其文件
rm -f fiel.txt  # 强制删除文件
ls | xargs du -ksh  #查看一级子目录存储空间大小

#vi命令，https://www.cnblogs.com/anno-ymy/p/10142925.html
vi myfile.txt   #打开进入命令行模式
#在命令行模式下，按i进入插入模式
#在插入模式下，按esc进入命令行模式
#在命令行模式下，按:进入底行模式
wq  #存盘并退出vi
q!  #不存盘强制退出vi

docker pull registry.cn-hangzhou.aliyuncs.com/ahs-creative/cuda102_pytorch171_detectron03:base

#nvidia-docker安装
curl https://get.docker.com | sh
sudo systemctl start docker && sudo systemctl enable docker
distribution=$(. /etc/os-release;echo $ID$VERSION_ID) && curl -s -L https://nvidia.github.io/nvidia-docker/gpgkey | sudo apt-key add - && curl -s -L https://nvidia.github.io/nvidia-docker/$distribution/nvidia-docker.list | sudo tee /etc/apt/sources.list.d/nvidia-docker.list
curl -s -L https://nvidia.github.io/nvidia-container-runtime/experimental/$distribution/nvidia-container-runtime.list | sudo tee /etc/apt/sources.list.d/nvidia-container-runtime.list
sudo apt-get update
sudo apt-get install -y nvidia-docker2
sudo systemctl restart docker

chmod a+x haha.txt # 给所有用户给予haha.txt文件可执行权限(找不到的命令)

docker ps | grep box-l1-l2-front-defect-hh-1"-deploy"
docker ps | grep cc54ff74b2af|awk '{print $1}'
awk '{print 222}'

tar -zcvf xxx.tar xxx(文件夹) # 压缩
tar -zxvf xxx.tar # 解缩

docker ps | grep $2"-deploy"|awk '{print $1}'


docker ps -a |grep  box-l1-l2-front-defect-hh-1-deploy |awk '{print $1}' | tail  -n +3
























