# Generated by Django 4.0.1 on 2022-11-15 17:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('places_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='places',
            name='object_type',
            field=models.CharField(choices=[('Apartment', 'Apartment'), ('Cottage', 'Cottage'), ('Hotel', 'Hotel')], max_length=20),
        ),
        migrations.AlterField(
            model_name='places',
            name='region',
            field=models.CharField(choices=[('Lakes', 'Lakes'), ('Mountains', 'Mountains'), ('Sea', 'Sea')], max_length=20),
        ),
    ]