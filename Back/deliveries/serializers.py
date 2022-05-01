from ast import Del
from unicodedata import category
from rest_framework import serializers
from django.contrib.auth import get_user_model
from .models import Delivery, Address, Category, Alarm
from accounts.serializers import UserSerializer

class AddressSerializer(serializers.ModelSerializer):

    class IDeliverySerializer(serializers.ModelSerializer):

        class Meta:
            model = Delivery
            fields = '__all__'
    deliveries = IDeliverySerializer(many=True, read_only=True,)

    class Meta:
        model = Address
        fields = '__all__'

class AlarmSerializer(serializers.ModelSerializer):

    class Meta:
        model = Alarm
        fields = '__all__'

class CategorySerializer(serializers.ModelSerializer):

    class Meta:
        model = Category
        fields = '__all__'

class DeliverySerializer(serializers.ModelSerializer):
    class IAddressSerializer(serializers.ModelSerializer):
        class Meta:
            model = Address
            fields = '__all__'

    category=CategorySerializer(read_only=True,)
    address=IAddressSerializer(read_only=True,)
    user = UserSerializer(read_only=True)

    class Meta:
        model = Delivery
        fields = '__all__'
        # read_only_fields = ('category', 'address')


class CountSerializer(serializers.Serializer):
    all = serializers.SerializerMethodField()
    move = serializers.SerializerMethodField()
    wait = serializers.SerializerMethodField()
    complete = serializers.SerializerMethodField()
    
    
    def get_all(self, obj):
        return obj.delivery_set.count()

    def get_move(self, obj):
        return obj.delivery_set.filter(state="배송").count()

    def get_wait(self, obj):
        return obj.delivery_set.filter(state="대기").count()

    def get_complete(self, obj):
        return obj.delivery_set.filter(state="완료").count()


