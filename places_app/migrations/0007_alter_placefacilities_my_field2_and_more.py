# Generated by Django 4.1.3 on 2022-11-21 17:59

from django.db import migrations, models
import multiselectfield.db.fields


class Migration(migrations.Migration):

    dependencies = [
        ('places_app', '0006_placefacilities_all_facilities_alter_places_region'),
    ]

    operations = [
        migrations.AlterField(
            model_name='placefacilities',
            name='my_field2',
            field=multiselectfield.db.fields.MultiSelectField(choices=[(1, 'Swimming pool'), (2, 'Free parking')], default='', max_length=3),
        ),
        migrations.AlterField(
            model_name='places',
            name='object_type',
            field=models.CharField(choices=[('Cottage', 'Cottage'), ('Apartment', 'Apartment'), ('Hotel', 'Hotel')], max_length=20),
        ),
        migrations.AlterField(
            model_name='places',
            name='region',
            field=models.CharField(choices=[('Sea', 'Sea'), ('Lakes', 'Lakes'), ('Mountains', 'Mountains')], max_length=20),
        ),
    ]
