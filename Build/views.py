from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.paginator import Paginator
from django.http import HttpResponse, request, Http404, JsonResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse, reverse_lazy
from django.views import View
from django.views.generic import TemplateView, ListView, DetailView, CreateView, FormView

from . import apps
from .attributes import *

import Build
from Build.forms import *
from Build.models import *


class HomePage(TemplateView):
    template_name = 'Build/index.html'

class BuildsPC(ListView):
    model = Computer
    template_name = 'Build/buildspc.html'
    context_object_name = 'computers'

    def get_queryset(self):
        # Передаем записи с индексами 0, 1 и 4
        computers = Computer.objects.prefetch_related('ram').order_by('total_price')
        return [computers[i] for i in [0, 1, 4] if i < len(computers)]

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Передаем записи с индексами 5 и 7
        computers = Computer.objects.prefetch_related('ram').order_by('total_price')
        context['selected_computer'] = [computers[i] for i in [5, 7] if i < len(computers)]
        return context


class ComponentDetailView(DetailView):
    template_name = 'Build/component_detail.html'  # Один универсальный шаблон
    context_object_name = 'component'  # Общий контекст для всех компонентов

    CATEGORY_MODELS = {
        'videocarty': (GPU, 'gpu'),
        'protsessory': (CPU, 'cpu'),
        'materinskie-platy': (MotherBoard, 'motherboard'),
        'operativnaja-pamjat': (RAM, 'ram'),
        'korpus': (Case, 'case'),
        'nakopiteli': (StorageDevice, 'storage_device'),
        'bloki-pitanija': (PowerSupply, 'power_supply'),
        'ohlazhdenie-dlja-protsessora': (CoolingSystem, 'cooling_system'),
    }

    def get_object(self):
        component_type = self.kwargs.get('component_type')
        model, _ = self.CATEGORY_MODELS.get(component_type, (None, None))

        if not model:
            raise ValueError(f"Неподдерживаемый тип компонента: {component_type}")

        return get_object_or_404(model, pk=self.kwargs.get('pk'))

    def get_context_data(self, **kwargs):
        component = self.get_object()
        context = super().get_context_data(**kwargs)
        component_type = self.kwargs.get('component_type')
        component_fields = {field: (label, getattr(component, field, None))
                            for field, label in fields.items()
                            if hasattr(component, field) and getattr(component, field) is not None}

        context['component_fields'] = component_fields
        context['category'] = component_type  # передаём тип категории для использования в шаблоне
        return context


class ComputerDetail(DetailView):
    model = Computer
    template_name = 'Build/Computer_detail.html'
    context_object_name = 'computer'

    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     # Получение комплектующих
    #     context['gpus'] = self.object.gpu
    #     context['cpus'] = self.object.cpu
    #     context['motherboards'] = self.object.motherboard
    #     context['rams'] = self.object.ram
    #     context['powersupplies'] = self.object.power_supply
    #     context['cases'] = self.object.case
    #     context['storage_devices'] = self.object.storage_device
    #     context['cooling_systems'] = self.object.cooling_system
    #     return context


class List_accessories(ListView):
    model = Category
    template_name = 'Build/accessories.html'
    context_object_name = 'categories'

    def get_queryset(self):
        return Category.objects.all()[3:]


class PCConfigurateView(LoginRequiredMixin, CreateView):
    model = Computer
    template_name = 'Build/configuratepc.html'
    form_class = ComputerConfigurationForm
    success_url = reverse_lazy('configuratepc')
    login_url = reverse_lazy('users:login')

    def form_valid(self, form):
        computer = form.save(commit=False)
        computer.author = self.request.user

        # Проверка на совместимость процессора и материнской платы
        if computer.cpu and computer.motherboard:
            if computer.cpu.socket != computer.motherboard.socket:
                form.add_error('motherboard',
                               'Выбранная материнская плата несовместима с этим процессором!Выберите другой сокет!')
                return self.form_invalid(form)
        if computer.motherboard and computer.case:
            if computer.motherboard.form_factor == 'ATX' and computer.case.form_factor == 'Mini-Tower':
                form.add_error('case', 'Выбранный корпус слишком маленький для данной материнской платы!')
                return self.form_invalid(form)

        # Подсчет общей стоимости
        total_price = 0
        if computer.gpu:
            total_price += computer.gpu.price
        if computer.cpu:
            total_price += computer.cpu.price
        if computer.motherboard:
            total_price += computer.motherboard.price
        if computer.power_supply:
            total_price += computer.power_supply.price
        if computer.cooling_system:
            total_price += computer.cooling_system.price
        if computer.case:
            total_price += computer.case.price

        total_price += sum(ram.price for ram in form.cleaned_data['ram'])
        total_price += sum(storage_device.price for storage_device in form.cleaned_data['storage_device'])

        computer.total_price = total_price
        computer.save()

        form.save_m2m()
        return super().form_valid(form)





class CategoryItemsView(ListView):
    template_name = 'Build/list_accessories.html'
    context_object_name = 'items'
    paginate_by = 12

    CATEGORY_MODELS = {
        'Видеокарты': GPU,
        'Процессоры': CPU,
        'Материнские платы' : MotherBoard,
        'Оперативная память': RAM,
        'Блоки Питания': PowerSupply,
        'Корпуса': Case,
        'Накопители': StorageDevice,
        'Охлаждение для процессора': CoolingSystem,
    }

    def get_queryset(self):
        # Получаем категорию по слагу из URL
        category = Category.objects.get(slug=self.kwargs['slug'])
        model = self.CATEGORY_MODELS[category.name]
        queryset = model.objects.all() if model else []
        if not model:
            return []

        queryset = model.objects.all()

        filters = {
            'price__gte': self.request.GET.get('price_min'),
            'price__lte': self.request.GET.get('price_max'),
            'wattage__gte': self.request.GET.get('wattage_min'),
            'wattage__lte': self.request.GET.get('wattage_max'),
            'max_speed__gte': self.request.GET.get('max_speed_min'),
            'max_speed__lte': self.request.GET.get('max_speed_max'),
            'memory_size__gte': self.request.GET.get('memory_size_min'),
            'memory_size__lte': self.request.GET.get('memory_size_max'),
            'power_dissipation__gte': self.request.GET.get('power_dissipation_min'),
            'power_dissipation__lte': self.request.GET.get('power_dissipation_max'),
            'heat_pipes__gte': self.request.GET.get('heat_pipes_min'),
            'heat_pipes__lte': self.request.GET.get('heat_pipes_max'),
            'manufacturer__icontains': self.request.GET.get('manufacturer'),
            'manufacturer_chip__icontains': self.request.GET.get('manufacturer_chip'),
            'form_factor__iexact': self.request.GET.get('form_factor'),
            'socket__icontains': self.request.GET.get('socket'),
            'chipset__icontains': self.request.GET.get('chipset'),
            'memory__icontains': self.request.GET.get('memory'),
            'memory_slots__icontains': self.request.GET.get('memory_slots'),
            'certification__icontains': self.request.GET.get('certification'),
            'color__icontains': self.request.GET.get('color'),
            'location_power_supply__icontains': self.request.GET.get('location_power_supply'),
            'side_window__icontains': self.request.GET.get('side_window'),
            'memory_size__icontains': self.request.GET.get('memory_size'),
            'type_memory__icontains': self.request.GET.get('type_memory'),
            'frequency__icontains': self.request.GET.get('frequency'),
            'type__iexact': self.request.GET.get('type'),
            'line_videocard__icontains': self.request.GET.get('line_videocard'),
        }

        for field, value in filters.items():
             if value:
                 queryset = queryset.filter(**{field: value})

        order_by = self.request.GET.get('order_by')
        gpu_order_by = self.request.GET.get('gpu_order_by')
        if order_by:
            queryset = queryset.order_by('price' if order_by == 'asc' else '-price')
        if gpu_order_by:
            queryset = queryset.order_by('memory' if gpu_order_by == 'asc' else '-memory')

        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        category = Category.objects.get(slug=self.kwargs['slug'])
        category_attributes = CATEGORY_ATTRIBUTES.get(category.name, {})

        # Передаем данные текущей категории в контекст
        context.update({
            'category': category,
            **category_attributes  # Разворачиваем атрибуты категории
        })
        return context

class BuildPCUsers(ListView):
    model = Computer
    template_name = 'Build/BuildPCUsers.html'
    context_object_name = 'computer'
    paginate_by = 12

    def get_queryset(self):
        queryset = Computer.objects.all()

        filters = {
            'total_price__gte': self.request.GET.get('total_price_min'),
            'total_price__lte': self.request.GET.get('total_price_max'),
            'gpu__manufacturer_chip__icontains': self.request.GET.get('gpu__manufacturer_chip'),
            'gpu__manufacturer__icontains': self.request.GET.get('gpu__manufacturer'),
            'gpu__line_videocard__icontains': self.request.GET.get('gpu'),
            'gpu__memory__icontains': self.request.GET.get('gpu__memory'),
            'cpu__manufacturer__icontains': self.request.GET.get('cpu__manufacturer'),
            'cpu__socket__icontains': self.request.GET.get('socket'),
            'ram__type_memory': self.request.GET.get('ram__type_memory'),
            'ram__memory_size': self.request.GET.get('ram__memory_size'),
            'power_supply__certification': self.request.GET.get('power_supply__certification'),
            'case__color': self.request.GET.get('case__color'),
            'case__side_window': self.request.GET.get('case__side_window'),
        }

        for field, value in filters.items():
             if value:
                 queryset = queryset.filter(**{field: value})

        order_by = self.request.GET.get('order_by')
        if order_by:
            queryset = queryset.order_by('total_price' if order_by == 'asc' else '-total_price')

        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        category_attributes = filters_pc.get('Компьютеры', {})
        context.update({
            **category_attributes  # Разворачиваем атрибуты категории
        })
        return context
