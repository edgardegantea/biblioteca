# Generated by Django 4.0.2 on 2022-03-05 02:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0006_libro_autor'),
    ]

    operations = [
        migrations.CreateModel(
            name='Categoria',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50, unique=True, verbose_name='Nombre de la categoría')),
                ('descripcion', models.TextField(max_length=1000, verbose_name='Descripción')),
            ],
        ),
        migrations.CreateModel(
            name='Editorial',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100, unique=True, verbose_name='Editorial')),
                ('email', models.EmailField(max_length=100, unique=True, verbose_name='Correo electrónico')),
                ('telefono', models.CharField(max_length=15, null=True, verbose_name='Teléfono')),
                ('url', models.URLField(max_length=255, null=True, verbose_name='URL de la Editorial')),
                ('pais', models.CharField(max_length=50, verbose_name='País')),
            ],
        ),
        migrations.AlterField(
            model_name='libro',
            name='autor',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='core.autor', verbose_name='Seleccione el autor'),
        ),
        migrations.AddField(
            model_name='libro',
            name='editorial',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='core.editorial', verbose_name='Elija la Editorial'),
        ),
        migrations.AlterField(
            model_name='libro',
            name='categoria',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='core.categoria', verbose_name='Elija la categoría'),
        ),
    ]