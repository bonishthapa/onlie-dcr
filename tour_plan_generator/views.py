from rest_framework import generics, status
from rest_framework.response import Response
from tour_plan_generator.serializers import TourPlanSerializer, TourPlanHigherSerializer
from tour_plan_generator.models import TourPlan, TourPlanHigher
from rest_framework.permissions import AllowAny
from django.views.decorators.cache import cache_page
from django.utils.decorators import method_decorator

# Create your views here.

class TourPlanListView(generics.ListAPIView):
    queryset = TourPlan.objects.all()
    serializer_class = TourPlanSerializer
    permission_classes = [AllowAny,]

    # @method_decorator(cache_page(60*60*2))
    # def get(self, *args, **kwargs):
    #     return super().get(*args, **kwargs)


class TourPlanCreateView(generics.CreateAPIView):
    queryset = TourPlan.objects.all()
    serializer_class = TourPlanSerializer

    def create(self, request, **kwargs):
        if self.request.user.is_verified:
            serializer = TourPlanSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save(created_by=request.user)
                return Response(serializer.data, status.HTTP_201_CREATED)


class TourPlanDetailView(generics.RetrieveAPIView):
    queryset = TourPlan.objects.all()
    serializer_class = TourPlanSerializer
    lookup_field = 'pk'
    permission_classes = [AllowAny,]

    # @method_decorator(cache_page(60*60*2))
    # def get(self, *args, **kwargs):
    #     return super().get(*args, **kwargs)

class TourPlanUpdateView(generics.UpdateAPIView):
    queryset = TourPlan.objects.all()
    serializer_class = TourPlanSerializer
    lookup_field = 'pk'

    def update(self, request, **kwargs):
        if self.request.user.is_verified:
            partial = kwargs.pop('partial', False)
            instance = self.get_object()
            print(instance)
            serializer = TourPlanSerializer(instance, data=request.data, partial=partial)
            if serializer.is_valid():
                serializer.save(updated_by=request.user)
                return Response(serializer.data, status.HTTP_201_CREATED)


class TourPlanDeleteView(generics.DestroyAPIView):
    queryset = TourPlan.objects.all()
    serializer_class = TourPlanSerializer
    lookup_field = 'pk'


class TourPlanHigherListView(generics.ListAPIView):
    queryset = TourPlanHigher.objects.all()
    serializer_class = TourPlanHigherSerializer
    permission_classes = [AllowAny,]

    # @method_decorator(cache_page(60*60*2))
    # def get(self, *args, **kwargs):
    #     return super().get(*args, **kwargs)


class TourPlanHigherCreateView(generics.CreateAPIView):
    queryset = TourPlanHigher.objects.all()
    serializer_class = TourPlanHigherSerializer

    def create(self, request, **kwargs):
        if self.request.user.is_verified:
            serializer = TourPlanHigherSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save(creator_id=request.user)
                return Response(serializer.data, status.HTTP_201_CREATED)


class TourPlanHigherDetailView(generics.RetrieveAPIView):
    queryset = TourPlanHigher.objects.all()
    serializer_class = TourPlanHigherSerializer
    permission_classes = [AllowAny,]
    lookup_field = 'pk'

    # @method_decorator(cache_page(60*60*2))
    # def get(self, *args, **kwargs):
    #     return super().get(*args, **kwargs)


class TourPlanHigherUpdateView(generics.UpdateAPIView):
    queryset = TourPlanHigher.objects.all()
    serializer_class = TourPlanHigherSerializer
    lookup_field = 'pk'

    def update(self, request, **kwargs):
        if self.request.user.is_verified:
            partial = kwargs.pop('partial', False)
            instance = self.get_object()
            serializer = TourPlanHigherSerializer(instance, data=request.data, partial=partial)
            if serializer.is_valid():
                serializer.save(updated_by=request.user)
                return Response(serializer.data, status.HTTP_201_CREATED)


class TourPlanHigherDeleteView(generics.DestroyAPIView):
    queryset = TourPlanHigher.objects.all()
    serializer_class = TourPlanHigherSerializer
    lookup_field = 'pk'