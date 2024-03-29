# Generated by Django 4.1.1 on 2022-10-08 17:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("reserves", "0004_remove_payment_status_alter_reserve_status"),
    ]

    operations = [
        migrations.AlterField(
            model_name="reserve",
            name="status",
            field=models.CharField(
                choices=[("bu", "Ocupada"), ("fi", "Finalizada"), ("an", "Anulada")],
                default="bu",
                max_length=2,
                verbose_name="Estado de Reserva",
            ),
        ),
    ]
