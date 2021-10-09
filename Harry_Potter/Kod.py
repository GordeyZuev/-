import re

ans = int(input('Введите номер произведения: '))
if ans == 1:
    file = open('Garri_Potter_I_Dary_Smerti.txt','r')
if ans == 2:
    file = open('Garri-Potter-I-Prints-Polukrovka.txt','r')         # С этим текстом проблема
if ans == 3:
    file = open('Garri_Potter_I_Kubok_Ognya.txt','r') 
if ans == 4:
    file = open('Garri_Potter_I_Orden_Fenixa.txt','r') 
if ans == 5:
    file = open('Garri_Potter_I_Taynaya_Komnata.txt','r') 
if ans == 6:
    file = open('Garri_Potter_I_Uznik_Azkabana.txt','r') 
if ans == 7:
    file = open('Garri_Potter_I_Filosofsky_Kamen.txt','r')
    
f2 = file.read()                                                    # Открытие и Чтение Файла

f2 = (f2.translate({ord(i): None for i in ','}))                    #Убираем все лишние символы
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

text = f2.split()                                                   #Превращаем Текст В Массив



#С помощью Регулярных Выржения ищем нужное
name_forms = (re.findall(r'Д[а|у]мбльдор[а |у |ом|ы |ов|овский|ова]|[Ха|О]грид[а |ы |у |ом|ов|овский|ова]|Гермион[а |е |ы |у |ой|овский|ин]', f2))


num_germ = (len(re.findall(r'Гермион[а |е |ы |у |ой|овский|ин]', f2)))          # Формы Имени Гермиона

num_hagr = (len(re.findall(r'[Ха|О]грид[а |ы |у |ом|ов|овский|ова]', f2)))      # Формы Имени Хагрид (Огрид)

num_damb = (len(re.findall(r'Д[а|у]мбльдор[а |у |ом|ы |ов|овский|ова]', f2)))  # Формы Имени Дамблдор (Думбльдор)
    
print('')
print('Инормация о формах имен Героев: ')

print('Количество форм Имени Гермиона: ', (num_germ))

print('Количество форм Имени Дамблдор (Думбльдор): ', (num_damb))

print('Количество форм Имени Хагрид (Огрид):', (num_hagr))

print('')

name_forms_list = (list(set(name_forms)))                                       #Массив с неповторяющимися Формами имени
name_forms_list.sort()



for i in range (len(name_forms)):                                               #Делаем все ячейки массива без заглавных букв
    name_forms[i] = name_forms[i].lower()

for i in range (len(name_forms_list)):
    name_forms_list[i] = name_forms_list[i].lower()

print('Формы Имен и их количество: ')

for i in range (len(name_forms_list)):                                          #Цикл, выводящий форму имени и количество этих форм
    print(name_forms_list[i])
    n = 0
    for k in range (len(name_forms)):
        if name_forms[k] == name_forms_list[i]:
            n = n + 1
    print(n)
    print(' ')
