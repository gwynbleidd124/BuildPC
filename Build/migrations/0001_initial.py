# Generated by Django 5.1.1 on 2024-11-03 13:53

import Build.models
import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150)),
                ('info', models.TextField(blank=True, max_length=1000, null=True)),
                ('image', models.ImageField(blank=True, null=True, upload_to='category_images/')),
                ('slug', models.SlugField(blank=True, null=True, unique=True)),
                ('parent_category', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='subcategories', to='Build.category')),
            ],
            bases=(Build.models.SlugifyMixin, models.Model),
        ),
        migrations.CreateModel(
            name='Case',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150)),
                ('info', models.TextField(blank=True, max_length=2500, null=True)),
                ('manufacturer', models.CharField(max_length=50)),
                ('image', models.ImageField(blank=True, null=True, upload_to='case_images/')),
                ('form_factor', models.CharField(max_length=50)),
                ('location_power_supply', models.CharField(max_length=50)),
                ('side_window', models.CharField(max_length=50)),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('color', models.CharField(max_length=50)),
                ('slug', models.SlugField(blank=True, null=True, unique=True)),
                ('categories', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='cases', to='Build.category')),
            ],
            bases=(Build.models.SlugifyMixin, models.Model),
        ),
        migrations.CreateModel(
            name='CoolingSystem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150)),
                ('info', models.TextField(blank=True, max_length=2500, null=True)),
                ('manufacturer', models.CharField(max_length=50)),
                ('image', models.ImageField(blank=True, null=True, upload_to='coolingsystem_images/')),
                ('max_speed', models.IntegerField()),
                ('power_dissipation', models.IntegerField()),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('heat_pipes', models.IntegerField()),
                ('slug', models.SlugField(blank=True, null=True, unique=True)),
                ('categories', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='coolingsystem', to='Build.category')),
            ],
            bases=(Build.models.SlugifyMixin, models.Model),
        ),
        migrations.CreateModel(
            name='CPU',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150)),
                ('info', models.TextField(blank=True, max_length=2500, null=True)),
                ('manufacturer', models.CharField(max_length=50)),
                ('image', models.ImageField(blank=True, null=True, upload_to='сpu_images/')),
                ('socket', models.CharField(help_text='Укажите сокет процессора', max_length=50)),
                ('chipset', models.CharField(blank=True, max_length=50, null=True)),
                ('cores', models.IntegerField()),
                ('threads', models.IntegerField()),
                ('base_clock', models.DecimalField(decimal_places=1, max_digits=2)),
                ('turbo_clock', models.DecimalField(decimal_places=1, max_digits=2)),
                ('cash_1', models.CharField(max_length=50)),
                ('cash_2', models.CharField(max_length=50)),
                ('cash_3', models.CharField(max_length=50)),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('slug', models.SlugField(blank=True, null=True, unique=True)),
                ('categories', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='cpus', to='Build.category')),
            ],
            bases=(Build.models.SlugifyMixin, models.Model),
        ),
        migrations.CreateModel(
            name='GPU',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('info', models.TextField(blank=True, max_length=2500, null=True)),
                ('manufacturer_chip', models.CharField(blank=True, max_length=150, null=True)),
                ('manufacturer', models.CharField(max_length=150)),
                ('line_videocard', models.CharField(blank=True, max_length=150, null=True)),
                ('image', models.ImageField(blank=True, null=True, upload_to='gpu_images/')),
                ('memory', models.IntegerField(help_text='Объём памяти в гб')),
                ('type_memory', models.CharField(help_text='Указать какая память у видеокарты. GDDR5 or GDDR6', max_length=150)),
                ('memory_bus', models.IntegerField(help_text='Указать разрядность шины памяти')),
                ('frequency', models.IntegerField(help_text='Частота работы видеочипа')),
                ('turbo_frequency', models.IntegerField(help_text='Частота работы видеочипа в турбобусте')),
                ('universal_processors', models.IntegerField(blank=True, null=True)),
                ('texture_block', models.IntegerField(blank=True, null=True)),
                ('color', models.CharField(blank=True, max_length=150, null=True)),
                ('TDP', models.IntegerField(blank=True, null=True)),
                ('PCIe', models.FloatField(help_text='Указать версию PCIe')),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('slug', models.SlugField(blank=True, null=True, unique=True)),
                ('categories', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='gpus', to='Build.category')),
            ],
            bases=(Build.models.SlugifyMixin, models.Model),
        ),
        migrations.CreateModel(
            name='MotherBoard',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150)),
                ('info', models.TextField(blank=True, max_length=2500, null=True)),
                ('manufacturer', models.CharField(max_length=50)),
                ('image', models.ImageField(blank=True, null=True, upload_to='motherbroad_images/')),
                ('form_factor', models.CharField(max_length=50)),
                ('socket', models.CharField(max_length=50)),
                ('chipset', models.CharField(max_length=50)),
                ('type_memory_mb', models.CharField(max_length=50)),
                ('memory_slots', models.IntegerField()),
                ('M2_slots', models.IntegerField()),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('slug', models.SlugField(blank=True, null=True, unique=True)),
                ('categories', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='motherbroads', to='Build.category')),
            ],
            bases=(Build.models.SlugifyMixin, models.Model),
        ),
        migrations.CreateModel(
            name='PowerSupply',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150)),
                ('info', models.TextField(blank=True, max_length=2500, null=True)),
                ('manufacturer', models.CharField(max_length=50)),
                ('image', models.ImageField(blank=True, null=True, upload_to='powersupply_images/')),
                ('wattage', models.IntegerField()),
                ('certification', models.CharField(max_length=50)),
                ('power_cpu', models.CharField(max_length=50)),
                ('power_gpu', models.CharField(max_length=50)),
                ('power_12W', models.IntegerField(blank=True, null=True)),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('slug', models.SlugField(blank=True, null=True, unique=True)),
                ('categories', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='powersupplies', to='Build.category')),
            ],
            bases=(Build.models.SlugifyMixin, models.Model),
        ),
        migrations.CreateModel(
            name='RAM',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150)),
                ('info', models.TextField(blank=True, max_length=2500, null=True)),
                ('manufacturer', models.CharField(max_length=50)),
                ('image', models.ImageField(blank=True, null=True, upload_to='ram_images/')),
                ('memory_size', models.IntegerField()),
                ('type_memory', models.CharField(max_length=50)),
                ('frequency_ram', models.IntegerField()),
                ('cl', models.IntegerField(blank=True, null=True)),
                ('tRCD', models.IntegerField(blank=True, null=True)),
                ('tRP', models.IntegerField(blank=True, null=True)),
                ('tRAS', models.IntegerField(blank=True, null=True)),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('number_of_modules', models.IntegerField()),
                ('slug', models.SlugField(blank=True, null=True, unique=True)),
                ('categories', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='ram', to='Build.category')),
            ],
            bases=(Build.models.SlugifyMixin, models.Model),
        ),
        migrations.CreateModel(
            name='StorageDevice',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150)),
                ('info', models.TextField(blank=True, max_length=2500, null=True)),
                ('manufacturer', models.CharField(max_length=50)),
                ('image', models.ImageField(blank=True, null=True, upload_to='storage_images/')),
                ('type', models.CharField(choices=[('ssd', 'SSD Накопитель'), ('ssd M2', 'SSD M2 Накопитель'), ('HDD', 'Жёсткий диск')], default='ssd', max_length=50)),
                ('memory_size_storage', models.IntegerField()),
                ('max_recording_speed', models.IntegerField()),
                ('max_reading_speed', models.IntegerField()),
                ('TBW', models.IntegerField(blank=True, null=True)),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('slug', models.SlugField(blank=True, null=True, unique=True)),
                ('categories', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='storagedevices', to='Build.category')),
            ],
            bases=(Build.models.SlugifyMixin, models.Model),
        ),
        migrations.CreateModel(
            name='Computer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=150, null=True)),
                ('info', models.TextField(blank=True, max_length=2500, null=True)),
                ('image', models.ImageField(blank=True, null=True, upload_to='pc_images/')),
                ('total_price', models.DecimalField(decimal_places=2, default=0, max_digits=10)),
                ('slug', models.SlugField(blank=True, null=True, unique=True)),
                ('author', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='author', to=settings.AUTH_USER_MODEL)),
                ('case', models.ForeignKey(default=3, on_delete=django.db.models.deletion.CASCADE, to='Build.case')),
                ('categories', models.ManyToManyField(related_name='computers', to='Build.category')),
                ('cooling_system', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='Build.coolingsystem')),
                ('cpu', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='Build.cpu')),
                ('gpu', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='Build.gpu')),
                ('motherboard', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='Build.motherboard')),
                ('power_supply', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='Build.powersupply')),
                ('ram', models.ManyToManyField(default=1, to='Build.ram')),
                ('storage_device', models.ManyToManyField(default=1, to='Build.storagedevice')),
            ],
            bases=(Build.models.SlugifyMixin, models.Model),
        ),
    ]
