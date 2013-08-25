#!/usr/bin/env python
import os
import socket,urllib
try:
	server=os.environ["SERVER_NAME"]
except:
	server="Storage"
try:
	filename=os.environ["QUERY_STRING"]
except:
	filename="media/test.mkv"

pos=filename.find('&')
arg=''
if pos>=0:
	arg=filename[pos+1:]
	filename=filename[:pos]
filename=urllib.unquote(filename)


s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.connect(('127.0.0.1',7890))
if arg=='qa':
	s.send("I%s\n"%filename)
	d=s.recv(1024)
	x=list(eval(d))
	length=x[0].strip()
	hour,min,sec=x[0].split(":")
	if sec[-1]==',': sec=sec[:-1]
	alll=int(hour)*3600+int(min)*60+float(sec)
	alll=int(alll)
	ret=[]
	ret.append(alll)
	audios=[]
	try:
		for audline in x[2]:
			info=audline.split("Audio:")
			sid=info[0].split()[1].split('.')[1]
			pos=sid.find("(")
			lang=''
			if pos>=0:
				lang=sid[pos:]
				sid=sid[:pos]
			else:
				if sid[-1]==":":sid=sid[:-1]
			sinfo=lang+info[1].strip()
			audios.append([sid,sinfo])
	except:
		audios=[]
	ret.append(audios)
	print "Content-type: text/html\r\n\r\n",
	print str(ret)
else:
	if arg!='':
		filename=filename+'.q'
		if arg[0]=='Q':
			filename=filename+'c'
		else:
			filename=filename+'t'
		filename=filename+arg[1]
	s.send("S%s\n"%filename)
	d=s.recv(1024)
	x=eval(d)
	length=x[0].strip()
	hour,min,sec=x[0].split(":")
	if sec[-1]==',': sec=sec[:-1]
	alll=int(hour)*3600+int(min)*60+float(sec)
	alll=int(alll)
	s.close()
	url='http://%s/media/.avs/pl/%s.m3u8'% (server,alll)
	print "Status: 302 Moved"
	print "Location: %s" % url
	print "URI: %s" % url
	print "Content-type: text/html\r\n\r\n"

