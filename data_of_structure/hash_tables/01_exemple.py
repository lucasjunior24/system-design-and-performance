def scream():
    print("aaaaaaa")


user = {"age": 45, "name": "Lucas", "magic": True, "scream": scream}

print(user["age"])
print(user["magic"])
user["scream"]()
print()
user["spell"] = "Abra kadabra"
print(user)
