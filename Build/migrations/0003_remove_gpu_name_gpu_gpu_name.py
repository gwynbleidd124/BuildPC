# Generated by Django 5.1.1 on 2024-11-03 18:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Build', '0002_remove_gpu_name_gpu_name_gpu'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='gpu',
            name='name_gpu',
        ),
        migrations.AddField(
            model_name='gpu',
            name='name',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
