import csv
import json
import os
what_to_process = ''
while what_to_process != 'N':
    what_to_process = input('Enter input file type : ')
    if what_to_process == 'CSV':
        print('**** Writing CSV started ******')
        with open('test_accounts.csv', mode='w', newline='') as test_accounts:
            test_accounts_csv_writer = csv.writer(test_accounts)
            test_accounts_csv_writer.writerows([[100, 'Yogesh'], [200, 'Sowmiyha'], [300, 'Chatresh']])
            test_accounts_csv_writer.writerow([400, 'Aruna'])
            test_accounts_csv_writer.writerow(['**** This is our family ****'])
        print('**** Writing CSV completed ******')

        try:
            print('Reading CSV file started')
            with open('test_accounts.csv',mode='r',newline='') as test_accounts:
                test_accounts_csv_reader = csv.reader(test_accounts)
                for record in test_accounts_csv_reader:
                    print(record)
                    print(record[0], '-', record[1]) if len(record) > 1 else print(record[0])
        except FileNotFoundError:
            print('File is not found')
        else:
            print('No exceptions found while reading csv file')
        finally:
            print('Reading CSV file is completed')
    elif what_to_process == 'TXT':
        print('*** Writing text file is started ***')
        with open('test_accounts.txt',mode='w') as test_accounts:
            test_accounts.write('Hello Yogesh\n')
            test_accounts.write('Hello Sowmiyha\n')
            test_accounts.write('Hello Chatresh\n')
            test_accounts.write('Hello Aruna\n')
            test_accounts.write('Uhh! Hello to the family')
        print('*** Writing text file is completed ***')

        print('*** Reading text file is started ***')
        try:
            with open('test_accounts.txt',mode='r') as test_accounts_txt:
                for record in test_accounts_txt:
                    columns = record.split()
                    print('{1}-{0}'.format(columns[0], columns[1]))
        except FileNotFoundError:
            print('No file found error')
        else:
            print('No exceptions found while reading text file')
        finally:
            print('*** Reading txt file completed ***')
    elif what_to_process == 'JSON':
        family_json = {
            100: 'Yogesh',
            200: 'Sowmiyha',
            300: 'Chatresh',
            400: 'Aruna',
            'Hello': 'Greeting',
            'deliverables' : ['Passport', 'DP', 'PR', 3]
        }
        print('****** Writing of JSON is started ******')
        with open('test_accounts.json', mode='w') as test_accounts_json:
            json.dump(family_json, test_accounts_json)
        print('****** Writing of JSON is completed ******')

        try:
            print('**** Reading of JSON started ****')
            with open('test_accounts.json', mode='r') as test_accounts_json:
                test_accounts = json.dumps(json.load(test_accounts_json), indent=2)
                print(test_accounts)
        except Exception as e:
            print(str(e))
        else:
            print('No exceptions found while reading json')
        finally:
            print('**** Reading of JSON completed ****')
    elif what_to_process == 'REMOVE':
        print('**** Going to remove files ****')
        try:
            os.remove('test_accounts.txt')
            os.remove('test_accounts.csv')
            os.remove('test_accounts.json')
            x = 4
        except FileNotFoundError as fr:
            print(str(fr))
        else:
            print('No exceptions found while removing', 4)
        finally:
            print('***  Files removing process completed ***')
    else:
        print('Not a valid format!! Try again!')




