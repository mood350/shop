# Generated by Django 5.1.4 on 2025-02-23 18:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0020_ventes_payement'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ventes',
            name='payement',
            field=models.CharField(choices=[(0, 'Mixx  By Yas'), (1, 'Moov Money')], default=0, max_length=1),
        ),
    ]
