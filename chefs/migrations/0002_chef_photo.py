# Generated by Django 3.0.6 on 2020-06-03 05:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chefs', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='chef',
            name='photo',
            field=models.ImageField(default=None, upload_to='Photos/%Y/%m/%d/'),
            preserve_default=False,
        ),
    ]