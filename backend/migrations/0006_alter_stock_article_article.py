# Generated by Django 5.1.4 on 2025-02-13 19:37

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0005_rename_quantite_ventes_quantite_achetee'),
    ]

    operations = [
        migrations.AlterField(
            model_name='stock_article',
            name='article',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='backend.article'),
        ),
    ]
