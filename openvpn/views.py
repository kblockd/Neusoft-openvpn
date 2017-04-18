# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

from django.views.generic.detail import DetailView

# Create your views here.

def status_view(request):
	from openvpn.control import status
	p = status()
	return render(request, 'openvpn/status.html', {'status':p,'rows':p.count()}, content_type='text/html')

def manage_view(request):
	return render(request, 'openvpn/manage.html', {}, content_type='text/html')

def adduser(request):
	return render(request, 'openvpn/action.html', {'action': request.POST['action'].encode('utf-8')},content_type='text/html')

def addgroup(request):
	return render(request, 'openvpn/action.html', {'action': request.POST['action'].encode('utf-8')},content_type='text/html')

def addguser(request):
	return render(request, 'openvpn/action.html', {'action': request.POST['action'].encode('utf-8')},content_type='text/html')

def deluser(request):
	return render(request, 'openvpn/action.html', {'action': request.POST['action'].encode('utf-8')},content_type='text/html')

def delguser(request):
	return render(request, 'openvpn/action.html', {'action': request.POST['action'].encode('utf-8')},content_type='text/html')

def delgroup(request):
	return render(request, 'openvpn/actioin.html', {'action': request.POST['action'].encode('utf-8')},content_type='text/html')
