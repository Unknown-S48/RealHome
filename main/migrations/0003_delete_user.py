# Generated by Django 5.1 on 2024-10-07 14:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_remove_property_description_remove_property_title_and_more'),
    ]

    operations = [
        migrations.DeleteModel(
            name='User',
        ),
    ]
