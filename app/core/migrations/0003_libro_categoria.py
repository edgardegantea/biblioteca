# Generated by Django 4.0.2 on 2022-03-03 03:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_alter_libro_options_libro_portada'),
    ]

    operations = [
        migrations.AddField(
            model_name='libro',
            name='categoria',
            field=models.CharField(choices=[('Terror', 'Terror'), ('Novela', 'Novela')], default='Novela', max_length=20, verbose_name='Categoría'),
        ),
    ]