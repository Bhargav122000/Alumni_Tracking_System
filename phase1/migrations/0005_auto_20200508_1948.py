# Generated by Django 3.0.5 on 2020-05-08 14:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('phase1', '0004_auto_20200508_1827'),
    ]

    operations = [
        migrations.RenameField(
            model_name='event',
            old_name='username',
            new_name='name',
        ),
    ]