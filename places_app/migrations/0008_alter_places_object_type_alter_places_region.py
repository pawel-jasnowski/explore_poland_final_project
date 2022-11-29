# Generated by Django 4.0.1 on 2022-11-29 13:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('places_app', '0007_alter_places_object_type_alter_places_region'),
    ]

    operations = [
        migrations.AlterField(
            model_name='places',
            name='object_type',
            field=models.CharField(choices=[('Cottage', 'Cottage'), ('Apartment', 'Apartment'), ('Hotel', 'Hotel')], max_length=20),
        ),
        migrations.AlterField(
            model_name='places',
            name='region',
            field=models.CharField(choices=[('Lakes', 'Lakes'), ('Sea', 'Sea'), ('Mountains', 'Mountains')], max_length=20),
        ),
    ]
