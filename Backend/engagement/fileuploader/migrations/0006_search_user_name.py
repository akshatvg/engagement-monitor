# Generated by Django 2.2.4 on 2019-09-03 20:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fileuploader', '0005_auto_20190904_0203'),
    ]

    operations = [
        migrations.AddField(
            model_name='search',
            name='user_name',
            field=models.CharField(default='', editable=False, max_length=50),
        ),
    ]
