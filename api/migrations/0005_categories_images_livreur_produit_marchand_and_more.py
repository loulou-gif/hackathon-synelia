# Generated by Django 4.2.4 on 2024-07-10 23:51

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('api', '0004_commandes_moyen_payement_userdetail_facture_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='categories',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=50)),
                ('categorie_parent', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='images',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('url', models.CharField(max_length=10000)),
            ],
        ),
        migrations.CreateModel(
            name='livreur',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='produit',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=50)),
                ('quantite', models.IntegerField()),
                ('description', models.CharField(max_length=50)),
                ('prix', models.IntegerField()),
                ('date_ajout', models.DateField(auto_now=True)),
                ('categorie', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.categories')),
                ('image', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.images')),
                ('vendeur', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='marchand',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('certifie', models.IntegerField()),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='ligne_de_livraison',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantite_livre', models.IntegerField()),
                ('statut_livraison', models.IntegerField()),
                ('numero_livreur', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.livreur')),
                ('reference_livreur', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.commandes')),
            ],
        ),
        migrations.CreateModel(
            name='ligne_de_commande',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantite_commande', models.IntegerField()),
                ('statut', models.IntegerField()),
                ('numero_commande', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.commandes')),
                ('reference_produit', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.produit')),
            ],
        ),
    ]
