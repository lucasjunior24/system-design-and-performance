obj1 = {"a": True}
obj2 = obj1

obj1["a"] = "teste"

del obj1
# print(obj1["a"])
print(obj2["a"])
