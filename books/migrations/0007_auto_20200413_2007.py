# Generated by Django 3.0.5 on 2020-04-13 14:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0006_auto_20200413_2003'),
    ]

    operations = [
        migrations.RenameField(
            model_name='comment',
            old_name='text',
            new_name='comment',
        ),
    ]
