# Generated by Django 3.1 on 2020-09-16 09:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('calc', '0005_auto_20200829_1625'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='person',
            name='user',
        ),
        migrations.AddField(
            model_name='person',
            name='username',
            field=models.CharField(default='17881A05J2', max_length=12),
            preserve_default=False,
        ),
    ]