# Generated by Django 4.0.2 on 2022-03-03 03:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0005_autor_alter_libro_categoria'),
    ]

    operations = [
        migrations.AddField(
            model_name='libro',
            name='autor',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='core.autor', verbose_name='Seleccione el autor'),
            preserve_default=False,
        ),
    ]
