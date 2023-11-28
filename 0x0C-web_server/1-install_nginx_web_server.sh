#!/usr/bin/env bash
# installing ngnix server and restarting it

sudo pt-get update

sudo apt-get -y install nginx

sudo sh -c 'echo "Hello World!" > /var/www/html/index.html'

sudo service nginx reload
