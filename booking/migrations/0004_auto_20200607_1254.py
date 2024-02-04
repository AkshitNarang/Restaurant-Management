# Generated by Django 3.0.6 on 2020-06-07 07:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('booking', '0003_inquiry'),
    ]

    operations = [
        migrations.AddField(
            model_name='booking',
            name='month',
            field=models.CharField(default='January', max_length=200),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='booking',
            name='user_id',
            field=models.IntegerField(blank=True, default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='booking',
            name='year',
            field=models.CharField(default=2020, max_length=200),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='inquiry',
            name='user_id',
            field=models.IntegerField(blank=True, default=0),
            preserve_default=False,
        ),
    ]
