# Дополнительное задание:
# Ты разрабатываешь программное обеспечение для сети магазинов. Каждый магазин в этой сети имеет свои особенности, но также существуют общие характеристики, такие как адрес, название и ассортимент товаров. Ваша задача — создать класс Store, который можно будет использовать для создания различных магазинов.
# Шаги:
# 1. Создай класс Store:
# -Атрибуты класса:
# name: название магазина.
# address: адрес магазина.
# items: словарь, где ключ - название товара, а значение - его цена. Например, {'apples': 0.5, 'bananas': 0.75}.
# Методы класса:
# __init__ - конструктор, который инициализирует название и адрес, а также пустой словарь дляitems`.
# -  метод для добавления товара в ассортимент.
# метод для удаления товара из ассортимента.
# метод для получения цены товара по его названию. Если товар отсутствует, возвращайте None.
# метод для обновления цены товара.
# 2. Создай несколько объектов класса Store:
# Создай не менее трех различных магазинов с разными названиями, адресами и добавь в каждый из них несколько товаров.
# 3. Протестировать методы:
# Выбери один из созданных магазинов и протестируй все его методы: добавь товар, обнови цену, убери товар и запрашивай цену.
# В поле для ответа загрузи ссылку на GitHub-репозиторий, содержащий код проекта с реализацией задания.


class Store():
    def __init__(self, name, address):
        self.name = name
        self.address = address
        self.items = {}

    def add_item(self, name_item, cost):
        # str(name_items)
        # float(cost)
        self.items[name_item] = cost

    def del_item(self, name_item):
        if name_item in self.items:
            del self.items[name_item]
            print(f'Товар удален!')
        else:
            print(f'Указанный товар не найден в магазине')

    def get_price_item(self, name_item):
        cost = self.items.get(name_item)
        if cost == None:
            print(f'Указанный товар не найден в магазине')
        else:
            print(cost)

    def update_price_item(self, name_item, cost):
        if name_item in self.items:
            self.items[name_item] = cost
        else:
            print(f"Указанный товар не найден в магазине.")


    def __str__(self):
        return f"Магазин: {self.name}, Адрес: {self.address}, Товары: {self.items}"

market1 = Store('Магазин1', 'ул. Мира, 33')

market1.add_item('Orange', 200)
market1.add_item('Apples', 250)
market1.get_price_item('Orange')
print(market1)
market1.update_price_item('Orange', 350)
market1.get_price_item('Orange')
market1.del_item('Orange')
print(market1)