# Generated by Django 4.1.2 on 2022-10-30 10:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0012_remove_warehouse_buyers_buyer_warehouse'),
    ]

    operations = [
        migrations.AlterField(
            model_name='warehouse',
            name='type_warehouse',
            field=models.CharField(max_length=250),
        ),
    ]