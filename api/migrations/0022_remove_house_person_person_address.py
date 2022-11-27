# Generated by Django 4.1.2 on 2022-11-11 03:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0021_remove_person_address_house_person'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='house',
            name='person',
        ),
        migrations.AddField(
            model_name='person',
            name='address',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='api.house'),
        ),
    ]