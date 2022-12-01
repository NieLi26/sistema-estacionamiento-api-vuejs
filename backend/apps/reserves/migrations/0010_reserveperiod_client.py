# Generated by Django 4.1.1 on 2022-11-08 22:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("reserves", "0009_client"),
    ]

    operations = [
        migrations.AddField(
            model_name="reserveperiod",
            name="client",
            field=models.ForeignKey(
                default=1,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="periods",
                to="reserves.client",
                verbose_name="cliente",
            ),
            preserve_default=False,
        ),
    ]