from django.conf.urls import url,include
from . import views

urlpatterns = [
        url (r'^$', views.product, name='product'),
        url(r'^register/',include('register.urls')),

]