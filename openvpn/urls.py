from django.conf.urls import url
from openvpn import views

urlpatterns = [
	url(r'^manage/status$',views.status_view,name='status'),
    url(r'^manage',views.manage_view,name='manage'),

]