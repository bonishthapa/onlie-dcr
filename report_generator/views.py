from rest_framework import generics, status
from rest_framework.response import Response
from report_generator.models import LeaveReport, AdminReport, DailyCallReport, DcrHigher, SalesReport
from report_generator.serializers import LeaveReportSerializer, AdminReportSerializer, DailyCallReportSerializer, DCRHigherSerializer, SalesReportSerializer
from rest_framework.permissions import AllowAny
from django.views.decorators.cache import cache_page
from django.utils.decorators import method_decorator

class LeaveReportListView(generics.ListAPIView):
    queryset = LeaveReport.objects.all()
    serializer_class = LeaveReportSerializer
    permission_classes = [AllowAny,]

    # @method_decorator(cache_page(60*60*2))
    # def get(self, *args, **kwargs):
    #     return super().get(*args, **kwargs)


class LeaveReportCreateView(generics.CreateAPIView):
    queryset = LeaveReport.objects.all()
    serializer_class = LeaveReportSerializer

    def create(self, request, **kwargs):
        if self.request.user.is_verified:
            serializer = LeaveReportSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save(report_initiator=request.user)
                return Response(serializer.data, status.HTTP_201_CREATED)


class LeaveReportDetailView(generics.RetrieveAPIView):
    queryset = LeaveReport.objects.all()
    serializer_class = LeaveReportSerializer
    lookup_field = 'pk'
    permission_classes = [AllowAny,]

    # @method_decorator(cache_page(60*60*2))
    # def get(self, *args, **kwargs):
    #     return super().get(*args, **kwargs)

class LeaveReportUpdateView(generics.UpdateAPIView):
    queryset = LeaveReport.objects.all()
    serializer_class = LeaveReportSerializer
    lookup_field = 'pk'

    def update(self, request, **kwargs):
        if self.request.user.is_verified:
            partial = kwargs.pop('partial', False)
            instance = self.get_object()
            serializer = LeaveReportSerializer(instance, data=request.data, partial=partial)
            if serializer.is_valid():
                serializer.save(updated_by=request.user)
                return Response(serializer.data, status.HTTP_201_CREATED)


class LeaveReportDeleteView(generics.DestroyAPIView):
    queryset = LeaveReport.objects.all()
    serializer_class = LeaveReportSerializer
    lookup_field = 'pk'


class AdminReportListView(generics.ListAPIView):
    queryset = AdminReport.objects.all()
    serializer_class = AdminReportSerializer
    permission_classes = [AllowAny,]

    # @method_decorator(cache_page(60*60*2))
    # def get(self, *args, **kwargs):
    #     return super().get(*args, **kwargs)


class AdminReportCreateView(generics.CreateAPIView):
    queryset = AdminReport.objects.all()
    serializer_class = AdminReportSerializer

    def create(self, request, **kwargs):
        if self.request.user.is_verified:
            serializer = AdminReportSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save(report_writer=request.user)
                return Response(serializer.data, status.HTTP_201_CREATED)


class AdminReportDetailView(generics.RetrieveAPIView):
    queryset = AdminReport.objects.all()
    serializer_class = AdminReportSerializer
    permission_classes = [AllowAny,]
    lookup_field = 'pk'

    # @method_decorator(cache_page(60*60*2))
    # def get(self, *args, **kwargs):
    #     return super().get(*args, **kwargs)


class AdminReportUpdateView(generics.UpdateAPIView):
    queryset = AdminReport.objects.all()
    serializer_class = AdminReportSerializer
    lookup_field = 'pk'

    def update(self, request, **kwargs):
        if self.request.user.is_verified:
            partial = kwargs.pop('partial', False)
            instance = self.get_object()
            serializer = AdminReportSerializer(instance, data=request.data, partial=partial)
            if serializer.is_valid():
                serializer.save(updated_by=request.user)
                return Response(serializer.data, status.HTTP_201_CREATED)


class AdminReportDeleteView(generics.DestroyAPIView):
    queryset = AdminReport.objects.all()
    serializer_class = AdminReportSerializer
    lookup_field = 'pk'

class DailyCallReportListView(generics.ListAPIView):
    queryset = DailyCallReport.objects.all()
    serializer_class = DailyCallReportSerializer
    permission_classes = [AllowAny,]

    # @method_decorator(cache_page(60*60*2))
    # def get(self, *args, **kwargs):
    #     return super().get(*args, **kwargs)

class DailyCallReportCreateView(generics.CreateAPIView):
    queryset = DailyCallReport.objects.all()
    serializer_class = DailyCallReportSerializer

class DailyCallReportDetailView(generics.RetrieveAPIView):
    queryset = DailyCallReport.objects.all()
    serializer_class = DailyCallReportSerializer
    permission_classes = [AllowAny,]
    lookup_field = 'pk'

    # @method_decorator(cache_page(60*60*2))
    # def get(self, *args, **kwargs):
    #     return super().get(*args, **kwargs)

class DailyCallReportUpdateView(generics.UpdateAPIView):
    queryset = DailyCallReport.objects.all()
    serializer_class = DailyCallReportSerializer
    lookup_field = 'pk'

class DailyCallReportDeleteView(generics.DestroyAPIView):
    queryset = DailyCallReport.objects.all()
    serializer_class = DailyCallReportSerializer
    lookup_field = 'pk'                


class DCRHigherListView(generics.ListAPIView):
    queryset = DcrHigher.objects.all()
    serializer_class = DCRHigherSerializer
    permission_classes = [AllowAny,]

    # @method_decorator(cache_page(60*60*2))
    # def get(self, *args, **kwargs):
    #     return super().get(*args, **kwargs)

class DCRHigherCreateView(generics.CreateAPIView):
    queryset = DcrHigher.objects.all()
    serializer_class = DCRHigherSerializer

class DCRHigherDetailView(generics.RetrieveAPIView):
    queryset = DcrHigher.objects.all()
    serializer_class = DCRHigherSerializer
    permission_classes = [AllowAny,]
    lookup_field ='pk'

    # @method_decorator(cache_page(60*60*2))
    # def get(self, *args, **kwargs):
    #     return super().get(*args, **kwargs)

class DCRHigherUpdateView(generics.UpdateAPIView):
    queryset = DcrHigher.objects.all()
    serializer_class = DCRHigherSerializer
    lookup_field ='pk'

    def update(self, request, **kwargs):
       if self.request.user.is_verified:
            partial = kwargs.pop('partial', False)
            instance = self.get_object()
            serializer = DCRHigherSerializer(instance,data=request.data, partial=partial)
            if serializer.is_valid():
               serializer.save(updated_by=request.user)
               return Response(serializer.data, status.HTTP_201_CREATED)


class DCRHigherDeleteView(generics.DestroyAPIView):
    queryset = DcrHigher.objects.all()
    serializer_class = DCRHigherSerializer                   
    lookup_field ='pk'    


class SalesReportListView(generics.ListAPIView):
    queryset = SalesReport.objects.all()
    serializer_class = SalesReportSerializer
    permission_classes = [AllowAny , ]

    # @method_decorator(cache_page(60*60*2))
    # def get(self, *args, **kwargs):
    #     return super().get(*args, **kwargs)

class SalesReportCreateView(generics.CreateAPIView):
    queryset = SalesReport.objects.all()
    serializer_class = SalesReportSerializer

class SalesReportDetailView(generics.RetrieveAPIView):
    queryset = SalesReport.objects.all()
    serializer_class = SalesReportSerializer
    lookup_field = 'pk'
    permission_classes = [AllowAny , ]

    # @method_decorator(cache_page(60*60*2))
    # def get(self, *args, **kwargs):
    #     return super().get(*args, **kwargs)

class SalesReportUpdateView(generics.UpdateAPIView):
    queryset = SalesReport.objects.all()
    serializer_class = SalesReportSerializer
    lookup_field = 'pk'

class SalesReportDeleteView(generics.DestroyAPIView):
    queryset = SalesReport.objects.all()
    serializer_class = SalesReportSerializer
    lookup_field = 'pk'                