# Generated by Django 4.2.4 on 2023-09-02 15:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fsite', '0002_alter_company_options_alter_company_photo'),
    ]

    operations = [
        migrations.AddField(
            model_name='company',
            name='url',
            field=models.URLField(blank='False'),
        ),
    ]
