# Generated by Django 5.0.6 on 2024-06-23 19:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('labclima', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='registro',
            name='pressao',
            field=models.DecimalField(decimal_places=2, max_digits=6, null=True),
        ),
        migrations.AlterField(
            model_name='registro',
            name='temperatura',
            field=models.DecimalField(decimal_places=2, max_digits=5, null=True),
        ),
        migrations.AlterField(
            model_name='registro',
            name='umidade',
            field=models.DecimalField(decimal_places=2, max_digits=5, null=True),
        ),
    ]
