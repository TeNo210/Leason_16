import json
person = {
    'name': 'Max',
    'age':10,
    'phones': ['9111', '738333']
}
spisok = ['orange','12' '321']
result = json.dumps(person)
result2 = json.dumps(spisok)
print(result)
print(type(result))
print(result2)
print(type(result2))

