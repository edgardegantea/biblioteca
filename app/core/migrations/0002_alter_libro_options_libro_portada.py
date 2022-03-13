# Generated by Django 4.0.2 on 2022-03-03 02:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='libro',
            options={'verbose_name': 'Título', 'verbose_name_plural': 'Títulos'},
        ),
        migrations.AddField(
            model_name='libro',
            name='portada',
            field=models.ImageField(null=True, upload_to='imagenes/libros/', verbose_name='Portada'),
        ),
    ]