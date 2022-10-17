from django.core.management.base import BaseCommand
from apps.reserves.models import Lot

class Command(BaseCommand):
    help = 'Load Lots'

    def handle(self, *args, **kwargs):
        Lot.objects.all().delete()

        if not Lot.objects.count():
            for lot_name in range(1,41):
                Lot.objects.create(name=lot_name, status=Lot.Status.AVAIBLE)
