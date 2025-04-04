# Generated by Django 5.1.7 on 2025-04-03 12:07

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='RulesPersonalDataImages',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('img', models.ImageField(blank=True, null=True, upload_to='page_images', verbose_name='Изображение')),
                ('description', models.CharField(blank=True, max_length=255, null=True, verbose_name='Описание')),
            ],
            options={
                'verbose_name': 'текст',
                'verbose_name_plural': 'Правила обработки данных пользователя',
                'db_table': 'rules_personal_data_images',
            },
        ),
        migrations.CreateModel(
            name='RulesPersonalDataObligations',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.TextField(blank=True, null=True, verbose_name='Основная часть')),
                ('definition_of_terms', models.TextField(blank=True, null=True, verbose_name='1. Определение терминов')),
                ('general_provisions', models.TextField(blank=True, null=True, verbose_name='2. Общие положения')),
                ('subject_of_privacy_policy', models.TextField(blank=True, null=True, verbose_name='3. Предмет политики конфиденциальности')),
                ('purposes_of_collecting_users', models.TextField(blank=True, null=True, verbose_name='4. Цели сбора персональной информации пользователей')),
                ('methods_and_terms_of_information', models.TextField(blank=True, null=True, verbose_name='5. Способы и сроки обработки персональной информации')),
                ('obligations_parties', models.TextField(blank=True, null=True, verbose_name='6. Обязательства сторон')),
                ('liability_parties', models.TextField(blank=True, null=True, verbose_name='7. Ответственность сторон')),
                ('dispute_resolutions', models.TextField(blank=True, null=True, verbose_name='8. Решение споров')),
                ('additional_terms', models.TextField(blank=True, null=True, verbose_name='9. Дополнительные условия')),
            ],
            options={
                'verbose_name': 'текст',
                'verbose_name_plural': 'Правила обработки',
                'db_table': 'rules_personal_data_obligations',
            },
        ),
        migrations.CreateModel(
            name='RulesPersonalDataTitles',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rules_title', models.CharField(blank=True, max_length=255, null=True, verbose_name='Заголовок1')),
            ],
            options={
                'verbose_name': 'заголовок',
                'verbose_name_plural': 'Заголовки',
                'db_table': 'rules_personal_data_titles',
            },
        ),
    ]
