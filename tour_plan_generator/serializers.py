from rest_framework import serializers
from tour_plan_generator.models import TourPlan, TourPlanHigher
from user.serializers import UserSerializer

class TourPlanSerializer(serializers.ModelSerializer):
    creator_id = UserSerializer()
    approver_id = UserSerializer()
    updated_by = UserSerializer()
    class Meta:
        model = TourPlan
        fields = ['id', 'date', 'morining_station', 'evening_station', 'morning_station_type',
                  'evening_station_type', 'creator_id', 'approver_id', 'status1', 'status2', 'updated_by',
                  'updated_date']
        read_only_fields = ['creator_id','updated_by']          

class TourPlanHigherSerializer(serializers.ModelSerializer):
    morning_supervised = UserSerializer()
    evening_supervised  = UserSerializer()
    created_by = UserSerializer()
    updated_by = UserSerializer()

    class Meta:
        model = TourPlanHigher
        fields = ['id', 'morning_supervised', 'evening_supervised', 'date', 'created_by',
                  'updated_by', 'updated_date']
        read_only_fields = ['creator_id','updated_by']           