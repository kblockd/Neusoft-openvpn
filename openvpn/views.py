# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

import json
from django.core.serializers.json import DjangoJSONEncoder
from django.core.paginator import Paginator
from django.core.paginator import PageNotAnInteger
from django.core.paginator import EmptyPage

#from django.views.generic.detail import DetailView

# Create your views here.

def status_json(request):
	from openvpn.control import status
	p = status()
	return render(request, 'openvpn/status.json',{'json':json.dumps(list(p), cls=DjangoJSONEncoder)}, content_type="application/json")

def index_view(request):
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
	return render(request, 'openvpn/index.html', {'status':topics}, content_type='text/html')

def status_view(request):
	from openvpn.control import status
	p = status()
	return render(request, 'openvpn/status.html', {'status':p}, content_type='text/html')

def manage_view(request):
	return render(request, 'openvpn/manage.html', {}, content_type='text/html')

def adduser(request):
	return render(request, 'openvpn/add.html', {'action': '233'},content_type='text/html')

def addgroup(request):
	return render(request, 'openvpn/action.html', {'action': request.POST['action'].encode('utf-8')},content_type='text/html')

def addguser(request):
	return render(request, 'openvpn/action.html', {'action': request.POST['action'].encode('utf-8')},content_type='text/html')

def deluser(request):
	return render(request, 'openvpn/action.html', {'action': request.POST['action'].encode('utf-8')},content_type='text/html')

def delguser(request):
	return render(request, 'openvpn/action.html', {'action': request.POST['action'].encode('utf-8')},content_type='text/html')

def delgroup(request):
	return render(request, 'openvpn/action.html', {'action': request.POST['action'].encode('utf-8')},content_type='text/html')
