# Generated by Django 4.2 on 2023-04-17 06:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('VpnApi', '0003_countrymodel_alter_vpnmodel_countryshorts'),
    ]

    operations = [
        migrations.AlterField(
            model_name='applicationmodel',
            name='vpnserver',
            field=models.CharField(max_length=200),
        ),
    ]
