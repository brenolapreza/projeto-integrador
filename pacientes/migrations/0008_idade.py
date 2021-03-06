# Generated by Django 3.0.6 on 2020-05-20 21:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('pacientes', '0007_auto_20200519_2056'),
    ]

    operations = [
        migrations.CreateModel(
            name='Idade',
            fields=[
                ('paciente_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='pacientes.Paciente')),
                ('crianca', models.BooleanField(default=True, verbose_name='crianca')),
                ('jovem', models.BooleanField(default=True, verbose_name='jovem')),
                ('idoso', models.BooleanField(default=True, verbose_name='idoso')),
            ],
            bases=('pacientes.paciente',),
        ),
    ]
