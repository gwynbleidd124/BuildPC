from django.contrib import admin

from Build.models import *

models = [Computer, GPU, CPU, MotherBoard, PowerSupply, Case, CoolingSystem, RAM, StorageDevice, Category]

admin.site.register(models)