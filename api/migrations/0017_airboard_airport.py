# Generated by Django 4.1.2 on 2022-11-03 18:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0016_remove_warehouse_max_price'),
    ]

    operations = [
        migrations.CreateModel(
            name='AirBoard',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('brand', models.CharField(max_length=255)),
                ('model', models.CharField(max_length=255)),
                ('price', models.DecimalField(decimal_places=5, max_digits=10)),
            ],
        ),
        migrations.CreateModel(
            name='Airport',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('airboard', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.airboard')),
            ],
        ),
    ]