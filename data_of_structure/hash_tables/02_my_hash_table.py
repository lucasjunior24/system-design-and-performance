from typing import Any


class HashTable:
    def __init__(self):
        self.data = []

    def get(self, key: str):
        value = None
        for n in self.data:
            if n[0] == key:
                value = n[1]
                break

        if value is None:
            raise Exception("This Key not exists")
        print(value)
        return value

    def set(self, key: str, value: Any):
        new_data = [key, value]
        if self.data == []:
            self.data.append(new_data)
        else:
            for n in self.data:
                if n[0] == key:
                    self.data.remove(n)

            self.data = [new_data] + self.data
        print(self.data)


table_one = HashTable()
table_one.set("Lucas", 15)
table_one.set("Pedro", 50)
table_one.set("Pedro", 60999)
table_one.set("Mateus", 50)
table_one.set("Lucas", 100)
table_one.set("Carlos", [45, 45])
table_one.set(None, "Valor None")

print()
table_one.get("Mateus")
table_one.get("Pedro")
table_one.get("Carlos")


# table_one.get("Maria")
table_one.get(None)
