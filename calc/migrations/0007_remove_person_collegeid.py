# Generated by Django 3.1 on 2020-09-16 09:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('calc', '0006_auto_20200916_1507'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='person',
            name='collegeID',
        ),
    ]
