from rest_framework.generics import ListAPIView
from info.models import Product
from .serializer import ProducrSerializer

class ProductListApiView (ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProducrSerializer