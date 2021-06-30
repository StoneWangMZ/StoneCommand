#开启ssh服务
sudo apt-get install openssh-server
dpkg -l | grep ssh
ps -e | grep ssh

#访问ssh
ssh username@192.168.1.103


#查看本地ip
apt-get update
sudo apt install net-tools
sudo apt install iputils-ping
ifconfig

sudo apt-get install terminator #一个好用的终端工具

sudo apt install git-all #安装git

#install anotapad++
sudo add-apt-repository  ppa:notepadqq-team/notepadqq 
sudo apt-get update
sudo apt-get install notepadqq

sudo apt-get remove notepadqq
sudo add-apt-repository --remove ppa:notepadqq-team/notepadqq






