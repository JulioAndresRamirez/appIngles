# Generated by Django 2.2.1 on 2019-05-15 14:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0008_auto_20190515_0953'),
    ]

    operations = [
        migrations.AlterField(
            model_name='prueba',
            name='hora_fin',
            field=models.DateTimeField(blank=True, null=True, verbose_name='Hora Fin'),
        ),
        migrations.AlterField(
            model_name='prueba',
            name='hora_inicio',
            field=models.DateTimeField(blank=True, null=True, verbose_name='Hora inicio'),
        ),
    ]
