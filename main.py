import os

os.system("pkg update -y")
os.system("pkg upgrade -y")
os.system("apt update -y")
os.system("apt upgrade -y")
os.system("pkg install ruby -y")
os.system("pkg install figlet -y")
os.system("gem install lolcat")
os.system("apt install wget -y")
os.system("apt install git -y")
os.system("pkg install figlet -y")
os.system("pkg install proot-distro -y")
os.system("proot-distro install debian")


termux_command_content = """#!/data/data/com.termux/files/usr/bin/sh
proot-distro login ubuntu"""
with open("/data/data/com.termux/files/usr/bin", 'w') as command:
    command.write(termux_command_content)

