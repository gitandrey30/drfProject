# Generated by Django 4.1.2 on 2022-10-27 18:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0008_alter_warehouse_type_warehouse'),
    ]

    operations = [
        migrations.AlterField(
            model_name='condition',
            name='status',
            field=models.CharField(choices=[('New', 'New'), ('Used', 'Used'), ('Include powerfull turbocharge', 'Include powerfull turbocharge')], max_length=250, verbose_name='статус'),
        ),
    ]