CATEGORY_ATTRIBUTES = {
    'Видеокарты': {
        'manufacturer': ['MSI', 'GIGABYTE', 'Palit', 'Sapphire', 'ASRock', 'KFA2', 'Colorful', 'PowerColor'],
        'manufacturer_chip': ['AMD', 'NVIDIA'],
        'line_videocard': ['GTX 1600', 'RTX 2000', 'RTX 3000', 'RTX 4000', 'RX 500', 'RX 6000', 'RX 7000'],
        'color': ['Чёрный', 'Белый', 'Серый', 'Чёрно-белый']
    },
    'Процессоры': {
        'manufacturer': ['Intel', 'AMD'],
        'socket': ['AM4', 'AM5', 'LGA1200', 'LGA1700'],
        'chipset': ['A420', 'A520', 'A620', 'B450', 'B550', 'B650', 'H610', 'B760', 'Z790']
    },
    'Материнские платы': {
        'manufacturer': ['ASUS', 'MSI', 'Gigabyte'],
        'form_factor': ['ATX', 'Micro-ATX', 'Mini-ITX'],
        'socket': ['AM4', 'AM5', 'LGA1200', 'LGA1700'],
        'chipset': ['A420', 'A520', 'A620', 'B450', 'B550', 'B650'],
        'memory': ['DDR4', 'DDR5'],
        'memory_slots': [2, 4],
    },
    'Блоки Питания': {
        'manufacturer': ['be quiet!', 'chieftec', 'thermaltake', 'FSP', 'deepcool', 'zalman'],
        'certification': ['Отсутствует', '80+ Standart', '80+ Bronze', '80+ Gold', '80+ Platinum', '80+ Titanium'],
    },
    'Корпуса': {
        'manufacturer': ['Cougar', 'Zalman', 'Ardor Gaming', 'DEXP', 'Montech'],
        'color': ['Чёрный', 'Белый', 'Серый', 'Красный'],
        'location_power_supply': ['Верхнее', 'Нижнее'],
        'side_window': ['Есть', 'Нет'],
    },

    'Охлаждение для процессора': {
        'manufacturer': ['DEEPCOOL', 'ID-COOlING', 'PCCooler', 'Ardor Gaming'],
    },

    'Оперативная память': {
        'manufacturer': ['Kingston', 'ADATA', 'G.SKILL'],
        'memory_size': [8, 16, 32, 64],
        'type_memory': ['DDR4', 'DDR5'],
        'frequency': [3200, 4800, 5200, 5600, 6000],
    },
    'Накопители': {
        'manufacturer': ['Kingston', 'Samsung', 'Surveillance', 'BarraCuda', 'WD BLUE', 'TOSHIBA', 'ADATA', 'Apacer'],
        'type': ['ssd', 'ssd M2', 'HDD'],
    }
}

filters_pc = {
    'Компьютеры': {
        'gpu__manufacturer': ['MSI', 'GIGABYTE', 'Palit', 'Sapphire', 'ASRock', 'KFA2', 'Colorful'],
        'gpu': ['GTX 1600', 'RTX 2000', 'RTX 3000', 'RTX 4000', 'RX 500', 'RX 6000', 'RX 7000'],
        'gpu__manufacturer_chip': ['AMD', 'NVIDIA'],
        'gpu__memory': [4, 6, 8, 12, 16, 20],
        'socket': ['AM4', 'AM5', 'LGA1200', 'LGA1700'],
        'cpu__manufacturer': ['Intel', 'AMD'],
        'ram__type_memory': ['DDR4', 'DDR5'],
        'ram__memory_size': [8, 16, 32, 64],
        'power_supply__certification': ['Отсутствует', '80+ standart', '80+ bronze', '80+ gold', '80+ platinum', '80+ titanium'],
        'case__color': ['Чёрный', 'Белый', 'Серый', 'Чёрно-белый'],
        'case__side_window': ['Есть', 'Нет']
    }
}


fields = {
            #общее
            'manufacturer': 'Производитель',
            # Видеокарты
            'manufacturer_chip': 'Производитель видеочипа',
            'memory': 'Память (GB)',
            'type_memory': 'Тип памяти',
            'memory_bus': 'Разрядность шины памяти (бит)',
            'frequency': 'Частота видеопроцессора (МГц)',
            'turbo_frequency': 'Частота в турбобусте (МГц)',
            'universal_processors': 'Число универсальных процессоров',
            'texture_block': 'Текстурных блоков',
            'TDP': 'TDP (Вт)',
            'PCIe': 'PCIe',
            #процессоры и материнские платы
            'form_factor': 'Форм фактор',
            'socket': 'Сокет',
            'chipset': 'Чипсет',
            #процессоры
            'cores': 'Ядер',
            'threads': 'Потоков',
            'base_clock': 'Базовая частота (МГц)',
            'turbo_clock': 'Частота в турбобусте (МГц)',
            'cash_1': 'Кеш 1-го уровня',
            'cash_2': 'Кеш 2-го уровня',
            'cash_3': 'Кеш 3-го уровня',
            #материнские платы
            'type_memory_mb': 'Тип памяти',
            'memory_slots': 'Количество слотов памяти',
            'M2_slots': 'Количество M2 слотов',
            #оперативная память и накопители
            'memory_size': 'Количество памяти',
            #Оперативная память
            'number_of_modules': 'Количество модулей памяти',
            'frequency_ram': 'Частота памяти',
            'cl': 'cl',
            'tRCD': 'tRCD',
            'tRP': 'tRP',
            'tRAS': 'tRAS',
            #Блоки питания
            'wattage': 'Мощность(Ватт)',
            'power_12W': 'Мощность по 12-ти вольтовой линии(Ватт)',
            'certification': 'Сертификат',
            'power_cpu': 'Разъёмы для питания процессора',
            'power_gpu': 'Разъёмы для питания видеокарты',
            #Охлаждение для процессора
            'max_speed': 'Максимальная скорость вращение',
            'power_dissipation': 'Рассеиваемая мощность',
            'heat_pipes': 'Количество телповых трубок',
            #Накопители
            'type': 'Тип накопителя',
            'memory_size_storage': 'Количество памяти',
            'max_recording_speed': 'Максимальная скорость чтения',
            'max_reading_speed': 'Максимальная скорость чтения',
            'TBW': 'TBW',
            #Корпуса
            'color': 'Цвет',
            'location_power_supply': 'Расположение блока питания',
            'side_window': 'Наличие бокового окна',
            #общее
            'categories': 'Категория',
            'price': 'Цена (рублей)',

        }

