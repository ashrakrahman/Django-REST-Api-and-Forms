from info.models import Product
from rest_framework import serializers
from rest_framework.serializers import ModelSerializer

class ProducrSerializer (ModelSerializer):
    class Meta:
        model = Product
        fields = [
            'product_name',
            'product_description',
            'product_price',
        ]