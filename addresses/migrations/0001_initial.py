# Generated by Django 4.2 on 2023-05-04 20:17

from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Address",
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
                ("street", models.CharField(max_length=255)),
                ("number", models.IntegerField()),
                ("add_on", models.CharField(blank=True, max_length=5, null=True)),
                ("zipcode", models.CharField(max_length=10)),
                ("city", models.CharField(max_length=50)),
                ("state", models.CharField(max_length=2)),
            ],
        ),
    ]
