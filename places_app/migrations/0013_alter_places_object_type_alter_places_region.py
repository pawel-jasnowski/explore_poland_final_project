# Generated by Django 4.1.3 on 2022-11-21 18:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('places_app', '0012_alter_places_object_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='places',
            name='object_type',
            field=models.CharField(choices=[('Cottage', 'Cottage'), ('Hotel', 'Hotel'), ('Apartment', 'Apartment')], max_length=20),
        ),
        migrations.AlterField(
            model_name='places',
            name='region',
            field=models.CharField(choices=[('Mountains', 'Mountains'), ('Sea', 'Sea'), ('Lakes', 'Lakes')], max_length=20),
        ),
    ]
