apt update
apt install xfce4 xfce4-goodies -y
apt install tightvncserver
vncserver
vncserver -kill :1
echo "#!/bin/bash" > ~/.vnc/xstartup
echo "xrdb $HOME/.Xresources" >> ~/.vnc/xstartup
echo "startxfce4 &" >> ~/.vnc/xstartup
chmod +x ~/.vnc/xstartup
vncserver
