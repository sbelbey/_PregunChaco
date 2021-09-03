# Generated by Django 3.2.6 on 2021-08-28 12:38

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('usuarios', '0006_alter_perfil_imagen_perfil'),
    ]

    operations = [
        migrations.AddField(
            model_name='perfil',
            name='creado',
            field=models.DateField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='perfil',
            name='updated',
            field=models.DateField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]