#!/bin/sh

cd /etc/init.d
update-rc.d optware.sh defaults

cd /etc/apache2/mods-enabled/
ln -s ../mods-available/autoindex.load
ln -s ../mods-available/autoindex.conf
ln -s ../mods-available/cgi.load
ln -s ../mods-available/auth_basic.load

cd /var/www
ln -s /shares/Media ./media
ln -s /shares/Public ./public

cd /opt
ipkg update
ipkg install lynx

ipkg install dnsmasq
conf-file=/opt/etc/dnsmasq.custom

echo "#deb http://ftp.us.debian.org/debian/ unstable main contrib non-free" >> /etc/apt/sources.list
apt-get update
apt-get install python2.7
cd /usr/bin
ln -sf python2.7 python
apt-cache search pycurl
apt-get install python-pycurl
