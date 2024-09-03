from rest_framework import serializers
from .models import Inventory, Inbound, Outbound

class InventorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Inventory
        fields = '__all__'

class InboundSerializer(serializers.ModelSerializer):
    class Meta:
        model = Inbound
        fields = '__all__'

class OutboundSerializer(serializers.ModelSerializer):
    class Meta:
        model = Outbound
        fields = '__all__'
