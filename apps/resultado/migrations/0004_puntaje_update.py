# Generated by Django 3.2.6 on 2021-08-29 02:06

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('resultado', '0003_alter_puntaje_categoria'),
    ]

    operations = [
        migrations.AddField(
            model_name='puntaje',
            name='update',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]