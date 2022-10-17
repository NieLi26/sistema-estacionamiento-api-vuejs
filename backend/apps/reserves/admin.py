from django.contrib import admin

from .models import Fare, Lot, Reserve, Payment, ReservePeriod, FarePeriod
# Register your models here.
admin.site.register(Lot)
admin.site.register(Fare)
admin.site.register(Reserve)
admin.site.register(Payment)
admin.site.register(FarePeriod)
admin.site.register(ReservePeriod)