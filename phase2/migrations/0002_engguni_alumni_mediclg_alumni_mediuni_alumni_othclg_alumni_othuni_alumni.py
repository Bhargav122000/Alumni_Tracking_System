# Generated by Django 3.0.5 on 2020-04-26 17:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('phase2', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='EnggUni_Alumni',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('person_name', models.CharField(max_length=100)),
                ('person_email', models.CharField(max_length=150)),
                ('person_gender', models.CharField(max_length=6)),
                ('person_phone', models.CharField(max_length=10)),
                ('institution_name', models.CharField(max_length=100)),
                ('institution_branch', models.CharField(max_length=50)),
                ('institution_year_pass', models.SmallIntegerField()),
                ('institution_state', models.CharField(max_length=50)),
                ('institution_place', models.CharField(max_length=50)),
                ('company_name', models.CharField(max_length=100)),
                ('company_role', models.CharField(max_length=50)),
                ('company_year_join', models.SmallIntegerField()),
                ('company_state', models.CharField(max_length=50)),
                ('company_place', models.CharField(max_length=50)),
                ('company_previous', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='MediClg_Alumni',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('person_name', models.CharField(max_length=100)),
                ('person_email', models.CharField(max_length=150)),
                ('person_gender', models.CharField(max_length=6)),
                ('person_phone', models.CharField(max_length=10)),
                ('institution_name', models.CharField(max_length=100)),
                ('institution_branch', models.CharField(max_length=50)),
                ('institution_year_pass', models.SmallIntegerField()),
                ('institution_state', models.CharField(max_length=50)),
                ('institution_place', models.CharField(max_length=50)),
                ('company_name', models.CharField(max_length=100)),
                ('company_role', models.CharField(max_length=50)),
                ('company_year_join', models.SmallIntegerField()),
                ('company_state', models.CharField(max_length=50)),
                ('company_place', models.CharField(max_length=50)),
                ('company_previous', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='MediUni_Alumni',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('person_name', models.CharField(max_length=100)),
                ('person_email', models.CharField(max_length=150)),
                ('person_gender', models.CharField(max_length=6)),
                ('person_phone', models.CharField(max_length=10)),
                ('institution_name', models.CharField(max_length=100)),
                ('institution_branch', models.CharField(max_length=50)),
                ('institution_year_pass', models.SmallIntegerField()),
                ('institution_state', models.CharField(max_length=50)),
                ('institution_place', models.CharField(max_length=50)),
                ('company_name', models.CharField(max_length=100)),
                ('company_role', models.CharField(max_length=50)),
                ('company_year_join', models.SmallIntegerField()),
                ('company_state', models.CharField(max_length=50)),
                ('company_place', models.CharField(max_length=50)),
                ('company_previous', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='OthClg_Alumni',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('person_name', models.CharField(max_length=100)),
                ('person_email', models.CharField(max_length=150)),
                ('person_gender', models.CharField(max_length=6)),
                ('person_phone', models.CharField(max_length=10)),
                ('institution_name', models.CharField(max_length=100)),
                ('institution_branch', models.CharField(max_length=50)),
                ('institution_year_pass', models.SmallIntegerField()),
                ('institution_state', models.CharField(max_length=50)),
                ('institution_place', models.CharField(max_length=50)),
                ('company_name', models.CharField(max_length=100)),
                ('company_role', models.CharField(max_length=50)),
                ('company_year_join', models.SmallIntegerField()),
                ('company_state', models.CharField(max_length=50)),
                ('company_place', models.CharField(max_length=50)),
                ('company_previous', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='OthUni_Alumni',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('person_name', models.CharField(max_length=100)),
                ('person_email', models.CharField(max_length=150)),
                ('person_gender', models.CharField(max_length=6)),
                ('person_phone', models.CharField(max_length=10)),
                ('institution_name', models.CharField(max_length=100)),
                ('institution_branch', models.CharField(max_length=50)),
                ('institution_year_pass', models.SmallIntegerField()),
                ('institution_state', models.CharField(max_length=50)),
                ('institution_place', models.CharField(max_length=50)),
                ('company_name', models.CharField(max_length=100)),
                ('company_role', models.CharField(max_length=50)),
                ('company_year_join', models.SmallIntegerField()),
                ('company_state', models.CharField(max_length=50)),
                ('company_place', models.CharField(max_length=50)),
                ('company_previous', models.TextField()),
            ],
        ),
    ]
