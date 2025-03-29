# Generated by Django 5.1.7 on 2025-03-29 10:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('check_list', '0002_orderchecklist'),
    ]

    operations = [
        migrations.CreateModel(
            name='OrderCheckListItems',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order_id', models.IntegerField(blank=True, null=True)),
                ('service_id', models.IntegerField(blank=True, null=True)),
                ('title', models.CharField(blank=True, max_length=255, null=True)),
                ('quantity', models.IntegerField(blank=True, null=True)),
                ('sum', models.IntegerField(blank=True, null=True)),
            ],
            options={
                'db_table': 'order_check_list_items',
            },
        ),
    ]
