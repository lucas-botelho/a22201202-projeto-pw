# Generated by Django 5.0.6 on 2024-06-05 09:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bandas', '0006_remove_band_biografia_song_biografia'),
    ]

    operations = [
        migrations.AlterField(
            model_name='album',
            name='cover',
            field=models.ImageField(upload_to='banda_imagens/'),
        ),
        migrations.AlterField(
            model_name='band',
            name='photo',
            field=models.ImageField(upload_to='banda_imagens/'),
        ),
    ]
