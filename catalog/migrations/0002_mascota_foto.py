# Generated by Django 2.2.6 on 2019-10-30 17:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='mascota',
            name='foto',
            field=models.FileField(default='catalog\\static\\catalog\\images\x08ack.jpg', upload_to=''),
        ),
    ]
