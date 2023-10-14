# Generated by Django 4.2 on 2023-04-29 18:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("rooms", "0003_amenity"),
    ]

    operations = [
        migrations.CreateModel(
            name="Facility",
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
                ("created", models.DateTimeField(auto_now_add=True)),
                ("updated", models.DateTimeField(auto_now=True)),
                ("name", models.CharField(max_length=80)),
            ],
            options={
                "abstract": False,
            },
        ),
        migrations.CreateModel(
            name="HouseRule",
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
                ("created", models.DateTimeField(auto_now_add=True)),
                ("updated", models.DateTimeField(auto_now=True)),
                ("name", models.CharField(max_length=80)),
            ],
            options={
                "abstract": False,
            },
        ),
        migrations.AddField(
            model_name="room",
            name="amenities",
            field=models.ManyToManyField(to="rooms.amenity"),
        ),
        migrations.RemoveField(
            model_name="room",
            name="room_type",
        ),
        migrations.AddField(
            model_name="room",
            name="facilities",
            field=models.ManyToManyField(to="rooms.facility"),
        ),
        migrations.AddField(
            model_name="room",
            name="house_rules",
            field=models.ManyToManyField(to="rooms.houserule"),
        ),
        migrations.AddField(
            model_name="room",
            name="room_type",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                to="rooms.roomtype",
            ),
        ),
    ]
