#-*-coding:utf-8-*-
from openvpn.models import RadUserList,RadUserGroup
import crypt,random,string

def getsalt(chars=string.letters + string.digits):
	r = '$5$'
	for i in range(1,8):
		r += random.choice(chars)
	r += '$'
	return r

def adduser(username,password,group):
	olduserlist = []
	for i in RadUserList.objects.all().values('username'):
		olduserlist.append(i['username'])
	if username not in olduserlist:
		password = crypt.crypt(password, getsalt())
		RadUserList(username=username,attribute="Crypt-Password",op=':=',value=password).save()
		RadUserGroup(username=username,groupname=group,priority=1).save()
		return True
	else:
		return False

def updateuser(username,password):
	olduserlist = []
	for i in RadUserList.objects.all().values('username'):
		olduserlist.append(i['username'])
	if username in olduserlist:
		password = crypt.crypt(password, getsalt())
		RadUserList.objects.filter(username=username).update(value=password)
		return 'Success'
	else:
		return 'False'

def deluser(username):
	if sqlfilter(username):
		olduserlist = []
		for i in RadUserList.objects.all().values('username'):
			olduserlist.append(i['username'])
		if username in olduserlist:
			RadUserList.objects.filter(username=username).delete()
			RadUserGroup.objects.filter(username=username).delete()
			return True
		else:
			return False
	else:
		return False


def addserver(serverip,serverdomain,enable):
	Oldlist = []
	for i in ServerList.objects.all().values('serverip'):
		Oldlist.append(i['serverip'])

	if serverip not in Oldlist:
		port = 22
		username = 'root'
		password = 'neusoft'
		execmd = ''
		try:
			print 1
		#sshclient_execmd(host, port, username, password, execmd)
		except Exception, e:
			return e
		ServerList(serverip=i['serverip'],serverdomain=serverdomain,enable=enable).save()
	else:
		return 'False'

def delserver(serverip):
	Oldlist = []
	for i in ServerList.objects.all().values('serverip'):
		Oldlist.append(i['serverip'])

	if serverip in Oldlist:
		port = 22
		username = 'root'
		password = 'neusoft'
		execmd = ''
		try:
			print 1
		#sshclient_execmd(host, port, username, password, execmd)
		except Exception, e:
			return e
		ServerList.objects.filter(serverip=serverip).delete()
	else:
		return 'False'

def addguser(userlist,password,group):
	# InsertList = []
	# olduserlist = []
	#
	# for i in RadUserList.objects.all().values('username'):
	# 	olduserlist.append(i['username'])
	# for username in list(set(userlist)):
	# 	if not username == '':
	# 		if sqlfilter(username)
	# 			if username not in olduserlist:
	# 				password = crypt.crypt(password, getsalt())
	# 				InsertList.append(RadUserList(username=username,attribute="Crypt-Password",op=':=',value=password))
	# 				InsertList.append(RadUserGroup(username=i,groupname=group,priority=1))
	# try:
	# 	RadUserGroup.objects.bulk_create(InsertList)
	# 	return True
	# except Exception:
	# 	return False
	print 1

def status():
	from openvpn.models import RadAcct
	#print RadAcct.objects.all().filter(acctstopdelay=None).values('acctstarttime')
	Onlinelist = RadAcct.objects.all().filter(acctstopdelay=None).values('username', 'groupname', 'nasipaddress','acctstarttime', 'callingstationid','framedipaddress')
	return Onlinelist


def sqlfilter(temp):
	import re
	if re.match(r'^[0-9a-zA-Z_]+$',temp):
		return temp
	else:
		return False
#def history():
