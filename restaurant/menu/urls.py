from django.conf.urls import url
from . import views

# important inorder to use namespaces in urls
app_name = 'menu'

urlpatterns = [
	url(r'^$', views.index, name="index"),
	url(r'storeDetails', views.storeDetails, name="storeDetails"),
]