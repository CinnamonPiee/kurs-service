# Generated by Django 5.1.7 on 2025-04-03 14:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('about', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='aboutimages',
            options={'verbose_name': 'текст', 'verbose_name_plural': 'Изображения с текстом'},
        ),
        migrations.AlterModelOptions(
            name='abouttitles',
            options={'verbose_name': 'заголовки', 'verbose_name_plural': 'Заголовки'},
        ),
    ]
