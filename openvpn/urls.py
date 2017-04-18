from django.conf.urls import url
from openvpn import views

urlpatterns = [
	url(r'^manage/status$',views.status_view,name='status'),
	url(r'^manage/index$',views.index_view,name='index'),
	url(r'^manage/user/add$',views.adduser,name='adduser'),
	url(r'^manage/status.json$',views.status_json,name='status.json'),
	url(r'^manage/addguser$', views.manage_view, name='addguser'),
	url(r'^manage/deluser$', views.manage_view, name='deluser'),
	url(r'^manage/delguser$', views.manage_view, name='delguser'),
	url(r'^manage/delgroup$', views.manage_view, name='delgroup'),
	url(r'^manage',views.manage_view,name='manage'),
]