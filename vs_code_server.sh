apt update
apt upgrade -y
apt install docker.io -y
docker run -it --init -p 3000:3000 -v "$(pwd):/home/workspace:cached" gitpod/openvscode-server
