# Generated by Django 4.1.2 on 2022-10-30 09:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0010_alter_buyer_address'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='buyer',
            name='warehouse',
        ),
        migrations.AddField(
            model_name='warehouse',
            name='buyers',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='api.buyer'),
        ),
    ]