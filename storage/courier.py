from typing import Dict

from storage.abstract_storage import AbstractStorage
from storage.request import Request


class Courier:
    def __init__(self, request: Request, storages: Dict[str, AbstractStorage]):
        self.__request = request

        self.departure: AbstractStorage = storages[self.__request.departure]
        self.destination: AbstractStorage = storages[self.__request.destination]

    def move(self):
        self.departure.remove(name=self.__request.product, amount=self.__request.amount)
        print(f"Курьер забирает {self.__request.amount} {self.__request.product} из {self.__request.departure}")
        self.destination.add(name=self.__request.product, amount=self.__request.amount)
        print(
            f"Курьер везет {self.__request.amount} {self.__request.product} "
            f"со {self.__request.departure} в {self.__request.destination}"
        )
        print(f"Курьер доставил {self.__request.amount} {self.__request.product} в {self.__request.destination}")

    def cancel(self):
        self.departure.add(name=self.__request.product, amount=self.__request.amount)
        print("Доставка отменена, товар вернулся обратно")
