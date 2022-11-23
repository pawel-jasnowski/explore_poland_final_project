# Generated by Django 4.1.3 on 2022-11-21 18:06

from django.db import migrations, models
import multiselectfield.db.fields


class Migration(migrations.Migration):

    dependencies = [
        ('places_app', '0008_remove_places_facilities_alter_places_region'),
    ]

    operations = [
        migrations.AddField(
            model_name='places',
            name='facilities',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AlterField(
            model_name='placefacilities',
            name='my_field2',
            field=multiselectfield.db.fields.MultiSelectField(choices=[(1, 'Swimming pool'), (2, 'Free parking outside')], default='', max_length=3),
        ),
        migrations.AlterField(
            model_name='places',
            name='object_type',
            field=models.CharField(choices=[('Hotel', 'Hotel'), ('Apartment', 'Apartment'), ('Cottage', 'Cottage')], max_length=20),
        ),
        migrations.AlterField(
            model_name='places',
            name='region',
            field=models.CharField(choices=[('Lakes', 'Lakes'), ('Sea', 'Sea'), ('Mountains', 'Mountains')], max_length=20),
        ),
    ]
