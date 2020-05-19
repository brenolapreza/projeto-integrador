# Generated by Django 3.0.6 on 2020-05-15 19:43

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Medico',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(blank=True, max_length=64, null=True, verbose_name='nome')),
                ('crm', models.CharField(blank=True, max_length=64, null=True, verbose_name='CRM')),
                ('especialidade', models.CharField(blank=True, max_length=64, null=True, verbose_name='especialidade')),
            ],
        ),
    ]
