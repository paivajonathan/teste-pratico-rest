# Generated by Django 4.2 on 2023-04-19 15:01

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('empresa', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='empresa',
            name='vCnpj',
            field=models.CharField(max_length=14, validators=[django.core.validators.RegexValidator('^\\d{14}$', 'O CNPJ deve conter 14 dígitos.')]),
        ),
    ]