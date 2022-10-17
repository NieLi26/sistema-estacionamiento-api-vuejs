# Generated by Django 4.1.1 on 2022-10-13 23:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("reserves", "0005_alter_reserve_status"),
    ]

    operations = [
        migrations.CreateModel(
            name="FarePlan",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("is_active", models.BooleanField(default=True, verbose_name="Activo")),
                (
                    "created_at",
                    models.DateField(
                        auto_now_add=True, verbose_name="Fecha de Creación"
                    ),
                ),
                (
                    "modified_at",
                    models.DateField(
                        auto_now=True, verbose_name="Fecha de Modificaión"
                    ),
                ),
                ("name", models.CharField(max_length=150, verbose_name="Nombre")),
                (
                    "price",
                    models.PositiveIntegerField(default=0, verbose_name="Precio"),
                ),
            ],
            options={
                "verbose_name": "FarePlan",
                "verbose_name_plural": "FarePlans",
                "ordering": ["id"],
            },
        ),
        migrations.CreateModel(
            name="ReservePeriod",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("is_active", models.BooleanField(default=True, verbose_name="Activo")),
                (
                    "created_at",
                    models.DateField(
                        auto_now_add=True, verbose_name="Fecha de Creación"
                    ),
                ),
                (
                    "modified_at",
                    models.DateField(
                        auto_now=True, verbose_name="Fecha de Modificaión"
                    ),
                ),
                (
                    "status",
                    models.CharField(
                        choices=[("in", "Iniciada"), ("fi", "Finalizada")],
                        default="in",
                        max_length=2,
                        verbose_name="Estado de Reserva Periodo",
                    ),
                ),
                ("licence", models.CharField(max_length=15, verbose_name="Patente")),
                ("check_in", models.DateTimeField(verbose_name="Entrada")),
                ("check_out", models.DateTimeField(verbose_name="Salida")),
                ("obs", models.TextField(blank=True, max_length=200)),
                (
                    "fare_plan",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="periods",
                        to="reserves.fareplan",
                        verbose_name="Tarifa Plan",
                    ),
                ),
                (
                    "lot",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="periods",
                        to="reserves.lot",
                        verbose_name="Estacionamiento",
                    ),
                ),
            ],
            options={
                "verbose_name": "ReservePeriod",
                "verbose_name_plural": "ReservePeriods",
            },
        ),
    ]
