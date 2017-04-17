# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

# Create your views here.

def status_view(request):
	from openvpn.control import status
	return render(request, 'openvpn/status.html', {'status':status()}, content_type='text/html')