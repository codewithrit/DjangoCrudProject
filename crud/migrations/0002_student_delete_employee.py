# Generated by Django 4.1 on 2022-09-03 03:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("crud", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="student",
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
                ("sid", models.CharField(max_length=4)),
                ("sname", models.CharField(max_length=255)),
                ("scontact", models.CharField(max_length=15)),
            ],
        ),
        migrations.DeleteModel(name="employee",),
    ]
