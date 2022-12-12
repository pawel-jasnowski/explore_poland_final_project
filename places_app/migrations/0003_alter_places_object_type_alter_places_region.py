# Generated by Django 4.1.3 on 2022-12-01 15:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('places_app', '0002_alter_places_object_type_alter_places_region'),
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
            field=models.CharField(choices=[('Lakes', 'Lakes'), ('Mountains', 'Mountains'), ('Sea', 'Sea')], max_length=20),
        ),
    ]