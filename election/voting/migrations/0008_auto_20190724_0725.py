# Generated by Django 2.2.3 on 2019-07-24 07:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('voting', '0007_voter_cashing'),
    ]

    operations = [
        migrations.AddField(
            model_name='voter',
            name='candidate',
            field=models.IntegerField(default=0, null=True),
        ),
        migrations.AlterField(
            model_name='voter',
            name='cashing',
            field=models.IntegerField(default=0, null=True),
        ),
    ]
