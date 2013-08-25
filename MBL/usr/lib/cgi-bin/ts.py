#!/usr/bin/env python
import os
import socket,urllib
try:
	server=os.environ["SERVER_NAME"]
except:
	server="Storage"
try:
	seg=os.environ["QUERY_STRING"]
except:
	seg='0'


s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.connect(('127.0.0.1',7890))
s.send("G%s\n"%seg)
d=s.recv(1024)
url='http://%s/media/.avs/segment_%s.ts'% (server,seg)
print "Status: 302 Moved"
print "Location: %s" % url
print "URI: %s" % url
print "Content-type: text/html\r\n\r\n"

