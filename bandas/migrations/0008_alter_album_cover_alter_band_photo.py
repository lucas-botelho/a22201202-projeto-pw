# Generated by Django 5.0.6 on 2024-06-05 10:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bandas', '0007_alter_album_cover_alter_band_photo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='album',
            name='cover',
            field=models.ImageField(blank=True, null=True, upload_to='banda_imagens/'),
        ),
        migrations.AlterField(
            model_name='band',
            name='photo',
            field=models.ImageField(blank=True, null=True, upload_to='banda_imagens/'),
        ),
    ]
