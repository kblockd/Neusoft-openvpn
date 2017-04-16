# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.

# class UserList(models.Model):
# 	username = models.CharField('用户名', max_length=20, default="NULL")
# 	validserver = models.IntegerField('允许列表',default="NULL")
# 	isfreeze = models.BooleanField('冻结',default=True)
#
# class OnlineUser(models.Model):
# 	serverip = models.GenericIPAddressField('服务器ip',protocol='ipv4',unpack_ipv4=False)
# 	username = models.CharField('用户名',max_length=20,default="NULL")
# 	fromip = models.GenericIPAddressField('来源ip',protocol='ipv4',unpack_ipv4=False)
# 	indoorip = models.GenericIPAddressField('内部ip',protocol='ipv4',unpack_ipv4=False)
# 	userlogintime = models.CharField('登录时间',max_length=30,default="NULL")
# 	useruptime = models.CharField('在线时长',max_length=15,default="NULL")

class ServerList(models.Model):
	serverip = models.GenericIPAddressField('服务器ip',protocol='ipv4',unpack_ipv4=False)
	serverdomain = models.CharField('服务器域名',max_length=30,default="NULL")
	enable = models.BooleanField('启用',default=True)

class RadUserList(models.Model):
	username = models.CharField('用户名',max_length=20,default="NULL")
	attribute = models.CharField('认证', max_length=19, default="Crypt-Password")
	op = models.CharField('认证2', max_length=2, default=":=")
	value = models.CharField('密码', max_length=64, default="NeusoftOpenVpn.Nss@A3-200OK")

class RadUserGroup(models.Model):
	username = models.CharField('用户名',max_length=20,default="NULL")
	groupname = models.CharField('组',max_length=20,default="vpnuser")
	priority = models.IntegerField('priority',default=1)

class UserLoginHistory(models.Model):
	serverip = models.GenericIPAddressField('服务器ip',protocol='ipv4',unpack_ipv4=False)
	username = models.CharField('用户名', max_length=20, default="NULL")
	fromip = models.GenericIPAddressField('来源ip', protocol='ipv4', unpack_ipv4=False)
	indoorip = models.GenericIPAddressField('内部ip', protocol='ipv4', unpack_ipv4=False)
	userlogintime = models.CharField('登录时间', max_length=50, default="NULL")
	userlogouttime = models.CharField('下线时间', max_length=50, default="NULL")
	useruptime = models.CharField('在线时长', max_length=10, default="NULL")

class RadGroupCheck(models.Model):
    groupname = models.CharField(max_length=64)
    attribute = models.CharField(max_length=64)
    op = models.CharField(max_length=2)
    value = models.CharField(max_length=253)

class RadGroupReply(models.Model):
    groupname = models.CharField(max_length=64)
    attribute = models.CharField(max_length=64)
    op = models.CharField(max_length=2)
    value = models.CharField(max_length=253)

class RadPostAuth(models.Model):
    id = models.BigAutoField(primary_key=True)
    username = models.CharField(max_length=253)
    password = models.CharField(db_column='pass', max_length=128, blank=True, null=True)  # Field renamed because it was a Python reserved word.
    reply = models.CharField(max_length=32, blank=True, null=True)
    calledstationid = models.CharField(max_length=50, blank=True, null=True)
    callingstationid = models.CharField(max_length=50, blank=True, null=True)
    authdate = models.DateTimeField()

class RadAcct(models.Model):
    radacctid = models.BigAutoField(primary_key=True)
    acctsessionid = models.CharField(max_length=64)
    acctuniqueid = models.CharField(unique=True, max_length=32)
    username = models.CharField(max_length=253, blank=True, null=True)
    groupname = models.CharField(max_length=253, blank=True, null=True)
    realm = models.CharField(max_length=64, blank=True, null=True)
    nasipaddress = models.GenericIPAddressField()
    nasportid = models.CharField(max_length=15, blank=True, null=True)
    nasporttype = models.CharField(max_length=32, blank=True, null=True)
    acctstarttime = models.DateTimeField(blank=True, null=True)
    acctstoptime = models.DateTimeField(blank=True, null=True)
    acctsessiontime = models.BigIntegerField(blank=True, null=True)
    acctauthentic = models.CharField(max_length=32, blank=True, null=True)
    connectinfo_start = models.CharField(max_length=50, blank=True, null=True)
    connectinfo_stop = models.CharField(max_length=50, blank=True, null=True)
    acctinputoctets = models.BigIntegerField(blank=True, null=True)
    acctoutputoctets = models.BigIntegerField(blank=True, null=True)
    calledstationid = models.CharField(max_length=50, blank=True, null=True)
    callingstationid = models.CharField(max_length=50, blank=True, null=True)
    acctterminatecause = models.CharField(max_length=32, blank=True, null=True)
    servicetype = models.CharField(max_length=32, blank=True, null=True)
    xascendsessionsvrkey = models.CharField(max_length=10, blank=True, null=True)
    framedprotocol = models.CharField(max_length=32, blank=True, null=True)
    framedipaddress = models.GenericIPAddressField(blank=True, null=True)
    acctstartdelay = models.IntegerField(blank=True, null=True)
    acctstopdelay = models.IntegerField(blank=True, null=True)

class Radreply(models.Model):
    username = models.CharField(max_length=64)
    attribute = models.CharField(max_length=64)
    op = models.CharField(max_length=2)
    value = models.CharField(max_length=253)