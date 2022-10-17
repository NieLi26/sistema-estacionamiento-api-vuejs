from django.db import models
from django.db.models.signals import post_save
from django.utils import timezone

from apps.base.models import BaseModel
# Create your models here.

class Lot(BaseModel):
    '''Model definition for Lot.'''
    
    class Status(models.TextChoices):
        AVAIBLE = 'av', 'Disponible'
        BUSY = 'bu', 'Ocupado'
        RESERVED = 're', 'Reservado'
        MAINTENANCE = 'ma', 'Mantenimiento'
    
    class Types(models.TextChoices):
        NORMAL = 'no', 'Normal'
        DISABILITY = 'di', 'Discapacitado'
    
    name = models.CharField('Numero', max_length=3)
    status = models.CharField('Estado Estacionamiento', choices=Status.choices, max_length=2)
    type = models.CharField('Tipo Estacionamiento', choices=Types.choices, max_length=2)

    class Meta:
        '''Meta definition for Lot.'''

        ordering = ('created_at', )
        verbose_name = 'Lot'
        verbose_name_plural = 'Lots'

    def __str__(self):
        return self.name

class Fare(BaseModel):
    """Model definition for Fare."""

    name = models.CharField('Nombre', max_length=150)
    price = models.PositiveIntegerField('Precio', default=0)

    class Meta:
        """Meta definition for Tarifa."""

        ordering = ['id']
        verbose_name = 'Fare'
        verbose_name_plural = 'Fares'

    def __str__(self):
        return self.name

class Reserve(BaseModel):

    class Status(models.TextChoices):
        BUSY = 'bu', 'Ocupada'
        FINISHED = 'fi', 'Finalizada'
        ANULLED = 'an', 'Anulada'

    lot = models.ForeignKey(
        Lot, on_delete=models.CASCADE, verbose_name="Estacionamiento", related_name="reserves")
    status = models.CharField(choices=Status.choices, verbose_name="Estado de Reserva", default='bu', max_length=2)
    fare = models.ForeignKey(
        Fare, on_delete=models.CASCADE, verbose_name='Tarifa', default='normal', related_name="reserves")
    licence = models.CharField('Patente', max_length=15)
    check_in = models.DateTimeField('Entrada', auto_now_add=True)
    check_out = models.DateTimeField('Salida',  null=True, blank=True)
    obs = models.TextField(
        max_length=200, blank=True)

    class Meta:

        ordering = ["id"]
        verbose_name = "Reserve"
        verbose_name_plural = "Reserves"

    def __str__(self):
        return self.licence

def reserve_save(sender, instance, created, **kwargs):
    lot = Lot.objects.filter(id=instance.lot_id)
    if created:
        if instance.status == "bu":
            lot.update(status="bu")

    if instance.status == "an":
        lot.update(status="av")

post_save.connect(reserve_save, sender=Reserve)

class Payment(BaseModel):

    reserve = models.ForeignKey(
        Reserve, on_delete=models.CASCADE, related_name='payments')
    number = models.PositiveIntegerField()
    total = models.PositiveIntegerField()
        
    class Meta:
        ordering = ["id"]
        verbose_name = "Payment"
        verbose_name_plural = "Payments"

    def __str__(self):
        return str(self.number)

def payment_save(sender, instance, created, **kwargs):
    if created:       
        reserve = Reserve.objects.get(id=instance.reserve.id)
        lot = Lot.objects.get(id=reserve.lot.id)
        reserve.status = 'fi'
        lot.status = 'av'
        lot.save()
        reserve.check_out = timezone.now()
        reserve.save()

post_save.connect(payment_save, sender=Payment)

class FarePeriod(BaseModel):
    """Model definition for FarePlan."""

    name = models.CharField('Nombre', max_length=150)
    price = models.PositiveIntegerField('Precio', default=0)

    class Meta:
        """Meta definition for FarePlan."""

        ordering = ['id']
        verbose_name = 'FarePlan'
        verbose_name_plural = 'FarePlans'

    def __str__(self):
        return self.name

class ReservePeriod(BaseModel):
    '''Model definition for ReservePeriod.'''

    class Status(models.TextChoices):
        INITIATE = 'in', 'Iniciada'
        FINISHED = 'fi', 'Finalizada'
        ANULLED = 'an', 'Anulada'

    lot = models.ForeignKey(
        Lot, on_delete=models.CASCADE, verbose_name="Estacionamiento", related_name="periods")
    status = models.CharField(choices=Status.choices, verbose_name="Estado de Reserva Periodo", default='in', max_length=2) 
    fare_period = models.ForeignKey(
        FarePeriod, on_delete=models.CASCADE, verbose_name='Tarifa Plan', related_name="periods")
    licence = models.CharField('Patente', max_length=15)
    check_in = models.DateTimeField('Entrada')
    check_out = models.DateTimeField('Salida')
    total = models.PositiveIntegerField()
    obs = models.TextField(
        max_length=200, blank=True)

    class Meta:
        '''Meta definition for ReservePeriod.'''

        verbose_name = 'ReservePeriod'
        verbose_name_plural = 'ReservePeriods'

    def __str__(self):
        return self.licence

def reserve_period_save(sender, instance, created, **kwargs):
    lot = Lot.objects.filter(id=instance.lot_id)
    if created:
        lot.update(status="re")

    if instance.status == "an":
        lot.update(status="av")

post_save.connect(reserve_period_save, sender=ReservePeriod)

class Client(models.Model):
    '''Model definition for Client.'''
    first_name = models.CharField('Nombre', max_length=200)
    last_name = models.CharField('Apellido', max_length=200)
    document_number = models.CharField('Numero de Documento', max_length=50) 
    social_reason = models.CharField('Razón Social', max_length=200, blank=True) 
    adress = models.CharField('Dirección', max_length=250) 
    phone = models.CharField('Telefóno', max_length=50) 
    email = models.EmailField('Correo', max_length=254)

    class Meta:
        '''Meta definition for Client.'''

        ordering = ['id']
        verbose_name = 'Client'
        verbose_name_plural = 'Clients'

    def __str__(self):
        return '{0} {1}'.format(self.first_name, self.last_name)