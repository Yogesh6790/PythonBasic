obj = {}

print(obj)
obj['a'] = 'Val a'
print(obj)
obj['b'] = 'Val b'
print(obj)

print("Removed key b")
del obj['b']
print(obj)
obj['c'] = 'Val C'
obj['d'] = 'Val D'
obj['e'] = 'Val E'

print(obj)

print('Iterating....')
for key in obj:
    print(f'Key : {key}')
    print(f'Value : {obj[key]}')

obj['a'] = 'Changed A'
print(obj)
print(len(obj))
print(obj['c'])
print('The End')