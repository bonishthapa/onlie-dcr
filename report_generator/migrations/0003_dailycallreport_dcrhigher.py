# Generated by Django 3.2 on 2021-04-23 07:26

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('user', '0006_usercontroltable'),
        ('dcr_system', '0003_auto_20210423_0726'),
        ('report_generator', '0002_auto_20210422_1216'),
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
                ('client_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='dcr_client_name', to='user.clienttable')),
                ('client_type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='dcr_client_type', to='user.clienttype')),
                ('mpo_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='dcr_mpo_id', to=settings.AUTH_USER_MODEL)),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='dcr_product', to='dcr_system.productinformation')),
                ('sample', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='dcr_sample_product', to='dcr_system.productinformation')),
                ('visited_with', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='dcr_visited_with', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='DcrHigher',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('updated_date', models.DateField(auto_now=True)),
                ('dcr_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='dcr_id', to='report_generator.dailycallreport')),
                ('supervised_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='dcr_higher_supervised', to=settings.AUTH_USER_MODEL)),
                ('updated_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='dcr_higher_updated_by', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
