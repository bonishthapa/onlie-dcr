# Generated by Django 3.1.6 on 2021-04-22 06:31

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AdminReport',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subject', models.CharField(max_length=250)),
                ('status1', models.CharField(max_length=250)),
                ('status2', models.CharField(max_length=250)),
                ('updated_date', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='LeaveReport',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subject', models.CharField(max_length=250)),
                ('status1', models.CharField(max_length=250)),
                ('status2', models.CharField(max_length=250)),
                ('updated_date', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]