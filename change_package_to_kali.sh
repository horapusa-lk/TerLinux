apt update -y
apt-get install net-tools -y 
apt-get install gnupg 
wget -q -O - https://archive.kali.org/archive-key.asc | gpg --import 
grep -v '#' /etc/apt/sources.list | sort -u
echo "deb http://http.kali.org/kali kali-rolling main non-free contrib" > /etc/apt/sources.list
echo "deb-src http://http.kali.org/kali kali-rolling main non-free contrib" | sudo tee -a /etc/apt/sources.list 
wget -q -O - https://archive.kali.org/archive-key.asc | apt-key add 
apt-get update && apt-cache search kali-linux 
apt-get install kali-linux-everything -y 
exit
