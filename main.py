import os

os.system("clear")

print("""Welcome to Hora Pusa Linux installer!.
Please choose os :
1. Alpine Linux.
2. Arch Linux.
3. Debian (Bullseye).
4. Fedora (35).
5. Opensuse (Tumbleweed).
6. Ubuntu (Jammy).
7. Void Linux.""")
install_os = int(input("> "))
if install_os == 1:
    main_os = "alpine"
elif install_os == 2:
    main_os = "archlinux"
elif install_os == 3:
    main_os = "debian"
elif install_os == 4:
    main_os = "fedora"
elif install_os == 5:
    main_os = "opensuse"
elif install_os == 6:
    main_os = "ubuntu"
elif install_os == 7:
    main_os = "void"
else:
    main_os = "ubuntu"

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

config = f"""#!/data/data/com.termux/files/usr/bin/sh
proot-distro login {main_os}
"""
os.system(f"proot-distro install {main_os}")
os.system(f'''echo a > /data/data/com.termux/files/usr/bin/linux''')
with open("/data/data/com.termux/files/usr/bin/linux", "w") as file:
    file.write(config)
os.system('''chmod +x /data/data/com.termux/files/usr/bin/linux''')
os.system("clear")

print(f"Successfully installed {main_os}.")
print("type 'linux' to start linux vm.")
