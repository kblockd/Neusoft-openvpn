from openvpn.models import ,ServerList


def addserver(serverip,serverdomain,enable):
	Oldlist = ServerList.objects.all().values('serverip')
	for i in Oldlist:
		if serverip != i['serverip']:
			ServerList(serverip=i['serverip'],serverdomain=serverdomain,enable=enable)