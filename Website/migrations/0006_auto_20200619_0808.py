# Generated by Django 3.0.7 on 2020-06-19 00:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Website', '0005_auto_20200619_0802'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='patient',
            name='machine',
        ),
        migrations.AlterField(
            model_name='patient',
            name='day',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
