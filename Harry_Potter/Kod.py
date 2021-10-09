import re 


#file = open('Garri_Potter_I_Filosofsky_Kamen.txt','r')
file = open('Garri_Potter_I_Dary_Smerti.txt','r')
f2 = file.read()

f2 = (f2.translate({ord(i): None for i in ','}))
f2 = (f2.translate({ord(i): None for i in '.'}))
f2 = (f2.translate({ord(i): None for i in '-'}))
f2 = (f2.translate({ord(i): None for i in '«'}))
f2 = (f2.translate({ord(i): None for i in '»'}))
f2 = (f2.translate({ord(i): None for i in '!'}))
f2 = (f2.translate({ord(i): None for i in '?'}))
f2 = (f2.translate({ord(i): None for i in ';'}))
f2 = (f2.translate({ord(i): None for i in ':'}))
f2 = (f2.translate({ord(i): None for i in ')'}))
f2 = (f2.translate({ord(i): None for i in '('}))


text = f2.split() # Разделение


#name_forms = (re.findall(r'(Хагрид|Гермион|Дамблдор)[а|е|ы|у|ой|ом]', f2)) не работает и ладно
name_forms = (re.findall(r'Дамблдор[а |у |ом|ы |ов|овский|ова]|Хагрид[а |ы |у |ом|ов|овский|ова]|Гермион[а |е |ы |у |ой|овский|ин]', f2))

for i in range (len(name_forms)):
    name_forms[i] = name_forms[i].lower()

    
name_forms_list = (list(set(name_forms))) #массив с неповторяющимися Формами имени
name_forms_list.sort()


for i in range (len(name_forms_list)):
    name_forms_list[i] = name_forms_list[i].lower()


for i in range (len(name_forms_list)):
    print(name_forms_list[i])
    n = 0
    for k in range (len(name_forms)):
        if name_forms[k] == name_forms_list[i]:
            n = n + 1
    print(n)
    print(' ')
