# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

import json,re
from django.core.serializers.json import DjangoJSONEncoder
from django.core.paginator import Paginator,EmptyPage,PageNotAnInteger
from django.contrib import messages

#from django.views.generic.detail import DetailView

# Create your views here.

# def status_json(request):
# 	from openvpn.control import status
# 	p = status()
# 	return render(request, 'openvpn/status.json',{'json':json.dumps(list(p), cls=DjangoJSONEncoder)}, content_type="application/json")

def status_view(request):
	from openvpn.control import status
	p = status()
	paginator = Paginator(p, 20)
	page = request.GET.get('page')
	try:
		topics = paginator.page(page)  # 获取某页对应的记录
	except PageNotAnInteger:  # 如果页码不是个整数
		topics = paginator.page(1)  # 取第一页的记录
	except EmptyPage:  # 如果页码太大，没有相应的记录
		topics = paginator.page(paginator.num_pages)
	return render(request, 'openvpn/status.html', {'status':topics}, content_type='text/html')

# def status_view(request):
# 	from openvpn.control import status
# 	p = status()
# 	return render(request, 'openvpn/status.html', {'status':p}, content_type='text/html')

def manage_view(request):
	return render(request, 'openvpn/manage.html', {}, content_type='text/html')

def adduser(request):
	if request.method == 'POST':
		if 'username' in request.POST and 'groupname' in request.POST and 'password' in request.POST:
			username = request.POST['username']
			password = request.POST['password']
			if request.POST['groupname'] == '':
				groupname = 'user'
			else:
				groupname = request.POST['groupname']

			from openvpn.control import adduser,sqlfilter

			if sqlfilter(username) and sqlfilter(password) and sqlfilter(groupname):
				if adduser(username,password,groupname):
					messages.success(request, '成功添加用户')
					return render(request, 'openvpn/adduser.html', {}, content_type='text/html')
				else:
					messages.error(request, '用户已存在')
					return render(request, 'openvpn/adduser.html', {}, content_type='text/html')
			else:
				messages.error(request, '非法字符')
				return render(request, 'openvpn/adduser.html', {}, content_type='text/html')
		else:
			return render(request, 'openvpn/adduser.html', {}, content_type='text/html')
	else:
		return render(request, 'openvpn/adduser.html', {}, content_type='text/html')

def addgroup(request):
	return render(request, 'openvpn/action.html', {'action': request.POST['action'].encode('utf-8')},content_type='text/html')

# def addguser(request):
# 	if request.method == 'POST':
# 		if 'userlist' in request.POST and 'groupname' in request.POST and 'password' in request.POST:
# 			userlist = request.POST['username']
# 			password = request.POST['password']
# 			if request.POST['groupname'] == '':
# 				groupname = 'user'
# 			else:
# 				groupname = request.POST['groupname']
#
# 			from openvpn.control import adduser,sqlfilter
#
# 			if sqlfilter(password) and sqlfilter(groupname):
# 				for username in userlist.split(','):
# 					if sqlfilter(username):
# 						if adduser(request.POST['username'],request.POST['password'],request.POST['groupname']):
# 							messages.success(request, '成功添加用户')
# 							return render(request, 'openvpn/addguser.html', {}, content_type='text/html')
# 						else:
# 					messages.error(request, '用户已存在')
# 					return render(request, 'openvpn/addguser.html', {}, content_type='text/html')
# 			else:
# 				messages.error(request, '非法字符')
# 				return render(request, 'openvpn/addguser.html', {}, content_type='text/html')
# 		else:
# 			return render(request, 'openvpn/addguser.html', {}, content_type='text/html')
# 	else:
# 		return render(request, 'openvpn/addguser.html', {}, content_type='text/html')
def deluser(request):
	if request.method == 'POST':
		if 'username' in request.POST:
			username = request.POST['username']
			from openvpn.control import deluser
			if sqlfilter(username):
				if deluser(username):
					messages.success(request, '成功删除'+username)
					return render(request, 'openvpn/deluser.html', {}, content_type='text/html')
				else:
					messages.error(request, '用户已存在')
					return render(request, 'openvpn/deluser.html', {}, content_type='text/html')
			else:
				messages.error(request, '非法字符')
				return render(request, 'openvpn/deluser.html', {}, content_type='text/html')
		else:
			return render(request, 'openvpn/deluser.html', {}, content_type='text/html')
	else:
		return render(request, 'openvpn/deluser.html', {}, content_type='text/html')

def delguser(request):
	return render(request, 'openvpn/action.html', {'action': request.POST['action'].encode('utf-8')},content_type='text/html')

def delgroup(request):
	return render(request, 'openvpn/action.html', {'action': request.POST['action'].encode('utf-8')},content_type='text/html')
