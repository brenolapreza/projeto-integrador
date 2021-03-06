# Generated by Django 3.0.6 on 2020-05-20 22:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pacientes', '0010_paciente_idade'),
    ]

    operations = [
        migrations.AlterField(
            model_name='paciente',
            name='idade',
            field=models.PositiveIntegerField(choices=[(1, 'Criança'), (2, 'Jovem'), (3, 'Adulto'), (4, 'Idoso')], default=1, verbose_name='Idade Pessoa'),
        ),
    ]
