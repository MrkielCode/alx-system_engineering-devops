#!/usr/bin/env bash
# installing ngnix server and restarting it

apt-get update

apt-get -y install nginx

sudo echo "Hello World!" > /var/www/html/index.html

sudo service nginx reload
