# Generated by Django 5.1.4 on 2025-02-13 18:56

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Categorie',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom_categorie', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Client',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=100)),
                ('prenoms', models.CharField(max_length=100)),
                ('telephone', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=100)),
                ('stock', models.PositiveIntegerField(null=True)),
                ('prix', models.FloatField()),
                ('categorie', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='backend.categorie')),
            ],
        ),
        migrations.CreateModel(
            name='Stock_article',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('stock_article', models.PositiveIntegerField()),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('article', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='backend.article')),
            ],
        ),
        migrations.CreateModel(
            name='Ventes',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('article_nom', models.CharField(max_length=100)),
                ('quantite', models.PositiveIntegerField()),
                ('prix', models.FloatField()),
                ('prix_total', models.FloatField(editable=False)),
                ('date_vente', models.DateTimeField(auto_now_add=True)),
                ('article', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='backend.article')),
            ],
        ),
        migrations.CreateModel(
            name='Facture',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('id_facture', models.IntegerField()),
                ('prix_total', models.FloatField(editable=False)),
                ('nom_client', models.CharField(max_length=100)),
                ('date_Facture', models.DateTimeField(auto_now_add=True)),
                ('id_client', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='backend.client')),
                ('id_vente', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='backend.ventes')),
            ],
        ),
    ]
