# Writing to a text file
with open('accounts.txt', mode='w') as accounts:
    accounts.write('100 Yogesh\n')
    accounts.write('200 Sowmiyha\n')
    accounts.write('300 Chatresh\n')
    accounts.write('400 Family\n')

# Reading a text file
# when we read, by default we get string
with open('accounts.txt', mode='r') as accounts:
    print(f'{"Account":<10}{"Name":<10}')
    for record in accounts:
        columns = record.split()
        print(f'{columns[0]:<10}{columns[1]:<10}')

# Updating a text file
import os
accounts =  open('accounts.txt', mode='r')
temp_file = open('temp_file.txt', mode='w')

with accounts,temp_file:
    for record in accounts:
        columns = record.split()
        if str(columns[0]) != '300':
            temp_file.write(record)
        else:
            new_line = ' '.join([columns[0], 'Chatresh Yogesh'])
            temp_file.write(new_line+'\n')
os.remove('accounts.txt')
os.rename('temp_file.txt','accounts.txt')

### CSV PROCESSING
import csv
with open('accounts.csv', mode='w', newline='') as accounts:
    #create CSV writer from a file writer
    writer = csv.writer(accounts)
    writer.writerow([100,'Yogesh'])
    writer.writerow([200,'Chatresh'])
    writer.writerows([[300,'Sowmiyha'],[400,'Family']])

# when we read, by default we get list
with open('accounts.csv', mode='r', newline='') as accounts:
    reader = csv.reader(accounts)
    print(f'{"ID":<10}{"NAME":<10}')
    for record in reader:
        print(record[0], ' - ', record[1])

### JSON FILE PROCESSING
import json

grades_dict = {
    'grades': [
        {'studentid': 100, 'name':'Yogesh'},
        {'studentid': 200, 'name': 'Chatresh'}
    ]
}

with open('grades.json', mode='w') as grades:
    json.dump(grades_dict, grades)

with open('grades.json', mode='r') as grades:
    grades_json = json.load(grades)
print(grades_json)

with open('grades.json', mode='r') as grades:
    grades_json = json.dumps(json.load(grades), indent=4)
print(grades_json)
