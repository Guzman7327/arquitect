# Generated by Django 5.1.2 on 2024-12-02 16:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_videojuego_categoria_alter_videojuego_genero_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='videojuego',
            name='categoria',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='videojuego',
            name='genero',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='videojuego',
            name='nombre',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='videojuego',
            name='plataforma',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='videojuego',
            name='precio',
            field=models.DecimalField(decimal_places=2, max_digits=10),
        ),
    ]
