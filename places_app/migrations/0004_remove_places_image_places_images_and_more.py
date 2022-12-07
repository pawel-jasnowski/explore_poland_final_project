# Generated by Django 4.1.3 on 2022-12-06 20:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('places_app', '0003_alter_places_image_alter_places_object_type_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='places',
            name='image',
        ),
        migrations.AddField(
            model_name='places',
            name='images',
            field=models.ImageField(default='', upload_to='places_img'),
        ),
        migrations.AlterField(
            model_name='places',
            name='object_type',
            field=models.CharField(choices=[('Hotel', 'Hotel'), ('Cottage', 'Cottage'), ('Apartment', 'Apartment')], max_length=20),
        ),
        migrations.AlterField(
            model_name='places',
            name='region',
            field=models.CharField(choices=[('Sea', 'Sea'), ('Lakes', 'Lakes'), ('Mountains', 'Mountains')], max_length=20),
        ),
        migrations.AlterField(
            model_name='placesimage',
            name='images',
            field=models.ImageField(default='', upload_to='places_img'),
        ),
        migrations.AlterField(
            model_name='placesimage',
            name='places',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='places_app.places'),
        ),
    ]
