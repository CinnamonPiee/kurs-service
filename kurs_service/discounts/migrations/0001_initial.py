# Generated by Django 5.1.7 on 2025-03-29 08:13

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Discount',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(blank=True, max_length=255, null=True)),
                ('title', models.CharField(blank=True, max_length=255, null=True)),
                ('short_description', models.CharField(blank=True, max_length=255, null=True)),
                ('description', models.TextField(blank=True, null=True)),
                ('logo', models.CharField(blank=True, max_length=255, null=True)),
                ('img', models.CharField(blank=True, max_length=255, null=True)),
                ('date_start', models.CharField(blank=True, max_length=255, null=True)),
                ('date_stop', models.CharField(blank=True, max_length=255, null=True)),
            ],
            options={
                'db_table': 'discounts',
            },
        ),
    ]
