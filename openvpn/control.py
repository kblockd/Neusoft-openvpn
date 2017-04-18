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

		return 'Success'
	else:
		return 'False'

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
	olduserlist = []
	for i in RadUserList.objects.all().values('username'):
		olduserlist.append(i['username'])
	if username in olduserlist:
		RadUserList.objects.filter(username=username).delete()
		RadUserGroup.objects.filter(username=username).delete()
		return 'Success'
	else:
		return 'False'


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

def addgroupuser(group,userlist):
	InsertList = []
	for i in list(set(userlist)):
		InsertList.append(RadUserGroup(username=i,groupname=group,priority=1))
	try:
		RadUserGroup.objects.bulk_create(InsertList)
		return 'Success'
	except Exception,e:
		return e

def status():
	from openvpn.models import RadAcct
	print RadAcct.objects.all().filter(acctstopdelay=None).values('acctstarttime')
	Onlinelist = RadAcct.objects.all().filter(acctstopdelay=None).values('username', 'groupname', 'nasipaddress','acctstarttime', 'callingstationid','framedipaddress')
	return Onlinelist

#def history():
