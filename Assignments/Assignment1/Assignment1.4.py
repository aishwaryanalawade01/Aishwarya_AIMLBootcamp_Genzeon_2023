x = ('key1', 'key2', 'key3')
y = 0

thisdict = dict.fromkeys(x, y)

print(thisdict)

car = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}

x = car.copy()
print(x)
print(car.get("model"))
print(car.items())
print(car.keys())
car.pop("model")
print(car)
car.popitem()

print(car)
x = car.setdefault("model", "Bronco")
print(x)
car.update({"color": "White"})

print(car)
x = car.values()

print(x)
car.clear()
print(car)
