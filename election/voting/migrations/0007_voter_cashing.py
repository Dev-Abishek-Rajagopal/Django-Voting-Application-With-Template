# Generated by Django 2.2.3 on 2019-07-23 11:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('voting', '0006_auto_20190722_1723'),
    ]

    operations = [
        migrations.AddField(
            model_name='voter',
            name='cashing',
            field=models.IntegerField(null=True),
        ),
    ]