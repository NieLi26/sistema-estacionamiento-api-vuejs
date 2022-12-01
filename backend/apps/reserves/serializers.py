from rest_framework import serializers
from datetime import date
from django.db.models import Q

from .models import Lot, Fare, Reserve, Payment, ReservePeriod, FarePeriod, Client

class LotSerializer(serializers.ModelSerializer):
    # Para el related_name debe ser asi
    reserves = serializers.StringRelatedField(many=True) 
    periods = serializers.StringRelatedField(many=True) 
    class Meta:
        model = Lot
        fields = ('id', 'name', 'status', 'type', 'reserves', 'periods')

class ClientSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Client
        fields = ('id', 'first_name', 'last_name', 'document_number', 'social_reason', 'adress', 'phone', 'email')

class FareSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Fare
        fields = ('id', 'name', 'price')

class ReserveSerializer(serializers.ModelSerializer):
    """ Validar  checkin y checkout"""
    class Meta:
        model = Reserve
        fields = ('id', 'lot', 'status', 'fare', 'licence', 'check_in', 'check_out', 'obs')

    def validate_lot(self, value):
        lots = Lot.objects.filter(status=Lot.Status.AVAIBLE).values_list('id', flat=True)
        status = self.context.get('status', '')
        if not self.instance: 
            # checkin: evita reservar el estacionamiento 2 veces al mismo tiempo
            if value.id not in lots and status == '':
                raise serializers.ValidationError('Este estacionamiento esta en uso')
        # checkout: evita anulación, luego de haber finalizado reserva y crear pago
        if value.id in lots and status == 'an':
                raise serializers.ValidationError('Esta reserva ha terminado')
        return value
    
class FarePeriodSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = FarePeriod
        fields = ('id', 'name', 'price')

class ReservePeriodSerializer(serializers.ModelSerializer):

    class Meta:
        model = ReservePeriod
        fields = ('id', 'lot', 'status', 'fare_period', 'licence', 'check_in', 'check_out', 'obs', 'client')

    def validate_lot(self, value):
        lots = Lot.objects.filter(status=Lot.Status.AVAIBLE).values_list('id', flat=True)
        status = self.context.get('status', '')
        # indica que es una actualizacion porque existe el id
        if not self.instance: 
            # checkin: evita reservar el estacionamiento 2 veces al mismo tiempo
            if value.id not in lots and status == '':
                raise serializers.ValidationError('Este estacionamiento esta en uso')
        # checkout: evita anulación, luego de haber finalizado reserva y crear pago
        if value.id in lots and status == 'an':
                raise serializers.ValidationError('Esta reserva ha terminado')
        return value

    def validate_status(self, value):
        if self.instance:
            if self.instance.status == 'an' and value == 'fi':
                    raise serializers.ValidationError('Esta reserva ha sido anulada')
        return value


    # def validate_check_in(self, value):
    #     check_out = self.validate_check_out(self.context.get('check_out', ''))
    #     if ReservePeriod.objects.filter(
    #         Q(check_in__range=(value, check_out), status=ReservePeriod.Status.RESERVED) |
    #         Q(check_in__range=(value, check_out), status=ReservePeriod.Status.INITIATE) ):
    #         raise serializers.ValidationError('Esta fecha esta ocupada')
    #     return value

    def create(self, validated_data): # validated data me trae la data validada y las  instancias de las relaciones
        print(validated_data)
        check_in = validated_data.get('check_in').date()
        check_out = validated_data.get('check_out').date()
        diff = (check_out - check_in).days
        fare_period= validated_data.get('fare_period').price
        total = diff * fare_period
        return ReservePeriod.objects.create(**validated_data, total=total)

    def update(self, instance, validated_data): # validated data me trae la data validada y las  instancias de las relaciones
        print(validated_data)
        check_in = validated_data.get('check_in', instance.check_in).date()
        check_out = validated_data.get('check_out', instance.check_out).date()
        diff = (check_out - check_in).days
        fare_period= validated_data.get('fare_period').price
        total = diff * fare_period
        instance.total = total
        instance.save()
        return super().update(instance, validated_data)


    def to_representation(self, instance):
        data = super().to_representation(instance)
        data['status'] = instance.get_status_display()
        data['lot'] = {
            'id':instance.lot.id,
            'name':instance.lot.name,
            'status':instance.lot.status,
            'type':instance.lot.type
        }
        data['total'] = instance.total
        data['fare_period'] = {
            'id': instance.fare_period.id, 
            'name': instance.fare_period.name
        }
        data['client'] = {
            'id': instance.client.id,
            'first_name': instance.client.first_name,
            'last_name': instance.client.last_name,
            'document_number': instance.client.document_number,
            'social_reason': instance.client.social_reason,
            'adress': instance.client.adress,
            'phone': instance.client.phone,
            'email': instance.client.email
        }
        return data

class CheckOutSerializer(serializers.ModelSerializer):
    lot = LotSerializer() # si se tiene es solo para mostrar, pq si crearamos con esto en el serializer, pediria el objeto completo no solo el id
    fare = FareSerializer()

    class Meta:
        model = Reserve
        fields = ('id', 'lot', 'status', 'fare', 'licence', 'check_in', 'check_out')

class PaymentSerializer(serializers.ModelSerializer):
    """ Validamos reserva antes de generar pago"""
    class Meta:
        model = Payment
        fields = ('id', 'reserve', 'number', 'total', 'created_at')

    def to_representation(self, instance):
        data =  super().to_representation(instance)
        data['licence'] = instance.reserve.licence
        return data

    def validate_reserve(self, value):
        reserve_list = Reserve.objects.all()
        reserve_list_anulled = reserve_list.filter(status=Reserve.Status.ANULLED).values_list('id', flat=True)
        # checkout: evitar finalizar reserva y crear pago, luego de haber realizado anulación
        if value.id in reserve_list_anulled:
                raise serializers.ValidationError('Esta reserva ha sido anulada')
        reserve_list_finished = reserve_list.filter(status=Reserve.Status.FINISHED).values_list('id', flat=True)
        if value.id in reserve_list_finished:
                raise serializers.ValidationError('Esta reserva ha terminado')
        return value