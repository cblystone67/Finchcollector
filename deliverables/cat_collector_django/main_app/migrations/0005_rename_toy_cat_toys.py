# Generated by Django 4.2.1 on 2023-06-02 20:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0004_cat_toy'),
    ]

    operations = [
        migrations.RenameField(
            model_name='cat',
            old_name='toy',
            new_name='toys',
        ),
    ]
