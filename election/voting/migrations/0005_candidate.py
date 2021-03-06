# Generated by Django 2.2.3 on 2019-07-22 16:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('voting', '0004_auto_20190722_1524'),
    ]

    operations = [
        migrations.CreateModel(
            name='Candidate',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150)),
                ('rolno', models.CharField(max_length=150)),
                ('symbol', models.ImageField(height_field='height_width', max_length=225, upload_to='symbols/', width_field='picture_width')),
            ],
        ),
    ]
