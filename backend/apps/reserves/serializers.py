from rest_framework import serializers
from datetime import date

from .models import Lot, Fare, Reserve, Payment, ReservePeriod, FarePeriod, Client

class LotSerializer(serializers.ModelSerializer):
    # Para el related_name debe ser asi
    reserves = serializers.StringRelatedField(many=True) 
    class Meta:
        model = Lot
        fields = ('id', 'name', 'status', 'type', 'reserves')

class ClientSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Client
        fields = ('id', 'first_name', 'last_name', 'document_number', 'social_reason', 'adress', 'phone', 'email')

class FareSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Fare
        fields = ('id', 'name', 'price')

class ReserveSerializer(serializers.ModelSerializer):
    # lot = LotSerializer()
    class Meta:
        model = Reserve
        fields = ('id', 'lot', 'status', 'fare', 'licence', 'check_in', 'check_out', 'obs')

class FarePeriodSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = FarePeriod
        fields = ('id', 'name', 'price')

class ReservePeriodSerializer(serializers.ModelSerializer):

    class Meta:
        model = ReservePeriod
        fields = ('id', 'lot', 'status', 'fare_period', 'licence', 'check_in', 'check_out', 'obs')

    def create(self, validated_data): # validated data me trae la data validada y las  instancias de las relaciones
        print(validated_data)
        check_in = validated_data.get('check_in').date()
        check_out = validated_data.get('check_out').date()
        diff = (check_out - check_in).days
        fare_period= validated_data.get('fare_period').price
        total = diff * fare_period
        return ReservePeriod.objects.create(**validated_data, total=total)

    def to_representation(self, instance):
        data = super().to_representation(instance)
        data['total'] = instance.total
        data['fare_period'] = instance.fare_period.name
        return data

class CheckOutSerializer(serializers.ModelSerializer):
    lot = LotSerializer() # si se tiene es solo para mostrar, pq si crearamos con esto en el serializer, pediria el objeto completo no solo el id
    fare = FareSerializer()

    class Meta:
        model = Reserve
        fields = ('id', 'lot', 'status', 'fare', 'licence', 'check_in', 'check_out')

class PaymentSerializer(serializers.ModelSerializer):

    class Meta:
        model = Payment
        fields = ('id', 'reserve', 'number', 'total', 'created_at')

    def to_representation(self, instance):
        data =  super().to_representation(instance)
        data['licence'] = instance.reserve.licence
        return data