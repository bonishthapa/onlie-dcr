from user.models import ClientTable, ClientType, Designation, User, UserControlTable
from rest_framework import serializers


class DesignationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Designation
        fields = ['id','designation_name']


class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only = True, style = {'input_type': 'password'})

    def create(self, validated_data):
        password = validated_data.pop('password')
        user = super().create(validated_data)
        user.set_password(password)
        user.save()
        return user

    class Meta:
        model = User
        fields = ['id', 'email', 'password', 'contact', 'address','designation_name']

class UserControlTableSerializer(serializers.ModelSerializer):
    supervisor = UserSerializer()
    supervised = UserSerializer()
    class Meta:
        model = UserControlTable
        fields = ['id','supervisor','supervised']

class ClientTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = ClientType
        fields = ['id', 'client_type_name']


class ClientTableSerializer(serializers.ModelSerializer):
    client_type_id = ClientTypeSerializer()
    user_id = UserSerializer()
    updated_by = UserSerializer()

    class Meta:
        model = ClientTable
        fields = ['id', 'name', 'address', 'contact_no', 'date_of_birth',
                  'anniversary_date', 'occupation', 'client_type_id', 'user_id', 'updated_by', 'updated_date']
        # read_only_fields = ['user_id','updated_by']          
