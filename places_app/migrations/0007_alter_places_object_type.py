# Generated by Django 4.0.1 on 2022-11-25 17:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('places_app', '0006_alter_places_object_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='places',
            name='object_type',
            field=models.CharField(choices=[('Apartment', 'Apartment'), ('Hotel', 'Hotel'), ('Cottage', 'Cottage')], max_length=20),
        ),
    ]