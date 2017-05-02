from django.conf.urls import url
from . import views

urlpatterns = [
        #url (r'^$', views.register, name='register'),
        url (r'^$', views.register_user, name='register_user'),

]