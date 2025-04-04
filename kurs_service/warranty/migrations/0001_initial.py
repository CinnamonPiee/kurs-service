# Generated by Django 5.1.7 on 2025-04-03 12:07

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='WarrantyImages',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('img', models.ImageField(blank=True, null=True, upload_to='page_images', verbose_name='Изображение')),
                ('description', models.CharField(blank=True, max_length=255, null=True, verbose_name='Описание')),
            ],
            options={
                'verbose_name': 'текст',
                'verbose_name_plural': 'Гарантия до 180 дней',
                'db_table': 'warranty_images',
            },
        ),
        migrations.CreateModel(
            name='WarrantyObligations',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('general_provisions', models.TextField(blank=True, null=True, verbose_name='1. Общие положения')),
                ('warranty_period', models.TextField(blank=True, null=True, verbose_name='2. Гарантийный срок')),
                ('execution_conditions', models.TextField(blank=True, null=True, verbose_name='3. Условия выполнения гарантийных обязательств')),
                ('cancellation_conditions', models.TextField(blank=True, null=True, verbose_name='4. Условия отказа в выполнении гарантийных обязательств')),
                ('list_types_work', models.TextField(blank=True, null=True, verbose_name='5. Перечень видов работ и запчастей, на которые гарантия не распространяется:')),
                ('parking_conditions', models.TextField(blank=True, null=True, verbose_name="6. Условия стоянки транспорта на территории сервиса ООО 'КУРС' по истечении ремонтных работ.")),
            ],
            options={
                'verbose_name': 'текст',
                'verbose_name_plural': 'Гарантии',
                'db_table': 'warranty_obligations',
            },
        ),
        migrations.CreateModel(
            name='WarrantyTitles',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('warranty_title', models.CharField(blank=True, max_length=255, null=True, verbose_name='Гарантия')),
            ],
            options={
                'verbose_name': 'заголовок',
                'verbose_name_plural': 'Заголовки',
                'db_table': 'warranty_titles',
            },
        ),
    ]
