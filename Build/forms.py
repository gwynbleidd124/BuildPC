from django import forms
from django.forms import ModelForm
from .models import *

class ComputerConfigurationForm(forms.ModelForm):
    gpu = forms.ModelChoiceField(
        queryset=GPU.objects.all(),
        label="Видеокарта",
        widget=forms.Select(attrs={'class': 'gpu-select'})
    )
    cpu = forms.ModelChoiceField(
        queryset=CPU.objects.all(),
        label="Процессор",
        widget=forms.Select(attrs={'class': 'cpu-select'})
    )
    motherboard = forms.ModelChoiceField(
        queryset=MotherBoard.objects.all(),
        label="Материнская плата",
        widget=forms.Select(attrs={'class': 'motherboard-select'})
    )

    class Meta:
        model = Computer
        fields = ['name', 'gpu', 'cpu', 'motherboard', 'ram', 'storage_device', 'power_supply', 'cooling_system', 'case',]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Кастомизируем отображение значений в выпадающем списке
        self.fields['gpu'].label_from_instance = lambda obj: f"{obj.name} — {obj.memory} GB {obj.type_memory}, {obj.price} рублей"
        self.fields['cpu'].label_from_instance = lambda obj: f"{obj.name} — Сокет: {obj.socket}, Чипсеты: {obj.chipset}, {obj.cores} ядер, {obj.threads} потоков, {obj.price} рублей "
        self.fields['motherboard'].label_from_instance = lambda obj: f"{obj.name} — {obj.socket}, {obj.chipset}, {obj.price} рублей"
        self.fields['ram'].label_from_instance = lambda obj: f"{obj.name} — {obj.frequency_ram} Мгц, {obj.price} рублей"
        self.fields['storage_device'].label_from_instance = lambda obj: f"{obj.name} — {obj.price} рублей"
        self.fields['power_supply'].label_from_instance = lambda obj: f"{obj.name} — {obj.certification}, {obj.price} рублей"
        self.fields['cooling_system'].label_from_instance = lambda obj: f"{obj.name} — {obj.max_speed} о/б, {obj.power_dissipation} Ватт, {obj.price} рублей"
        self.fields['case'].label_from_instance = lambda obj: f"{obj.name} — {obj.color}, {obj.form_factor}, {obj.location_power_supply}, {obj.side_window}, {obj.price} рублей"


# class ComputerConfigurationForm(forms.ModelForm):
#     name = forms.CharField(label='Название')
#     gpu = forms.ModelChoiceField(queryset=GPU.objects.all(), label='Видеокарта')
#     cpu = forms.ModelChoiceField(queryset=CPU.objects.all(), label='Процессор')
#     motherboard = forms.ModelChoiceField(queryset=MotherBoard.objects.all(), label='Материнская плата')
#     ram = forms.ModelMultipleChoiceField(queryset=RAM.objects.all(), label='Оперативная память')
#     power_supply = forms.ModelChoiceField(queryset=PowerSupply.objects.all(), label='Блок питания')
#     storage_device = forms.ModelMultipleChoiceField(queryset=StorageDevice.objects.all(), label='Накопитель')
#     cooling_system = forms.ModelChoiceField(queryset=CoolingSystem.objects.all(), label='Система охлаждения')
#     case = forms.ModelChoiceField(queryset=Case.objects.all(), label='Корпус')
#
#     class Meta:
#         model = Computer
#         fields = ['name', 'gpu', 'cpu', 'motherboard', 'ram', 'power_supply', 'storage_device', 'cooling_system',
#                   'case']

