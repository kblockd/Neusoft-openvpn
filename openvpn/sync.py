#-*-coding:utf-8-*-
import paramiko,re,datetime
from openvpn.models import OnlineUser,ServerList
import os,django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "project_name.settings")# project_name 项目名称
django.setup()

def human_readable_time(t):#时间转码
    if t < 86400:
        m,s = divmod(t,60)
        h,m = divmod(m,60)
        return ("%.2d:%.2d:%.2d" % (h,m,s))
    else:
        m,s = divmod(t,60)
        h,m = divmod(m,60)
        d,h = divmod(h,24)
        return ("%dd %.2d:%.2d:%.2d" % (d,h,m,s))

def sshclient_execmd(hostname, port, username, password, execmd):#创建ssh连接
	paramiko.util.log_to_file("paramiko.log")

	s = paramiko.SSHClient()
	s.set_missing_host_key_policy(paramiko.AutoAddPolicy())

	s.connect(hostname=hostname, port=port, username=username, password=password)
	stdin, stdout, stderr = s.exec_command(execmd)
	stdin.write("Y")  # Generally speaking, the first connection, need a simple interaction.

	return stdout.read()

	s.close()


def sync():#获取数据并整理
	hosts = []
	for i in ServerList.objects.all().values('serverip'):
		hosts.append(i['serverip'])
	port = 22
	syncname = 'root'
	password = 'neusoft'
	execmd = "cat /etc/openvpn/openvpn-status.log"

	querysetlist = []
	for host in hosts:
		log = sshclient_execmd(host, port, syncname, password, execmd)
		find_lst = re.findall('Virtual Address,Common Name,Real Address,Last Ref(.*?)GLOBAL STATS', log, re.S)
		if len(find_lst):
			for item in find_lst:
				line_lst = item.strip("\n").split('\n')
				for line in line_lst:
					if line:
						user_log = line.strip().split(',')
						client_addr = ''.join(user_log[:1])
						username = ''.join(user_log[1:2])
						client_from_addr = re.search(r'\d{1,3}.\d{1,3}.\d{1,3}.\d{1,3}', ''.join(user_log[2:3])).group()
						user_login_time = ''.join(user_log[3:4])
						user_login_time = datetime.datetime.strptime(user_login_time, '%a %b %d %H:%M:%S %Y').strftime('%Y-%m-%d %H:%M:%S')
						user_uptime = (datetime.datetime.now() - datetime.datetime.strptime(user_login_time,'%Y-%m-%d %H:%M:%S')).seconds
						user_uptime = human_readable_time(user_uptime)
						querysetlist.append(OnlineUser(username = username,serverip=host,fromip=client_from_addr,indoorip=client_addr,userlogintime=user_login_time,useruptime=user_uptime))
	try:
		SubIp.objects.bulk_create(querysetlist)
		return 'Success'
	except Exception, e:
		return 'False'


if __name__ == "__main__":
	sshexec()