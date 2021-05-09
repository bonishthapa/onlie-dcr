from rest_framework import serializers
from dcr_system.models import ProductInformation, ProductType

class ProductInformationSerializer(serializers.ModelSerializer):

    class Meta:
        model = ProductInformation
        fields = ['id','product_name','product_price','product_type']

class ProductTypeSerializer(serializers.ModelSerializer):

    product_type = ProductInformationSerializer(many=True,read_only=True)
    class Meta:
        model =ProductType
        fields = ['id','product_type_name','product_type']

