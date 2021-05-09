from rest_framework import generics, status
from rest_framework.response import Response
from dcr_system.models import ProductInformation, ProductType
from dcr_system.serializers import ProductInformationSerializer, ProductTypeSerializer
from rest_framework.permissions import AllowAny
from django.views.decorators.cache import cache_page
from django.utils.decorators import method_decorator

class ProductTypeListView(generics.ListAPIView):
    queryset = ProductType.objects.all()
    serializer_class = ProductTypeSerializer
    permission_classes = [AllowAny,]

    # @method_decorator(cache_page(60*60*2))
    # def get(self, *args, **kwargs):
    #     return super().get(*args, **kwargs)

class ProductTypeCreateView(generics.CreateAPIView):
    queryset = ProductType.objects.all()
    serializer_class = ProductTypeSerializer

class ProductTypeDetailView(generics.RetrieveAPIView):
    queryset = ProductType.objects.all()
    serializer_class = ProductTypeSerializer
    permission_classes = [AllowAny,]
    lookup_field = 'pk'

    # @method_decorator(cache_page(60*60*2))
    # def get(self, *args, **kwargs):
    #     return super().get(*args, **kwargs)

class ProductTypeUpdateView(generics.UpdateAPIView):
    queryset = ProductType.objects.all()
    serializer_class = ProductTypeSerializer
    permission_classes = [AllowAny,]
    lookup_field = 'pk'

class ProductTypeDestroyView(generics.DestroyAPIView):
    queryset = ProductType.objects.all()
    serializer_class = ProductTypeSerializer
    lookup_field = 'pk'


class ProductInformationListView(generics.ListAPIView):
    queryset = ProductInformation.objects.all()
    serializer_class = ProductInformationSerializer
    permission_classes = [AllowAny,]

    # @method_decorator(cache_page(60*60*2))
    # def get(self, *args, **kwargs):
    #     return super().get(*args, **kwargs)

class ProductInformationCreateView(generics.CreateAPIView):
    queryset = ProductInformation.objects.all()
    serializer_class = ProductInformationSerializer

class ProductInformationDetailView(generics.RetrieveAPIView):
    queryset = ProductInformation.objects.all()
    serializer_class = ProductInformationSerializer
    permission_classes = [AllowAny,]
    lookup_field = 'pk'

    # @method_decorator(cache_page(60*60*2))
    # def get(self, *args, **kwargs):
    #     return super().get(*args, **kwargs)

class ProductInformationUpdateView(generics.UpdateAPIView):
    queryset = ProductInformation.objects.all()
    serializer_class = ProductInformationSerializer
    lookup_field = 'pk'

class ProductInformationDeleteView(generics.DestroyAPIView):
    queryset = ProductInformation.objects.all()
    serializer_class = ProductInformationSerializer
    lookup_field = 'pk'

