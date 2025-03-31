# Generated by Django 5.1.7 on 2025-03-31 13:44

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AboutHeaders',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description_company', models.CharField(blank=True, max_length=255, null=True, verbose_name='Заголовок1')),
                ('advantages', models.CharField(blank=True, max_length=255, null=True, verbose_name='Заголовок2')),
                ('best_in_business', models.CharField(blank=True, max_length=255, null=True, verbose_name='Заголовок3')),
                ('contacts', models.CharField(blank=True, max_length=255, null=True, verbose_name='Заголовок4')),
                ('accurately_time', models.CharField(blank=True, max_length=255, null=True, verbose_name='Заголовок5')),
                ('training', models.CharField(blank=True, max_length=255, null=True, verbose_name='Заголовок6')),
                ('last_review', models.CharField(blank=True, max_length=255, null=True, verbose_name='Заголовок7')),
            ],
            options={
                'verbose_name': 'заголовок',
                'verbose_name_plural': 'Заголовки',
                'db_table': 'about_headers',
            },
        ),
        migrations.CreateModel(
            name='AccuratelyTime',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=255, null=True, verbose_name='Заголовок')),
                ('short_description', models.CharField(blank=True, max_length=255, null=True, verbose_name='Кроткое описание')),
                ('description', models.CharField(blank=True, max_length=255, null=True, verbose_name='Описание')),
            ],
            options={
                'verbose_name': 'текст',
                'verbose_name_plural': 'Текст точно и в срок',
                'db_table': 'accurately_time',
            },
        ),
        migrations.CreateModel(
            name='Advantages',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('num_big_text', models.CharField(blank=True, max_length=255, null=True, verbose_name='Количество')),
                ('big_text', models.CharField(blank=True, max_length=255, null=True, verbose_name='Название')),
                ('num_small_text', models.CharField(blank=True, max_length=255, null=True, verbose_name='Количество')),
                ('small_text', models.CharField(blank=True, max_length=255, null=True, verbose_name='Описание')),
                ('description', models.CharField(blank=True, max_length=255, null=True, verbose_name='Описание')),
            ],
            options={
                'verbose_name': 'текст',
                'verbose_name_plural': 'Текст преимуществ',
                'db_table': 'advantages',
            },
        ),
        migrations.CreateModel(
            name='BestInBusiness',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=255, null=True, verbose_name='Заголовок')),
                ('short_description', models.CharField(blank=True, max_length=255, null=True, verbose_name='Кроткое описание')),
                ('description', models.CharField(blank=True, max_length=255, null=True, verbose_name='Описание')),
            ],
            options={
                'verbose_name': 'текст',
                'verbose_name_plural': 'Текст лучшие в бизнесе',
                'db_table': 'best_in_business',
            },
        ),
        migrations.CreateModel(
            name='Contacts',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('img', models.ImageField(blank=True, null=True, upload_to='mini_icons_on_page', verbose_name='Изображение')),
                ('description', models.CharField(blank=True, max_length=255, null=True, verbose_name='Описание')),
            ],
            options={
                'verbose_name': 'контакт',
                'verbose_name_plural': 'Контакты',
                'db_table': 'contacts',
            },
        ),
        migrations.CreateModel(
            name='DescriptionCompany',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=255, null=True, verbose_name='Название')),
                ('description', models.TextField(blank=True, null=True, verbose_name='Описание')),
                ('short_description', models.CharField(blank=True, max_length=255, null=True, verbose_name='Короткое описание')),
            ],
            options={
                'verbose_name': 'текст',
                'verbose_name_plural': 'Текст описания',
                'db_table': 'description_company',
            },
        ),
        migrations.CreateModel(
            name='Training',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('img', models.ImageField(blank=True, null=True, upload_to='staff_training', verbose_name='Изображение')),
                ('description', models.CharField(blank=True, max_length=255, null=True, verbose_name='Описание')),
            ],
            options={
                'verbose_name': 'изображение',
                'verbose_name_plural': 'Изображения',
                'db_table': 'training',
            },
        ),
    ]
