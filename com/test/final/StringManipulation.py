
# 1)  Iterate through the string
word = input('Enter thr word : ')
counter = 0
for letter in word:
    if letter in ['a','e','i','o','u']: #if letter in 'aeiou'
        counter += 1

print(counter)

word2 = input('Enter thr word 2 : ')
counter2 = 0
for letter in word2:
    if letter in 'aeiou':
        counter2 += 1

print(counter2)

counter3 = 0;
for index in range(0,len(word)-2):
    if word[index] == 'm':
        counter3 += 1
    # print(word[index])
print(f'm Counter : {counter3}')

# 2) length of string
print(f'Length : {len(word)}')

# 3) print a character at a index
print(f'Char at index 0 : {word[0]}')

# 4) parse to string
print(f'Parse to String : {str(7)}')

# 5) check if string equals
print("aaa" == "ab")

# 6) find index of a string
print("abcd".find("bc"))

# 7) substring
print(word[1:4])


# 8) form string from list
strTemp = ' '+' '.join(['-','-','-']) + ' '
print(strTemp)
print(len(strTemp))
strTemp = strTemp.strip()
print(strTemp)
print(len(strTemp))
# print(' '.join(['- ','- ','- ']))
