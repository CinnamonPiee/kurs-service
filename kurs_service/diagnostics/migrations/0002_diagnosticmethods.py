# Generated by Django 5.1.7 on 2025-03-29 07:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('diagnostics', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='DiagnosticMethods',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=255, null=True)),
                ('img', models.CharField(blank=True, max_length=255, null=True)),
                ('description_text', models.TextField(blank=True, null=True)),
                ('services_data', models.IntegerField(blank=True, null=True)),
                ('title_data_modal', models.CharField(blank=True, max_length=255, null=True)),
            ],
            options={
                'db_table': 'diagnostic_methods',
            },
        ),
    ]
