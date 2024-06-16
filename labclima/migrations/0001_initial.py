# Generated by Django 5.0.6 on 2024-06-16 16:06

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Registro',
            fields=[
                ('ident', models.AutoField(primary_key=True, serialize=False)),
                ('datahora', models.DateTimeField(auto_now_add=True)),
                ('nome', models.TextField(blank=True, max_length=16, null=True)),
                ('cep', models.TextField(max_length=9, validators=[django.core.validators.MinLengthValidator(9)])),
                ('temperatura', models.DecimalField(decimal_places=1, max_digits=3, null=True)),
                ('umidade', models.DecimalField(decimal_places=1, max_digits=3, null=True)),
                ('pressao', models.IntegerField(null=True, validators=[django.core.validators.MaxValueValidator(9999)])),
            ],
        ),
    ]
