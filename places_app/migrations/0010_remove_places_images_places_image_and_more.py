# Generated by Django 4.0.1 on 2022-11-27 20:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('places_app', '0009_alter_places_images_alter_places_object_type_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='places',
            name='images',
        ),
        migrations.AddField(
            model_name='places',
            name='image',
            field=models.FileField(default='', upload_to=''),
        ),
        migrations.AlterField(
            model_name='places',
            name='region',
            field=models.CharField(choices=[('Sea', 'Sea'), ('Lakes', 'Lakes'), ('Mountains', 'Mountains')], max_length=20),
        ),
    ]