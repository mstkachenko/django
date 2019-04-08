from rest_framework.serializers import (
    ModelSerializer, SerializerMethodField
)

from products.models import Product
from datetime import datetime

class ProductSerializer(ModelSerializer):
    category = SerializerMethodField()
    #is_pure = SerializerMethodField()
    is_new = SerializerMethodField()

    class Meta:
        model = Product
        fields = (
           'url', 'name', 'image', 'category', 
            'description', 'cost', 'is_new'
        )
    def get_category(self, obj):
        if obj.category:
            return obj.category.name
        
    # def get_is_pure(self,obj):
    #     return obj.created == obj.modified
    def get_is_new(self,obj):
        return obj.created.date() == datetime.now().date()