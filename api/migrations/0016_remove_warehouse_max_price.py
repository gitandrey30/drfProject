# Generated by Django 4.1.2 on 2022-11-02 22:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0015_warehouse_max_price'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='warehouse',
            name='max_price',
        ),
    ]
