# Generated by Django 3.0.7 on 2020-06-19 00:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Website', '0007_patient_machine'),
    ]

    operations = [
        migrations.RenameField(
            model_name='patient',
            old_name='day',
            new_name='DayOfTheWeek',
        ),
    ]
