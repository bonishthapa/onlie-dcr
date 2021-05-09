from user.serializers import ClientTableSerializer, ClientTypeSerializer, DesignationSerializer, UserSerializer, UserControlTableSerializer
from user.models import Designation, ClientTable, ClientType, User, UserControlTable
from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from rest_framework import filters
from django.views.decorators.cache import cache_page
from django.utils.decorators import method_decorator
from django.http import HttpResponse


def home(request):
    return  HttpResponse("Welcome")

class DesignationListView(generics.ListAPIView):
    queryset = Designation.objects.all()
    serializer_class = DesignationSerializer
    permission_classes = [AllowAny, ]
    filter_backends = [filters.SearchFilter]
    search_fields = ['designation_name']


    # @method_decorator(cache_page(60*60*2))
    # def get(self, *args, **kwargs):
    #     print("Cached data")
    #     return super().get(*args, **kwargs)

    # def get_search_fields(self, view, request):
    #     print('hello')
    #     if request.query_params.get('desognation_name'):
    #         return ['designation_name']
    #     return super(CustomSearchFilter, self).get_search_fields(view, request)

class DesignationCreateView(generics.CreateAPIView):
    queryset = Designation.objects.all()
    serializer_class = DesignationSerializer


class DesignationUpdateView(generics.UpdateAPIView):
    queryset = Designation.objects.all()
    serializer_class = DesignationSerializer
    lookup_field = 'pk'


class DesignationDetailView(generics.RetrieveAPIView):
    queryset = Designation.objects.all()
    serializer_class = DesignationSerializer
    permission_classes = [AllowAny, ]


class DesignationDeleteView(generics.DestroyAPIView):
    queryset = Designation.objects.all()
    serializer_class = DesignationSerializer


class UserListView(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [AllowAny, ]
    filter_backends = [filters.SearchFilter]
    search_fields = ['email']

    # @method_decorator(cache_page(60*60*2))
    # def get(self, *args, **kwargs):
    #     print("Cached data")
    #     return super().get(*args, **kwargs)


class UserDetailView(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [AllowAny, ]
    lookup_field = 'pk'


class UserCreateView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [AllowAny,]


class UserUpdateView(generics.UpdateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    lookup_field = 'pk'


class UserDeleteView(generics.DestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class ClientTypeListView(generics.ListAPIView):
    queryset = ClientType.objects.all()
    serializer_class = ClientTypeSerializer
    permission_classes = [AllowAny, ]
    filter_backends = [filters.SearchFilter]
    search_fields = ['client_type']

    @method_decorator(cache_page(60*60*2))
    def get(self, *args, **kwargs):
        print("Cached data")
        return super().get(*args, **kwargs)

class ClientTypeDetailView(generics.RetrieveAPIView):
    queryset = ClientType.objects.all()
    serializer_class = ClientTypeSerializer
    lookup_field = 'pk'
    permission_classes = [AllowAny,]


class ClientTypeCreateView(generics.CreateAPIView):
    queryset = ClientType.objects.all()
    serializer_class = ClientTypeSerializer


class ClientTypeUpdateView(generics.UpdateAPIView):
    queryset = ClientType.objects.all()
    serializer_class = ClientTypeSerializer
    lookup_field = 'pk'


class ClientTypeDeleteView(generics.DestroyAPIView):
    queryset = ClientType.objects.all()
    serializer_class = ClientTypeSerializer


class ClientTableListView(generics.ListAPIView):
    serializer_class = ClientTableSerializer
    queryset = ClientTable.objects.all()
    permission_classes = [AllowAny, ]
    filter_backends = [filters.SearchFilter]
    search_fields = ['client_name']

    # @method_decorator(cache_page(60*60*2))
    # def get(self, *args, **kwargs):
    #     return super().get(*args, **kwargs)


class ClientTableDetailView(generics.RetrieveAPIView):
    serializer_class = ClientTableSerializer
    queryset = ClientTable.objects.all()
    permission_classes = [AllowAny, ]
    lookup_field = 'pk'
    
    # @method_decorator(cache_page(60*60*2))
    # def get(self, *args, **kwargs):
    #     return super().get(*args, **kwargs)


class ClientTableCreateView(generics.CreateAPIView):
    serializer_class = ClientTableSerializer
    queryset = ClientTable.objects.all()

    def create(self, request, **kwargs):
        if self.request.user.is_verified:
            serializer = ClientTableSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save(user_id=request.user)
                return Response(serializer.data)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ClientTableUpdateView(generics.UpdateAPIView):
    serializer_class = ClientTableSerializer
    queryset = ClientTable.objects.all()
    lookup_field = 'pk'

    def update(self, request, **kwargs):
        if self.request.user.is_verified:
            partial = kwargs.pop('partial', False)
            instance = self.get_object()
            serializer = ClientTableSerializer(instance, data=request.data, partial=partial)
            if serializer.is_valid():
                serializer.save(updated_by=request.user)
                return Response(serializer.data)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)    


class ClientTableDeleteView(generics.DestroyAPIView):
    serializer_class = ClientTableSerializer
    queryset = ClientTable.objects.all()


class UserControlTableListView(generics.ListAPIView):
    queryset = UserControlTable.objects.all()
    serializer_class = UserControlTableSerializer
    permission_classes = [AllowAny, ]

    # @method_decorator(cache_page(60*60*2))
    # def get(self, *args, **kwargs):
    #     return super().get(*args, **kwargs)

class UserControlTableCreateView(generics.CreateAPIView):
    queryset = UserControlTable.objects.all()
    serializer_class = UserControlTableSerializer
    permission_classes = [AllowAny, ]
    lookup_field = 'pk'


class UserControlTableDetailView(generics.RetrieveAPIView):
    queryset = UserControlTable.objects.all()
    serializer_class = UserControlTableSerializer
    lookup_field = 'pk'

    @method_decorator(cache_page(60*60*2))
    def get(self, *args, **kwargs):
        return super().get(*args, **kwargs)


class UserControlTableUpdateView(generics.UpdateAPIView):
    queryset = UserControlTable.objects.all()
    serializer_class = UserControlTableSerializer
    lookup_field = 'pk'


class UserControlTableDeleteView(generics.DestroyAPIView):
    queryset = UserControlTable.objects.all()
    serializer_class = UserControlTableSerializer
    lookup_field = 'pk'
