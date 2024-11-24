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
            'heat_pipes': 'Количество тепловых трубок',
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

fields_for_category = {
    'Видеокарты': [
        {'field': 'manufacturer', 'label': 'Производитель'},
        {'field': 'manufacturer_chip', 'label': 'Производитель чипа'},
        {'field': 'memory', 'label': 'Память (GB)'},
        {'field': 'type_memory', 'label': 'Тип памяти'},
        {'field': 'memory_bus', 'label': 'Разрядность шины памяти (бит)'},
        {'field': 'frequency', 'label': 'Частота видеопроцессора (МГц)'},
        {'field': 'turbo_frequency', 'label': 'Частота в турбобусте (МГц)'},
        {'field': 'universal_processors', 'label': 'Число универсальных процессоров:'},
        {'field': 'texture_block', 'label': 'Текстурных блоков:'},
        {'field': 'TDP', 'label': 'TDP(Вт)'},
        {'field': 'PCIe', 'label': 'PCIe'},
        {'field': 'color', 'label': 'Цвет'},
        {'field': 'price', 'label': 'Цена (рублей)'},
    ],
    'Процессоры': [
        {'field': 'manufacturer', 'label': 'Производитель'},
        {'field': 'socket', 'label': 'Сокет'},
        {'field': 'chipset', 'label': 'Чипсет'},
        {'field': 'cores', 'label': 'Ядер'},
        {'field': 'threads', 'label': 'Потоков'},
        {'field': 'base_clock', 'label': 'Базовая частота (МГц)'},
        {'field': 'turbo_clock', 'label': 'Частота в турбобоусте(МГц)'},
        {'field': 'cash_1', 'label': 'Кеш 1-го уровня'},
        {'field': 'cash_2', 'label': 'Кеш 2-го уровня'},
        {'field': 'cash_3', 'label': 'Кеш 3-го уровня'},
        {'field': 'price', 'label': 'Цена (рублей)'},
    ],
    'Материнские платы': [
        {'field': 'manufacturer', 'label': 'Производитель'},
        {'field': 'form_factor', 'label': 'Форм фактор'},
        {'field': 'chipset', 'label': 'Чипсет'},
        {'field': 'type_memory_mb', 'label': 'Тип памяти'},
        {'field': 'memory_slots', 'label': 'Количество слотов памяти'},
        {'field': 'M2_slots', 'label': 'Количество M2 слотов'},
        {'field': 'price', 'label': 'Цена (рублей)'}
    ],
    'Блоки Питания': [
        {'field': 'manufacturer', 'label': 'Производитель'},
        {'field': 'wattage', 'label': 'Мощность(Ватт)'},
        {'field': 'power_12W', 'label': 'Мощность по 12-ти вольтовой линии(Ватт)'},
        {'field': 'certification', 'label': 'Сертификат'},
        {'field': 'power_cpu', 'label': 'Разъёмы для питания процессора'},
        {'field': 'power_gpu', 'label': 'Разъёмы для питания видеокарты'},
        {'field': 'price', 'label': 'Цена (рублей)'}
    ],
    'Корпуса': [
        {'field': 'manufacturer', 'label': 'Производитель'},
        {'field': 'form_factor', 'label': 'Форм фактор'},
        {'field': 'color', 'label': 'Цвет'},
        {'field': 'location_power_supply', 'label': 'Расположение блока питания'},
        {'field': 'side_window', 'label': 'Наличие бокового окна'},
        {'field': 'price', 'label': 'Цена (рублей)'}
    ],
    'Охлаждение для процессора': [
        {'field': 'manufacturer', 'label': 'Производитель'},
        {'field': 'max_speed', 'label': 'Максимальная скорость вращение'},
        {'field': 'power_dissipation', 'label': 'Рассеиваемая мощность'},
        {'field': 'heat_pipes', 'label': 'Количество тепловых трубок'},
        {'field': 'price', 'label': 'Цена (рублей)'}
    ],
    'Оперативная память': [
        {'field': 'manufacturer', 'label': 'Производитель'},
        {'field': 'type_memory', 'label': 'Тип памяти'},
        {'field': 'memory_size', 'label': 'Количество памяти'},
        {'field': 'number_of_modules', 'label': 'Количество модулей памяти'},
        {'field': 'frequency_ram', 'label': 'Частота памяти'},
        {'field': 'cl', 'label': 'cl'},
        {'field': 'tRCD', 'label': 'tRCD'},
        {'field': 'tRP', 'label': 'tRP'},
        {'field': 'tRAS', 'label': 'tRAS'},
        {'field': 'price', 'label': 'Цена (рублей)'}
    ],
    'Накопители': [
        {'field': 'manufacturer', 'label': 'Производитель'},
        {'field': 'type', 'label': 'Тип накопителя'},
        {'field': 'memory_size_storage', 'label': 'Количество памяти'},
        {'field': 'max_reading_speed', 'label': 'Максимальная скорость чтения'},
        {'field': 'max_recording_speed', 'label': 'Максимальная скорость чтения'},
        {'field': 'TBW', 'label': 'TBW'},
        {'field': 'price', 'label': 'Цена (рублей)'}
    ]
}

FIELD_LABELS = {
    'gpu': 'Видеокарта',
    'cpu': 'Процессор',
    'motherboard': 'Материнская плата',
    'ram': 'Оперативная память',
    'power_supply': 'Блок питания',
    'case': 'Корпус',
    'storage_device': 'Накопитель',
    'cooling_system': 'Охлаждение процессора',
}
