# Generated by Django 5.1.7 on 2025-03-29 08:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('insurance', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='InsuranceQuestion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title_questions', models.CharField(blank=True, max_length=255, null=True)),
                ('content_questions', models.TextField(blank=True, null=True)),
            ],
            options={
                'db_table': 'insuranse_questions',
            },
        ),
    ]
