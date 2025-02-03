# Ein paar Übungen, die ich sehr interessant finde, um den Umgang mit Dictionaries und Listen zu üben
# und wie man diese miteinander kombieren kann

# mehrere verschiedene Dicts innerhalb einer Liste speichern

a = {'name':'smith'}
b = {'name':'sawyer'}
c = {'name':'tawin'}

list = [a,b,c]

for dictionary in list:
    print(dictionary)

#for schleife um identische Dicts zu generieren und innerhalb einer Liste zu speichern
for number_dicts in range(10):
    new_dict = {'name':'junior'}
    list.append(new_dict)
print(f"total lenght of list is {len(list)}")

# for schleife um 'values' innerhalb mehrerer Dicts innerhalb einer Liste zu verändern
for dictionary in list[:3]:
    if dictionary['name'] == 'smith' or 'sawyer' or 'tawin':
        dictionary['name'] = 'junior'
print(list)

# Listen als 'values' innerhalb eines Dicts
# erlauben es mehr als einen Wert als 'value' zu speichern
users = []

user_data = {'user_1':["1.butcc","1234565"],
             'user_2':["2.uzsifhj","3875zfg"],
             'user_3':["3.asd78z4hoit","2387rfhdf8"],
             'user_4':["4.sadufghd","213485ur9tg8"],
             'user_5':["5.sdiuhfg","28tu34958t"],
             'user_6':["6.273zrh7er","3984tzh3"],
             'user_7':["7.9784tzr34t","32498th3"],
             }

# for schleife um jedes einzelne 'key' und 'value' paar anzuzeigen
for k,v in user_data.items():
    # if statement um sicher zu gehen, dass 'value' mindestens 2 Werte hat
    if len(v) >= 2 :     
        print(f"{k} your username and password is:\n\t {v}")

# Dictionaries die als 'value' innerhalb von übergeordneten Dictionaries befinden
persons = {'FlashbangFury':
                            {'first':'alber','last':'einstein','location':'Miami'},
           'ToiletDestroyer':
                            {'first':'tom','last':'','location':'Utah'},
           'NeonVortex':
                            {'first':'Peter','last':'Griffin','location':'Quahog'},
           
           }
# for Schleife mit f-String um Informationen aus obigem Dictionary zu holen
for username,userinfo in persons.items():
    print(f"{username}, your Fullname is {userinfo['first'].title()} {userinfo['last'].title()} and you live in {userinfo['location'].title()}")
