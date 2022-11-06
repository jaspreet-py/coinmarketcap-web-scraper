# Generated by Django 4.1.3 on 2022-11-06 11:13

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ("app", "0003_delete_currency"),
    ]

    operations = [
        migrations.CreateModel(
            name="Currency",
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
                ("source", models.CharField(default="", max_length=100)),
                ("updated_on", models.DateTimeField(default=django.utils.timezone.now)),
                ("data", models.JSONField(default=list)),
            ],
        ),
    ]