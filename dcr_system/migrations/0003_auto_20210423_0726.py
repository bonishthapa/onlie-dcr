# Generated by Django 3.2 on 2021-04-23 07:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dcr_system', '0002_auto_20210422_1216'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='dcrhigher',
            name='dcr_id',
        ),
        migrations.RemoveField(
            model_name='dcrhigher',
            name='supervised_id',
        ),
        migrations.RemoveField(
            model_name='dcrhigher',
            name='updated_by',
        ),
        migrations.DeleteModel(
            name='DailyCallReport',
        ),
        migrations.DeleteModel(
            name='DcrHigher',
        ),
    ]