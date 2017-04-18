# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

# Create your views here.

def status_view(request):
	from openvpn.control import status
	p = status()
	return render(request, 'openvpn/status.html', {'status':p,'rows':p.count()}, content_type='text/html')

def manage_view(request):
	from openvpn.control import adduser
	if request.method == 'POST':
		if request.POST['action'] == 'adduser':
			return render(request, 'openvpn/adduser.html', {'action':request.POST['action'].encode('utf-8')}, content_type='text/html')
		elif request.POST['action'] == 'addgroup':
			return render(request, 'openvpn/addgroup.html', {'action':request.POST['action'].encode('utf-8')}, content_type='text/html')
		elif request.POST['action'] == 'addguser':
			return render(request, 'openvpn/addguser.html', {'action': request.POST['action'].encode('utf-8')}, content_type='text/html')
		elif request.POST['action'] == 'deluser':
			return render(request, 'openvpn/deluser.html', {'action': request.POST['action'].encode('utf-8')}, content_type='text/html')
		elif request.POST['action'] == 'delguser':
			return render(request, 'openvpn/delguser.html', {'action': request.POST['action'].encode('utf-8')}, content_type='text/html')
		elif request.POST['action'] == 'delgroup':
			return render(request, 'openvpn/delgroup.html', {'action': request.POST['action'].encode('utf-8')}, content_type='text/html')
		else:
			return render(request, 'openvpn/manage.html', {}, content_type='text/html')
	else:
		return render(request, 'openvpn/manage.html', {}, content_type='text/html')