# Generated by Django 4.1.3 on 2022-11-15 17:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('review_app', '0003_review_name_alter_review_id'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='review',
            name='name',
        ),
    ]
