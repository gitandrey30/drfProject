import json

d= {"name": 'Johan', 'age': 18, 'stack': 'Python'}
print(type(d))
d.json

ser = json.dump(d)
print(ser)
print(type(ser))
print(d)
print(type(d))