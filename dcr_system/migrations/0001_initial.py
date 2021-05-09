# Generated by Django 3.1.6 on 2021-04-22 06:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='DailyCallReport',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('shift', models.CharField(max_length=250)),
                ('visited_area', models.CharField(max_length=250)),
                ('gift', models.CharField(max_length=250)),
                ('quantity', models.IntegerField()),
                ('amount', models.FloatField()),
                ('dcr_date', models.DateField()),
                ('created_date', models.DateField(auto_now_add=True)),
                ('sample_qty', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='ProductType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_type_name', models.CharField(max_length=250)),
            ],
        ),
        migrations.CreateModel(
            name='ProductInformation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_name', models.CharField(max_length=250)),
                ('product_price', models.FloatField()),
                ('product_type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='product_type', to='dcr_system.producttype')),
            ],
        ),
        migrations.CreateModel(
            name='DcrHigher',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('updated_date', models.DateField(auto_now=True)),
                ('dcr_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='dcr_id', to='dcr_system.dailycallreport')),
            ],
        ),
    ]