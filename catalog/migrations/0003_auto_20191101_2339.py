# Generated by Django 2.2.6 on 2019-11-02 02:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0002_mascota_foto'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mascota',
            name='descripcion',
            field=models.CharField(help_text='Descripcion', max_length=500),
        ),
        migrations.AlterField(
            model_name='mascota',
            name='nombre',
            field=models.CharField(help_text='Nombre', max_length=250),
        ),
        migrations.AlterField(
            model_name='mascota',
            name='raza',
            field=models.CharField(help_text='Raza', max_length=250),
        ),
        migrations.AlterField(
            model_name='mascota',
            name='tipo',
            field=models.CharField(help_text='Tipo', max_length=250),
        ),
    ]
