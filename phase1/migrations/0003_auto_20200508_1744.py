# Generated by Django 3.0.5 on 2020-05-08 12:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('phase1', '0002_event'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='attachment',
            field=models.ImageField(upload_to='images'),
        ),
    ]