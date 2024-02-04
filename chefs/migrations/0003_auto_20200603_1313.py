# Generated by Django 3.0.6 on 2020-06-03 07:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chefs', '0002_chef_photo'),
    ]

    operations = [
        migrations.RenameField(
            model_name='chef',
            old_name='speciality',
            new_name='designation',
        ),
        migrations.AlterField(
            model_name='chef',
            name='city',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='chef',
            name='email',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='chef',
            name='phone',
            field=models.CharField(max_length=20),
        ),
        migrations.AlterField(
            model_name='chef',
            name='state',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='chef',
            name='zipcode',
            field=models.CharField(max_length=10),
        ),
    ]
