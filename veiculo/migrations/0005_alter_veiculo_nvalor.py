# Generated by Django 4.2 on 2023-04-23 19:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('veiculo', '0004_alter_veiculo_nvalor'),
    ]

    operations = [
        migrations.AlterField(
            model_name='veiculo',
            name='nValor',
            field=models.DecimalField(decimal_places=3, max_digits=15),
        ),
    ]
