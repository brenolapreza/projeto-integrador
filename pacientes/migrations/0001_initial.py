# Generated by Django 3.0.6 on 2020-05-15 18:33

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Paciente',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('_nome', models.CharField(blank=True, max_length=50, null=True, verbose_name='nome')),
                ('_cpf', models.CharField(db_index=True, max_length=15, null=True, unique=True, verbose_name='cpf')),
                ('data_nascimento', models.DateField(blank=True, null=True, verbose_name='Data de nascimento')),
                ('_telefone', models.CharField(blank=True, max_length=50, null=True, verbose_name='telefone')),
                ('_endereco', models.CharField(blank=True, max_length=60, null=True, verbose_name='endereço')),
                ('_nascionalidade', models.CharField(blank=True, max_length=60, null=True, verbose_name='nascionalidade')),
                ('criado_em', models.DateTimeField(auto_now_add=True, null=True)),
                ('editado_em', models.DateTimeField(auto_now=True, null=True, verbose_name='Última visualização')),
            ],
        ),
    ]
