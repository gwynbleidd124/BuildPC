# Generated by Django 5.1.1 on 2024-11-05 15:01

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Build', '0008_alter_computer_case_alter_computer_cooling_system_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='computer',
            name='case',
            field=models.ForeignKey(blank=True, default=3, null=True, on_delete=django.db.models.deletion.CASCADE, to='Build.case'),
        ),
        migrations.AlterField(
            model_name='computer',
            name='cooling_system',
            field=models.ForeignKey(blank=True, default=1, null=True, on_delete=django.db.models.deletion.CASCADE, to='Build.coolingsystem'),
        ),
        migrations.AlterField(
            model_name='computer',
            name='motherboard',
            field=models.ForeignKey(blank=True, default=1, null=True, on_delete=django.db.models.deletion.CASCADE, to='Build.motherboard'),
        ),
        migrations.AlterField(
            model_name='computer',
            name='power_supply',
            field=models.ForeignKey(blank=True, default=1, null=True, on_delete=django.db.models.deletion.CASCADE, to='Build.powersupply'),
        ),
        migrations.AlterField(
            model_name='computer',
            name='ram',
            field=models.ManyToManyField(blank=True, default=1, null=True, to='Build.ram'),
        ),
        migrations.AlterField(
            model_name='computer',
            name='storage_device',
            field=models.ManyToManyField(blank=True, default=1, null=True, to='Build.storagedevice'),
        ),
        migrations.AlterField(
            model_name='computer',
            name='total_price',
            field=models.DecimalField(blank=True, decimal_places=2, default=0, max_digits=10, null=True),
        ),
    ]
