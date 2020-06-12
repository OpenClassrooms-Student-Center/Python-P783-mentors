# Generated by Django 3.0 on 2020-06-12 17:00

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lettings', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='address',
            name='country_iso_code',
            field=models.CharField(default='USA', max_length=3, validators=[django.core.validators.MinLengthValidator(3)]),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='address',
            name='city',
            field=models.TextField(max_length=64),
        ),
        migrations.AlterField(
            model_name='address',
            name='number',
            field=models.PositiveIntegerField(validators=[django.core.validators.MaxValueValidator(9999)]),
        ),
        migrations.AlterField(
            model_name='address',
            name='state',
            field=models.CharField(max_length=2, validators=[django.core.validators.MinLengthValidator(2)]),
        ),
        migrations.AlterField(
            model_name='address',
            name='street',
            field=models.TextField(max_length=64),
        ),
        migrations.AlterField(
            model_name='address',
            name='zip_code',
            field=models.PositiveIntegerField(validators=[django.core.validators.MaxValueValidator(99999)]),
        ),
    ]
