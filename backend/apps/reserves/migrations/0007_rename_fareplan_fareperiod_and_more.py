# Generated by Django 4.1.1 on 2022-10-14 12:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("reserves", "0006_fareplan_reserveperiod"),
    ]

    operations = [
        migrations.RenameModel(old_name="FarePlan", new_name="FarePeriod",),
        migrations.RenameField(
            model_name="reserveperiod", old_name="fare_plan", new_name="fare_period",
        ),
    ]
