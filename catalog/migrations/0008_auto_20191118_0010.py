# Generated by Django 2.2.6 on 2019-11-18 03:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0007_mascota_sexo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mascota',
            name='sexo',
            field=models.CharField(choices=[('Hembra', 'hembra'), ('Macho', 'macho')], max_length=10, null=True),
        ),
    ]
