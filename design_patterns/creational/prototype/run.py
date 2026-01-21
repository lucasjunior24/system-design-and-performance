from __future__ import annotations

print(
    "O Prototype especifica os tipos dos objetos a serem criados, usando uma intancia-protótipo e cria novos objetos pela copia desse protótipo"
)

from typing import List
from pydantic import BaseModel
from copy import deepcopy


class Person(BaseModel):
    firstname: str
    lastname: str
    addresses: List[Address] = []

    def add_address(self, address: Address):
        self.addresses.append(address)

    def clone(self) -> Person:
        return deepcopy(self)


class Address(BaseModel):
    street: str
    number: str


print()
if __name__ == "__main__":
    luca = Person(firstname="Luca", lastname="puza")
    endereco_luca = Address(street="Rua jacinto", number="2645")
    luca.add_address(endereco_luca)

    lara = luca.clone()
    lara.firstname = "Lara"
    print(luca)
    print(lara)
