from __future__ import annotations
from abc import ABC, abstractmethod

from pydantic import BaseModel


class Car(BaseModel, ABC):
    @abstractmethod
    def buscar_cliente(self): ...


class LuxoCar(Car):
    def buscar_cliente(self) -> None:
        print("Carro de luxo buscando cliente")


class PopularCar(Car):
    def buscar_cliente(self) -> None:
        print("Carro popular buscando cliente")


class CarFactory:
    @staticmethod
    def get_car(tipo: str) -> Car:
        if tipo == "luxo":
            return LuxoCar()
        if tipo == "popular":
            return PopularCar()
        assert 0, "Veiculo não existe"


if __name__ == "__main__":
    luxo_car1 = CarFactory.get_car("luxo")
    luxo_car1.buscar_cliente()

    luxo_car2 = CarFactory.get_car("popular")
    luxo_car2.buscar_cliente()

    # luxo_car3 = CarFactory.get_car("oi")
    # luxo_car3.buscar_cliente()

    luxo_car4 = CarFactory.get_car("luxo")
    luxo_car4.buscar_cliente()
