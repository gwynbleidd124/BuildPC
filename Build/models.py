from django.contrib.auth.models import User
from django.db import models
from django.template.defaultfilters import slugify
from transliterate import translit



class SlugifyMixin:
    def generate_slug(self):
        slug_value = translit(self.name, 'ru', reversed=True)
        return slugify(slug_value)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = self.generate_slug()
        super().save(*args, **kwargs)


class Category(SlugifyMixin, models.Model):
    name = models.CharField(max_length=150)
    info = models.TextField(max_length=1000, blank=True, null=True)
    image = models.ImageField(upload_to='category_images/', blank=True, null=True)
    slug = models.SlugField(unique=True, blank=True, null=True, max_length=50)
    parent_category = models.ForeignKey('self', on_delete=models.SET_NULL, null=True, blank=True, related_name='subcategories')

    def __str__(self):
        return self.name


class GPU(SlugifyMixin, models.Model):
    name = models.CharField(blank=True, null=True)
    info = models.TextField(max_length=2500, blank=True, null=True)
    manufacturer_chip = models.CharField(max_length=150, blank=True, null=True)
    manufacturer = models.CharField(max_length=150)
    line_videocard = models.CharField(max_length=150, blank=True, null=True)
    image = models.ImageField(upload_to='gpu_images/', blank=True, null=True)
    memory = models.IntegerField(help_text='Объём памяти в гб')
    type_memory = models.CharField(max_length=150, help_text='Указать какая память у видеокарты. GDDR5 or GDDR6')
    memory_bus = models.IntegerField(help_text='Указать разрядность шины памяти')
    frequency = models.IntegerField(help_text='Частота работы видеочипа')
    turbo_frequency = models.IntegerField(help_text='Частота работы видеочипа в турбобусте')
    universal_processors = models.IntegerField(blank=True, null=True)
    texture_block = models.IntegerField(blank=True, null=True)
    color = models.CharField(max_length=150, blank=True, null=True)
    TDP = models.IntegerField(blank=True, null=True)
    PCIe = models.FloatField(help_text='Указать версию PCIe')
    price = models.DecimalField(max_digits=10, decimal_places=2)
    slug = models.SlugField(unique=True, blank=True, null=True, max_length=255)
    categories = models.ForeignKey(Category, on_delete=models.SET_NULL, blank=True, null=True, related_name='gpus')

    def __str__(self):
        return self.name


class CPU(SlugifyMixin, models.Model):
    name = models.CharField(max_length=150)
    info = models.TextField(max_length=2500, blank=True, null=True)
    manufacturer = models.CharField(max_length=50)
    image = models.ImageField(upload_to='сpu_images/', blank=True, null=True)
    socket = models.CharField(max_length=50, help_text='Укажите сокет процессора')
    chipset = models.CharField(max_length=50, blank=True, null=True)
    cores = models.IntegerField()
    threads = models.IntegerField()
    base_clock = models.DecimalField(max_digits=2, decimal_places=1)
    turbo_clock = models.DecimalField(max_digits=2, decimal_places=1)
    cash_1 = models.CharField(max_length=50)
    cash_2 = models.CharField(max_length=50)
    cash_3 = models.CharField(max_length=50)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    slug = models.SlugField(unique=True, blank=True, null=True, max_length=50)
    categories = models.ForeignKey(Category, on_delete=models.SET_NULL, blank=True, null=True, related_name='cpus')

    def __str__(self):
        return self.name


class MotherBoard(SlugifyMixin, models.Model):
    name = models.CharField(max_length=150)
    info = models.TextField(max_length=2500, blank=True, null=True)
    manufacturer = models.CharField(max_length=50)
    image = models.ImageField(upload_to='motherbroad_images/', blank=True, null=True)
    form_factor = models.CharField(max_length=50)
    socket = models.CharField(max_length=50)
    chipset = models.CharField(max_length=50)
    type_memory_mb = models.CharField(max_length=50)
    memory_slots = models.IntegerField()
    M2_slots = models.IntegerField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    slug = models.SlugField(unique=True, blank=True, null=True, max_length=50)
    categories = models.ForeignKey(Category, on_delete=models.SET_NULL, blank=True, null=True, related_name='motherbroads')

    def __str__(self):
        return self.name


class PowerSupply(SlugifyMixin, models.Model):
    name = models.CharField(max_length=150)
    info = models.TextField(max_length=2500, blank=True, null=True)
    manufacturer = models.CharField(max_length=50)
    image = models.ImageField(upload_to='powersupply_images/', blank=True, null=True)
    wattage = models.IntegerField()
    certification = models.CharField(max_length=50)
    power_cpu = models.CharField(max_length=50)
    power_gpu = models.CharField(max_length=50)
    power_12W = models.IntegerField(blank=True, null=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    slug = models.SlugField(unique=True, blank=True, null=True, max_length=50)
    categories = models.ForeignKey(Category, on_delete=models.SET_NULL, blank=True, null=True, related_name='powersupplies')

    def __str__(self):
        return self.name


class Case(SlugifyMixin, models.Model):
    name = models.CharField(max_length=150)
    info = models.TextField(max_length=2500, blank=True, null=True)
    manufacturer = models.CharField(max_length=50)
    image = models.ImageField(upload_to='case_images/', blank=True, null=True)
    form_factor = models.CharField(max_length=50)
    location_power_supply = models.CharField(max_length=50)
    side_window = models.CharField(max_length=50)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    color = models.CharField(max_length=50)
    slug = models.SlugField(unique=True, blank=True, null=True, max_length=50)
    categories = models.ForeignKey(Category, on_delete=models.SET_NULL, blank=True, null=True, related_name='cases')

    def __str__(self):
        return self.name


class CoolingSystem(SlugifyMixin, models.Model):
    name = models.CharField(max_length=150)
    info = models.TextField(max_length=2500, blank=True, null=True)
    manufacturer = models.CharField(max_length=50)
    image = models.ImageField(upload_to='coolingsystem_images/', blank=True, null=True)
    max_speed = models.IntegerField()
    power_dissipation = models.IntegerField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    heat_pipes = models.IntegerField()
    slug = models.SlugField(unique=True, blank=True, null=True, max_length=50)
    categories = models.ForeignKey(Category, on_delete=models.SET_NULL, blank=True, null=True, related_name='coolingsystem')

    def __str__(self):
        return self.name


class RAM(SlugifyMixin, models.Model):
    name = models.CharField(max_length=150)
    info = models.TextField(max_length=2500, blank=True, null=True)
    manufacturer = models.CharField(max_length=50)
    image = models.ImageField(upload_to='ram_images/', blank=True, null=True)
    memory_size = models.IntegerField()
    type_memory = models.CharField(max_length=50)
    frequency_ram = models.IntegerField()
    cl = models.IntegerField(blank=True, null=True)
    tRCD = models.IntegerField(blank=True, null=True)
    tRP = models.IntegerField(blank=True, null=True)
    tRAS = models.IntegerField(blank=True, null=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    number_of_modules = models.IntegerField()
    slug = models.SlugField(unique=True, blank=True, null=True, max_length=50)
    categories = models.ForeignKey(Category, on_delete=models.SET_NULL, blank=True, null=True, related_name='ram')

    def __str__(self):
        return self.name


class StorageDevice(SlugifyMixin, models.Model):
    StorageTypes = [
        ('ssd', 'SSD Накопитель'),
        ('ssd M2', 'SSD M2 Накопитель'),
        ('HDD', 'Жёсткий диск')
    ]
    name = models.CharField(max_length=150)
    info = models.TextField(max_length=2500, blank=True, null=True)
    manufacturer = models.CharField(max_length=50)
    image = models.ImageField(upload_to='storage_images/', blank=True, null=True)
    type = models.CharField(max_length=50, choices=StorageTypes, default='ssd')
    memory_size_storage = models.IntegerField()
    max_recording_speed = models.IntegerField()
    max_reading_speed = models.IntegerField()
    TBW = models.IntegerField(blank=True, null=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    slug = models.SlugField(unique=True, blank=True, null=True, max_length=50)
    categories = models.ForeignKey(Category, on_delete=models.SET_NULL, blank=True, null=True, related_name='storagedevices')

    def __str__(self):
        return self.name


class Computer(SlugifyMixin, models.Model):
    name = models.CharField(max_length=150, blank=True, null=True)
    info = models.TextField(max_length=2500, blank=True, null=True)
    image = models.ImageField(upload_to='pc_images/', blank=True, null=True)
    gpu = models.ForeignKey(GPU, on_delete=models.CASCADE, default=1)
    cpu = models.ForeignKey(CPU, on_delete=models.CASCADE, default=1)
    motherboard = models.ForeignKey(MotherBoard, on_delete=models.CASCADE, default=1)
    ram = models.ManyToManyField(RAM, default=1)
    power_supply = models.ForeignKey(PowerSupply, on_delete=models.CASCADE, default=1)
    storage_device = models.ManyToManyField(StorageDevice, default=1)
    cooling_system = models.ForeignKey(CoolingSystem, on_delete=models.CASCADE, default=1)
    case = models.ForeignKey(Case, on_delete=models.CASCADE, default=3)
    total_price = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    slug = models.SlugField(unique=True, blank=True, null=True, max_length=50)
    categories = models.ManyToManyField(Category, related_name='computers')
    author = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True, related_name='author')


    def __str__(self):
        return self.name

    def calculate_total_price(self):
        ram_price = sum(ram.price for ram in self.ram.all())
        storage_device_price = sum(storage_device.price for storage_device in self.storage_device.all())
        self.total_price = (
            ram_price +
            storage_device_price +
            self.gpu.price +
            self.cpu.price +
            self.motherboard.price +
            self.power_supply.price +
            self.cooling_system.price +
            self.case.price
        )
        return self.total_price

class CartItem:
    def __init__(self, product_id, name, price, image):
        self.product_id = product_id
        self.name = name
        self.price = price
        self.image = image