#!/bin/bash

apt update

apt-get install -yq git

mkdir /opt/nodejs
curl https://nodejs.org/dist/v20.11.0/node-v20.11.0-linux-x64.tar.gz | sudo tar xvzf - -C /opt/nodejs --strip-components=1
ln -s /opt/nodejs/bin/node /usr/bin/node
ln -s /opt/nodejs/bin/npm /usr/bin/npm


apt install pip3

pip3 install flask
pip3 install flask-cors
pip3 install pandas