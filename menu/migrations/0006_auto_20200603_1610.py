# Generated by Django 3.0.6 on 2020-06-03 10:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('menu', '0005_auto_20200603_1516'),
    ]

    operations = [
        migrations.RenameField(
            model_name='special',
            old_name='speciality',
            new_name='specialty',
        ),
    ]
