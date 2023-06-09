# Generated by Django 4.2 on 2023-04-23 19:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('endereco', '0005_alter_endereco_cuf_alter_endereco_vnumero'),
        ('empresa', '0003_alter_empresa_vemail'),
    ]

    operations = [
        migrations.AlterField(
            model_name='empresa',
            name='iCod_endereco',
            field=models.OneToOneField(error_messages={'Endereço já cadastrado.', 'unique'}, on_delete=django.db.models.deletion.CASCADE, to='endereco.endereco'),
        ),
    ]
