# Generated by Django 4.1.13 on 2024-08-09 07:51

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("chat", "0001_initial"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="room",
            options={"ordering": ["-pk"]},
        ),
    ]
