# dictionaries 2

# multiple dictionarys inside a list

a = {'name':'smith'}
b = {'name':'sawyer'}
c = {'name':'tawin'}

list = [a,b,c]

for dictionary in list:
    print(dictionary)

#generating identical dictionaries to store in a list

for number_dicts in range(10):
    new_dict = {'name':'junior'}
    list.append(new_dict)
print(f"total lenght of list is {len(list)}")

# chaning multiple dictionaries in a list

for dictionary in list[:3]:
    if dictionary['name'] == 'smith' or 'sawyer' or 'tawin':
        dictionary['name'] = 'junior'
print(list)

# lists inside of dictionarys to store more than one value per key

users = []

user_data = {'user_1':["1.butcc","1234565"],
             'user_2':["2.uzsifhj","3875zfg"],
             'user_3':["3.asd78z4hoit","2387rfhdf8"],
             'user_4':["4.sadufghd","213485ur9tg8"],
             'user_5':["5.sdiuhfg","28tu34958t"],
             'user_6':["6.273zrh7er","3984tzh3"],
             'user_7':["7.9784tzr34t","32498th3"],
             }

#printing every key and its corresponding values
for k,v in user_data.items():
    #if statements to check if dictionaries have atleast 2 values
    if len(v) >= 2 :     
        print(f"{k} your username and password is:\n\t {v}")

# dictionaries inside of dictionaries

persons = {'buttfucker3000':
                            {'first':'alber','last':'einstein','location':'Miami'},
           'ToiletDestroyer':
                            {'first':'tom','last':'','location':'Utah'},
           'gnomish_child_fondler':
                            {'first':'Peter','last':'Griffin','location':'Quahog'},
           
           }

for username,userinfo in persons.items():
    print(f"{username}, your Fullname is {userinfo['first'].title()} {userinfo['last'].title()} and you live in {userinfo['location'].title()}")