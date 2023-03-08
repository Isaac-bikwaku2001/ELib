# Generated by Django 4.1.5 on 2023-01-09 19:37

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Auteur',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=100)),
                ('prenom', models.CharField(max_length=100)),
                ('nationalite', models.CharField(max_length=80)),
            ],
        ),
        migrations.CreateModel(
            name='Genre',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('libelle', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Livre',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ISBN', models.CharField(max_length=50, unique=True)),
                ('titre', models.CharField(max_length=90)),
                ('langue', models.CharField(max_length=50)),
                ('date_edition', models.DateField()),
                ('image', models.ImageField(blank=True, null=True, upload_to='')),
                ('auteur', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='elibrary.auteur')),
                ('genre', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='elibrary.genre')),
            ],
        ),
        migrations.CreateModel(
            name='Exemplaire',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre_exemplaire', models.IntegerField()),
                ('livre', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='elibrary.livre')),
            ],
        ),
        migrations.CreateModel(
            name='Emprunt',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_emprunt', models.DateField(auto_now_add=True)),
                ('date_remise', models.DateField(default=14)),
                ('client', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('livre', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='elibrary.livre')),
            ],
        ),
    ]