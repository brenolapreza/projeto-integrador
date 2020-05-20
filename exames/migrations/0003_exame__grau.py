# Generated by Django 3.0.6 on 2020-05-20 02:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('exames', '0002_remove_exame_data_entrega'),
    ]

    operations = [
        migrations.AddField(
            model_name='exame',
            name='_grau',
            field=models.PositiveIntegerField(choices=[(1, 'Leve'), (2, 'Grave'), (3, 'Gravissimo')], default=1, verbose_name='Grau do Exame'),
        ),
    ]