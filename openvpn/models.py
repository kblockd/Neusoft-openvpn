# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class ServerList(models.Model):
	serverip = models.GenericIPAddressField('服务器ip',protocol='ipv4',unpack_ipv4=False)
	serverdomain = models.CharField('服务器域名',max_length=30,default="NULL")
	enable = models.BooleanField('启用',default=True)

class UserList(models.Model):
	username = models.CharField('用户名', max_length=20, default="NULL")
	validserver = models.IntegerField('允许列表',default="NULL")
	isfreeze = models.BooleanField('冻结',default=True)

class OnlineUser(models.Model):
	serverip = models.GenericIPAddressField('服务器ip',protocol='ipv4',unpack_ipv4=False)
	username = models.CharField('用户名',max_length=20,default="NULL")
	fromip = models.GenericIPAddressField('来源ip',protocol='ipv4',unpack_ipv4=False)
	indoorip = models.GenericIPAddressField('内部ip',protocol='ipv4',unpack_ipv4=False)
	userlogintime = models.CharField('登录时间',max_length=30,default="NULL")
	useruptime = models.CharField('在线时长',max_length=15,default="NULL")

class UserLoginHistory(models.Model):
	serverip = models.GenericIPAddressField('服务器ip',protocol='ipv4',unpack_ipv4=False)
	username = models.CharField('用户名', max_length=20, default="NULL")
	fromip = models.GenericIPAddressField('来源ip', protocol='ipv4', unpack_ipv4=False)
	indoorip = models.GenericIPAddressField('内部ip', protocol='ipv4', unpack_ipv4=False)
	userlogintime = models.CharField('登录时间', max_length=30, default="NULL")
	userlogouttime = models.CharField('下线时间', max_length=30, default="NULL")
	useruptime = models.CharField('在线时长', max_length=10, default="NULL")

class RadUserList(models.Model):
	username = models.CharField('用户名',max_length=20,default="NULL")
	attribute = models.CharField('认证', max_length=19, default="Cleartext-Password")
	op = models.CharField('认证2', max_length=2, default=":=")
	value = models.CharField('密码', max_length=64, default="NeusoftOpenVpn.Nss@A3-200OK")

class RadGroupList(models.Model):
	username = models.CharField('用户名',max_length=20,default="NULL")
	groupname = models.CharField('组',max_length=20,default="vpnuser")
	priority = models.IntegerField('priority',default=1)
