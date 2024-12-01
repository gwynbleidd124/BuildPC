from lib2to3.fixes.fix_input import context

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

import requests
from bs4 import BeautifulSoup



class HomePage(TemplateView):
    template_name = 'Build/index.html'

class BuildsPC(ListView):
    model = Computer
    template_name = 'Build/buildspc.html'
    context_object_name = 'computers'

    def get_queryset(self):
        # Передаем записи с индексами 0, 1 и 4
        computers = Computer.objects.prefetch_related('ram').order_by('total_price')
        return [computers[i] for i in [0, 1, 2, 3, 4] if i < len(computers)]

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Передаем записи с индексами 5 и 7
        computers = Computer.objects.prefetch_related('ram').order_by('total_price')
        context['selected_computer'] = [computers[i] for i in [5, 6, 7, 8, 9] if i < len(computers)]
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


class List_accessories(ListView):
    model = Category
    template_name = 'Build/accessories.html'
    context_object_name = 'categories'

    def get_queryset(self):
        return Category.objects.all()[3:]


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


# test # test # test # test # test # test # test # test # test # test # test # test # test # test # test # test # test # test # test

def add_to_configurator(request, category, pk):
    category_models = {
        'Видеокарты': GPU,
        'Процессоры': CPU,
        'Материнские платы': MotherBoard,
        'Оперативная память': RAM,
        'Блоки Питания': PowerSupply,
        'Корпуса': Case,
        'Накопители': StorageDevice,
        'Охлаждение для процессора': CoolingSystem,
    }

    model = category_models.get(category)
    if not model:
        return JsonResponse({'error': 'Неверная категория'}, status=400)

    item = get_object_or_404(model, pk=pk)
    configurator = request.session.get('configurator', {})

    configurator[category] = item.id
    request.session['configurator'] = configurator
    request.session.modified = True

    return redirect('current_configurator')


def current_configurator(request):
    configurator = request.session.get('configurator', {})
    category_models = {
        'Видеокарты': GPU,
        'Процессоры': CPU,
        'Материнские платы': MotherBoard,
        'Оперативная память': RAM,
        'Блоки Питания': PowerSupply,
        'Накопители': StorageDevice,
        'Корпуса': Case,
        'Охлаждение для процессора': CoolingSystem,
    }

    category_slug = {
        'Видеокарты': 'videocarty',
        'Процессоры': 'protsessory',
        'Материнские платы': 'materinskie-platy',
        'Оперативная память': 'operativnaja-pamjat',
        'Блоки Питания': 'bloki-pitanija',
        'Корпуса': 'korpus',
        'Накопители': 'nakopiteli',
        'Охлаждение для процессора': 'ohlazhdenie-dlja-protsessora',
    }

    selected_items = []
    for category, slug in category_slug.items():
        model = category_models.get(category)
        item = model.objects.filter(pk=configurator.get(category)).first() if model else None
        selected_items.append({
            'category': category,
            'slug': slug,
            'item': item,
        })

    return render(request, 'Build/current_configurator.html', {'selected_items': selected_items})


def save_configurator(request):
    CATEGORY_MAPPING = {
        'Видеокарты': 'gpu',
        'Процессоры': 'cpu',
        'Материнские платы': 'motherboard',
        'Оперативная память': 'ram',
        'Блоки Питания': 'power_supply',
        'Корпуса': 'case',
        'Накопители': 'storage_device',
        'Охлаждение для процессора': 'cooling_system',
    }

    configurator = request.session.get('configurator', {})

    # Преобразуем ключи с помощью CATEGORY_MAPPING
    normalized_configurator = {
        CATEGORY_MAPPING[key]: value
        for key, value in configurator.items()
        if key in CATEGORY_MAPPING
    }
    print("Преобразованный конфигуратор:", normalized_configurator)

    # Проверяем наличие обязательных полей
    required_fields = ['gpu', 'cpu', 'motherboard', 'ram', 'power_supply', 'case', 'storage_device', 'cooling_system',]
    missing_fields = [field for field in required_fields if normalized_configurator.get(field) in [None, '', 0]]

    if missing_fields:
        print("Отсутствуют обязательные компоненты:", missing_fields)

        # Используем FIELD_LABELS для преобразования технических названий в пользовательские
        missing_labels = [FIELD_LABELS.get(field, field) for field in missing_fields]

        error_message = f'Не выбраны обязательные компоненты: {", ".join(missing_labels)}'

        return render(request, 'Build/error_configurate.html', {'error_message': error_message})


    # Создаем объект сборки
    computer = Computer(
        name=request.POST.get('name', 'Сборка ПК'),
        gpu=GPU.objects.filter(pk=normalized_configurator.get('gpu')).first(),
        cpu=CPU.objects.filter(pk=normalized_configurator.get('cpu')).first(),
        motherboard=MotherBoard.objects.filter(pk=normalized_configurator.get('motherboard')).first(),
        power_supply=PowerSupply.objects.filter(pk=normalized_configurator.get('power_supply')).first(),
        case=Case.objects.filter(pk=normalized_configurator.get('case')).first(),
        cooling_system=CoolingSystem.objects.filter(pk=normalized_configurator.get('cooling_system')).first(),
    )

    computer.save()  # Сохраняем объект

    # Для ManyToManyField используем set()
    if normalized_configurator.get('ram'):
        ram_objects = RAM.objects.filter(pk__in=[normalized_configurator.get('ram')])
        computer.ram.set(ram_objects)

    if normalized_configurator.get('storage_device'):
        storage_objects = StorageDevice.objects.filter(pk__in=[normalized_configurator.get('storage_device')])
        computer.storage_device.set(storage_objects)

    computer.calculate_total_price()
    computer.save()

    # Очищаем сессию
    request.session['configurator'] = {}
    request.session.modified = True

    return redirect('current_configurator')

def add_to_comparison(request, category, pk):
    category_models = {
        'Видеокарты': GPU,
        'Процессоры': CPU,
        'Материнские платы': MotherBoard,
        'Оперативная память': RAM,
        'Блоки Питания': PowerSupply,
        'Корпуса': Case,
        'Накопители': StorageDevice,
        'Охлаждение для процессора': CoolingSystem,
    }

    model = category_models.get(category)
    if model is None:
        return JsonResponse({'error': 'Неверная категория'}, status=400)

    item = get_object_or_404(model, pk=pk)
    comparison = request.session.get('comparison', {})

    if category not in comparison:
        comparison[category] = []

    if len(comparison[category]) == 2:
        comparison[category].pop(0)

    if pk not in comparison[category]:
        comparison[category].append(pk)

    request.session['comparison'] = comparison
    request.session.modified = True

    return redirect('comparison')

def comparison(request):
    comparison = request.session.get('comparison', {})

    category_models = {
        'Видеокарты': GPU,
        'Процессоры': CPU,
        'Материнские платы': MotherBoard,
        'Оперативная память': RAM,
        'Блоки Питания': PowerSupply,
        'Корпуса': Case,
        'Накопители': StorageDevice,
        'Охлаждение для процессора': CoolingSystem,
    }

    # Поля для отображения


    comparison_data = {}
    for category, ids in comparison.items():
        model = category_models.get(category)
        if model:
            items = model.objects.filter(pk__in=ids)
            prepared_items = []
            for item in items:
                fields = [
                    {'label': field['label'], 'value': getattr(item, field['field'], None)}
                    for field in fields_for_category.get(category, [])
                ]
                prepared_items.append({'name': item.name, 'fields': fields, 'image': item.image, 'id': item.id})
            comparison_data[category] = prepared_items

    return render(request, 'Build/comparison.html', {'comparison_data': comparison_data})


def remove_from_comparison(request, category, pk):
    comparison = request.session.get('comparison', {})
    if category in comparison and pk in comparison[category]:
        comparison[category].remove(pk)
        if not comparison[category]:  # Если список пуст, удалить категорию
            del comparison[category]
        request.session['comparison'] = comparison
        request.session.modified = True
    return redirect('comparison')


# def fetch_prices(url):
#     try:
#         # Выполняем HTTP-запрос
#         response = requests.get(url)
#         response.raise_for_status()  # Проверяем успешность запроса
#
#         # Анализируем HTML-страницу
#         soup = BeautifulSoup(response.text, 'html.parser')
#
#         # Ищем все элементы с классом 'price'
#         price_elements = soup.select('.price')  # select возвращает список всех элементов
#
#         if price_elements:
#             # Извлекаем текст для каждой найденной цены
#             prices = [price_element.get_text(strip=True) for price_element in price_elements]
#             return prices
#         else:
#             return ["Цены не найдены"]
#
#     except Exception as e:
#         return [f"Ошибка: {e}"]
#
# def price_view(request):
#     url = 'https://dinakom.net/index.php?route=product/category&path=60_96'  # URL страницы с ценами
#     prices = fetch_prices(url)  # Получаем все цены
#     return render(request, 'Build/price.html', {'prices': prices})

