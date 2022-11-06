pkg update -y
pkg upgrade -y
apt update -y
apt upgrade -y
pkg install ruby -y
pkg install figlet -y
gem install lolcat
apt install wget -y
apt install git -y
pkg install figlet -y
pkg install proot-distro -y
proot-distro install ubuntu
echo "#!/data/data/com.termux/files/usr/bin/sh" > /data/data/com.termux/files/usr/bin/ubuntu
echo "proot-distro login ubuntu" /data/data/com.termux/files/usr/ubuntu
chmod +x /data/data/com.termux/files/usr/ubuntu
