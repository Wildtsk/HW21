from typing import Dict

from exceptions import NotEnoughSpaceError, NotEnoughProductError
from storage.abstract_storage import AbstractStorage


class BaseStorage(AbstractStorage):
    def __init__(self, items: Dict[str, int], capacity: int):
        self.__items = items
        self.__capacity = capacity

    def add(self, name: str, amount: int) -> None:          #`add`( < название >, < количество >)  - увеличивает запас items
        if self.get_free_space() < amount:      #выведет ошибку что на складе недостаточно места.
            raise NotEnoughSpaceError

        if name in self.__items:
            self.__items[name] += amount
        else:
            self.__items[name] = amount

    def remove(self, name: str, amount: int) -> None:       #`remove`( < название >, < количество >) - уменьшает запас items
        if name not in self.__items or self.__items[name] < amount:     #выведет ошибку: на складе недостаточно товара.
            raise NotEnoughProductError

        self.__items[name] -= amount
        if self.__items[name] == 0:
            self.__items.pop(name)

    def get_free_space(self) -> int:   #`get_free_space()` - вернуть количество свободных мест
        return self.__capacity - sum(self.__items.values())

    def get_items(self):        #`get_items()` - возвращает сожержание склада в словаре {товар: количество}
        return self.__items

    def get_unique_items_count(self):   #`get_unique_items_count()` - возвращает количество уникальных товаров.
        return len(self.__items)


