tempList  = []

# 1) adding elements to the list
tempList.append('a')
tempList.append('b')
print(tempList)
tempList.append('c')
tempList.append('d')
tempList.append('d')
print(tempList)

# 2) find an index
print(f"Index {tempList.index('c')}")

# 3) iterate through list
for val in tempList:
    print(f'Element {val}')

# 4) finding length of the list
print(f'Length of the list : {len(tempList)}')

# 5) iterate through the list with index
for num in range(len(tempList)):
    print(tempList[num])

index  = 0
while index < len(tempList):
    print(tempList[index])
    index += 1

print('Removed elem')
# 6) Removing element from the list
del(tempList[1])
tempList.remove('c')
print(tempList)


# 7) Poping elem
print(tempList.pop())
print(tempList.pop())
print(tempList)

# 8) Reassigning elems
tempList[0] = 'z'
print(tempList)

tempList.append('n')
tempList.append('m')
tempList.append('i')
print(tempList)
# 9) printing only elements from q range iof indices
print(tempList[2:3])

#10) remving duplicates with set method
tempList.append('i')
print(tempList)
print(set(tempList))

#11) form list in a single line
listVar = ['_ ' for letter in 'Hello']
print(listVar)

squares = [n**2 for n in range(10)]
print(squares)

