# Generated by Django 3.1.7 on 2021-03-04 09:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainone', '0008_auto_20210304_1204'),
    ]

    operations = [
        migrations.AlterField(
            model_name='videos',
            name='vid',
            field=models.FileField(null=True, upload_to='media'),
        ),
    ]
