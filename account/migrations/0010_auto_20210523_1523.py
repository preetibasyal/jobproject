# Generated by Django 3.2.2 on 2021-05-23 09:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0009_auto_20210523_1518'),
    ]

    operations = [
        migrations.AlterField(
            model_name='applicant',
            name='company',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='applicant',
            name='job',
            field=models.CharField(max_length=80),
        ),
    ]
