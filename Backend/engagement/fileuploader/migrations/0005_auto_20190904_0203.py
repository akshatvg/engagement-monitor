# Generated by Django 2.2.4 on 2019-09-03 20:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('fileuploader', '0004_previoussearches'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='PreviousSearches',
            new_name='Search',
        ),
        migrations.DeleteModel(
            name='Document',
        ),
    ]
