# Generated by Django 4.0.6 on 2024-04-15 23:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('biblioteca', '0002_alter_livro_autor'),
    ]

    operations = [
        migrations.AddField(
            model_name='autor',
            name='retrato',
            field=models.ImageField(blank=True, default=None, null=True, upload_to='retratos'),
        ),
    ]
