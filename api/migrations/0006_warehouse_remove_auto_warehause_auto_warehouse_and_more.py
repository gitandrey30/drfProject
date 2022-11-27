# Generated by Django 4.1.2 on 2022-10-27 13:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0005_auto_warehause_buyer_warehouse_condition_auto'),
    ]

    operations = [
        migrations.CreateModel(
            name='Warehouse',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('locate', models.CharField(max_length=250)),
                ('type_warehouse', models.CharField(choices=[('O', 'Official_dealer'), ('M', 'Market_auto_used'), ('P', 'Перекуп')], max_length=250)),
            ],
        ),
        migrations.RemoveField(
            model_name='auto',
            name='warehause',
        ),
        migrations.AddField(
            model_name='auto',
            name='warehouse',
            field=models.ManyToManyField(to='api.warehouse'),
        ),
        migrations.AlterField(
            model_name='buyer',
            name='warehouse',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='api.warehouse'),
        ),
        migrations.DeleteModel(
            name='Warehause',
        ),
    ]
