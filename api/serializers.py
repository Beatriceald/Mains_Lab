from rest_framework import serializers
from .models import *

class ClientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Client
        fields = ('name',)

class OrganizationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Client
        fields = ('client_name', 'name', 'address')

class BillsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Biils
        fields = ('client_name', 'client_org', 'number', 'sum', 'date', 'service')