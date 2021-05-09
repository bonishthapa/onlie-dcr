from django.shortcuts import render
from salary_expenses.serializers import SalaryExpensesSerializer
from salary_expenses.models import SalaryExpense
from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from django.views.decorators.cache import cache_page
from django.utils.decorators import method_decorator


class SalaryExpensesListView(generics.ListAPIView):
    queryset = SalaryExpense.objects.all()
    serializer_class = SalaryExpensesSerializer
    permission_classes = [AllowAny,]

    # @method_decorator(cache_page(60*60*2))
    # def get(self, *args, **kwargs):
    #     return super().get(*args, **kwargs)


class SalaryExpensesCreateView(generics.CreateAPIView):
    queryset = SalaryExpense.objects.all()
    serializer_class = SalaryExpensesSerializer

    def create(self, request, **kwargs):
        if self.request.user.is_verified:
            serializer = SalaryExpensesSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save(created_by=request.user)
                return Response(serializer.data, status.HTTP_201_CREATED)


class SalaryExpensesDetailView(generics.RetrieveAPIView):
    queryset = SalaryExpense.objects.all()
    serializer_class = SalaryExpensesSerializer
    permission_classes = [AllowAny,]
    lookup_field = 'pk'

    # @method_decorator(cache_page(60*60*2))
    # def get(self, *args, **kwargs):
    #     return super().get(*args, **kwargs)


class SalaryExpensesUpdateView(generics.UpdateAPIView):
    queryset = SalaryExpense.objects.all()
    serializer_class = SalaryExpensesSerializer
    lookup_field = 'pk'

    def update(self, request, **kwargs):
        if self.request.user.is_verified:
            partial = kwargs.pop('partial', False)
            instance = self.get_object()
            print(instance)
            serializer = SalaryExpensesSerializer(instance, data=request.data, partial=partial)
            if serializer.is_valid():
                serializer.save(updated_by=request.user)
                return Response(serializer.data, status.HTTP_201_CREATED)


class SalaryExpensesDeleteView(generics.DestroyAPIView):
    queryset = SalaryExpense.objects.all()
    serializer_class = SalaryExpensesSerializer
    lookup_field = 'pk'