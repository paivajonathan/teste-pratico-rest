# Generated by Django 4.2 on 2023-04-23 18:46

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('endereco', '0003_alter_endereco_cuf_alter_endereco_vnumero'),
    ]

    operations = [
        migrations.AlterField(
            model_name='endereco',
            name='cUF',
            field=models.CharField(max_length=2, validators=[django.core.validators.MinLengthValidator(2, message='Este campo deve ter 2 caracteres.')]),
        ),
    ]