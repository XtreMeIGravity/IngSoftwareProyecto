# Generated by Django 3.2.6 on 2021-09-02 03:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0006_auto_20210901_2201'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='fecha_nacimiento',
            field=models.CharField(max_length=50),
        ),
    ]
