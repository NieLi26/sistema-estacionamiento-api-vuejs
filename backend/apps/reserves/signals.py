from django.db.models.signals import post_save
from django.utils import timezone

from .models import Reserve, Payment, ReservePeriod, Lot


def reserve_save(sender, instance, created, **kwargs):
    lot = Lot.objects.filter(id=instance.lot_id)

    if created:
        if instance.status == "bu" and lot[0].status == 'av':
            lot.update(status="bu")

    if instance.status == "an" and lot[0].status == 'bu':
        lot.update(status="av")

post_save.connect(reserve_save, sender=Reserve)


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


def reserve_period_save(sender, instance, created, **kwargs):
    lot = Lot.objects.filter(id=instance.lot_id)
    if created:
        lot.update(status="re")

    # if instance.status == "an":
    #     lot.update(status="av")

    if instance.status == "fi":
        lot.update(status="av")

post_save.connect(reserve_period_save, sender=ReservePeriod)
