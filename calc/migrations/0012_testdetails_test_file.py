# Generated by Django 3.1 on 2020-09-24 10:25

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('calc', '0011_auto_20200924_1544'),
    ]

    operations = [
        migrations.AddField(
            model_name='testdetails',
            name='test_file',
            field=models.FileField(default=django.utils.timezone.now, upload_to=''),
        ),
    ]
