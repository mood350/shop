# Generated by Django 5.1.4 on 2025-02-20 13:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0018_alter_facture_prix'),
    ]

    operations = [
        migrations.AlterField(
            model_name='facture',
            name='prix',
            field=models.FloatField(editable=False),
        ),
    ]
