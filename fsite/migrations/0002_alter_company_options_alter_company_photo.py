# Generated by Django 4.2.4 on 2023-09-02 14:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fsite', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='company',
            options={'verbose_name': 'Компания', 'verbose_name_plural': 'Компании'},
        ),
        migrations.AlterField(
            model_name='company',
            name='photo',
            field=models.ImageField(upload_to='images/'),
        ),
    ]