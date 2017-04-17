from django.conf.urls import url
from openvpn import views

urlpatterns = [
    url(r'^pprint$',views.status,name='status'),
]