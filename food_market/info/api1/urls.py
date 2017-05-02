from django.conf.urls import url
from .views import ProductListApiView

urlpatterns = [
        url (r'^$', ProductListApiView.as_view(), name='product'),

]