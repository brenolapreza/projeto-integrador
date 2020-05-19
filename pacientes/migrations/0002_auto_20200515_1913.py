# Generated by Django 3.0.6 on 2020-05-15 19:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pacientes', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='paciente',
            old_name='_cpf',
            new_name='cpf',
        ),
        migrations.RenameField(
            model_name='paciente',
            old_name='_endereco',
            new_name='endereco',
        ),
        migrations.RenameField(
            model_name='paciente',
            old_name='_nascionalidade',
            new_name='nascionalidade',
        ),
        migrations.RenameField(
            model_name='paciente',
            old_name='_nome',
            new_name='nome',
        ),
        migrations.RenameField(
            model_name='paciente',
            old_name='_telefone',
            new_name='telefone',
        ),
        migrations.AddField(
            model_name='paciente',
            name='diagnostico',
            field=models.TextField(blank=True, max_length=500, null=True, verbose_name='Diagnóstico'),
        ),
    ]
