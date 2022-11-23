# Generated by Django 4.1.3 on 2022-11-23 21:59

from decimal import Decimal
import django.core.validators
from django.db import migrations, models
import multiselectfield.db.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Places',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('place_name', models.CharField(max_length=120, unique=True)),
                ('city', models.CharField(max_length=50)),
                ('region', models.CharField(choices=[('Lakes', 'Lakes'), ('Mountains', 'Mountains'), ('Sea', 'Sea')], max_length=20)),
                ('object_type', models.CharField(choices=[('Apartment', 'Apartment'), ('Cottage', 'Cottage'), ('Hotel', 'Hotel')], max_length=20)),
                ('price_per_night', models.DecimalField(decimal_places=2, max_digits=10, validators=[django.core.validators.MinValueValidator(Decimal('50.00'))])),
                ('facilities', multiselectfield.db.fields.MultiSelectField(choices=[(1, 'Swimming pool'), (2, 'Free parking outside'), (3, 'Wi-Fi'), (4, 'Pet friendly'), (5, 'SPA'), (6, 'Private kitchen'), (7, 'Bike rating'), (8, 'BBQ Place'), (9, 'coffee maker'), (10, 'family room')], default='', max_length=100)),
                ('description', models.TextField()),
                ('images', models.ImageField(upload_to='places_img')),
            ],
        ),
    ]
