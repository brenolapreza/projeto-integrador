# Generated by Django 3.0.6 on 2020-05-20 22:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('exames', '0004_exame__diagnostico'),
    ]

    operations = [
        migrations.AlterField(
            model_name='exame',
            name='_tipo',
            field=models.PositiveIntegerField(choices=[(1, 'Urina'), (2, 'Sangue'), (3, 'Vista'), (4, 'Mamografia'), (5, 'Tomografia'), (6, 'Rotina'), (7, 'Pezinho')], default=2, verbose_name='tipo de exame'),
        ),
    ]
