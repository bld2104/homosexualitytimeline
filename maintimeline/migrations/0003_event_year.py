# Generated by Django 2.0.4 on 2018-04-15 15:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('maintimeline', '0002_auto_20180408_1704'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='year',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
