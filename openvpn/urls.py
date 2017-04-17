from django.conf.urls import url
from openvpn import views

urlpatterns = [
    url(r'^status$',views.status_view,name='status'),
]