from rest_framework import serializers
from report_generator.models import LeaveReport, AdminReport, DcrHigher,DailyCallReport, SalesReport
from user.serializers import UserSerializer, ClientTableSerializer, ClientTypeSerializer
from dcr_system.serializers import ProductInformationSerializer

class LeaveReportSerializer(serializers.ModelSerializer):
    report_initiator = UserSerializer()
    report_reciever = UserSerializer()
    updated_by = UserSerializer()

    class Meta:
        model = LeaveReport
        fields = ['id', 'report_initiator', 'report_reciever', 'subject',
                  'status1', 'status2', 'updated_by', 'updated_date']
        # read_only_fields = ['report_initiator','updated_by']           

class AdminReportSerializer(serializers.ModelSerializer):
    report_writer = ClientTableSerializer()
    updated_by = UserSerializer()
    report_supervisor = UserSerializer()

    class Meta:
        model = AdminReport
        fields = ['id', 'report_writer', 'subject', 'report_supervisor', 'status1', 'status2',
                  'updated_by', 'updated_date']
        # read_only_fields = ['report_writer','updated_by']     

class DailyCallReportSerializer(serializers.ModelSerializer):
    client_type = ClientTypeSerializer()
    client_name = ClientTableSerializer()
    product = ProductInformationSerializer()
    mpo_id = UserSerializer()
    visited_with = UserSerializer()
    sample = ProductInformationSerializer()

    class Meta:
        model = DailyCallReport
        fields = ['id','shift','visited_area','client_type','client_name','gift','product',
                    'quantity','amount','mpo_id','dcr_date','created_date','visited_with','sample','sample_qty']


class DCRHigherSerializer(serializers.ModelSerializer):
    supervised_id = UserSerializer()
    dcr_id = DailyCallReportSerializer()
    updated_by = UserSerializer()

    class Meta:
        model = DcrHigher
        fields = ['id','date','supervised_id','dcr_id','updated_by','updated_date']
        # read_only_fields = ['updated_by']             

class SalesReportSerializer(serializers.ModelSerializer):
    client_name = ClientTableSerializer()
    product = ProductInformationSerializer()
    sales_person = UserSerializer()
    updated_by = UserSerializer()

    class Meta:
        model = SalesReport
        fields =['id','date','client_name','address','product',
                    'qunatity','sales_person','updated_by','updated_date']