# Generated by Django 4.0.1 on 2022-11-25 17:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('places_app', '0007_alter_places_object_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='places',
            name='object_type',
            field=models.CharField(choices=[('Hotel', 'Hotel'), ('Cottage', 'Cottage'), ('Apartment', 'Apartment')], max_length=20),
        ),
        migrations.AlterField(
            model_name='places',
            name='region',
            field=models.CharField(choices=[('Mountains', 'Mountains'), ('Lakes', 'Lakes'), ('Sea', 'Sea')], max_length=20),
        ),
    ]
