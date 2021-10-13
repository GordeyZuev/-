import re

k1 = open('Garri_Potter_I_Dary_Smerti.txt','r') 
k2 = open('Garri_Potter_I_Dary_Smerti.txt','r')
k3 = open('Garri_Potter_I_Kubok_Ognya.txt','r') 
k4 = open('Garri_Potter_I_Orden_Fenixa.txt','r')
k5 = open('Garri_Potter_I_Taynaya_Komnata.txt','r') 
k6 = open('Garri_Potter_I_Uznik_Azkabana.txt','r') 
k7 = open('Garri_Potter_I_Filosofsky_Kamen.txt','r')

ans = int(input('Введите номер произведения: '))
if ans == 1:
    file = k1                   # Не декодирует
if ans == 2:
    file = k2                   # Не декодирует
if ans == 3:
    file = k3                   # Декодирует
if ans == 4:
    file = k4                   # Декодирует
if ans == 5:
    file = k5                   # Декодирует
if ans == 6:
    file = k6                   # Декодирует
if ans == 7:
    file = k7                   # Декодирует
    
f2 = file.read()                                                        # Открытие и Чтение Файла

f2 = (f2.translate({ord(i): None for i in ','}))                        # Убираем все лишние символы
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

f2 = f2.lower()


#С помощью Регулярных Выржения ищем нужное
name_forms = (re.findall(r'д[а,у]мбл[ ,ь]дор[а-я]{0,6}|[ха,о]грид[а-я]{0,6}|гермион[а-я]{0,6}', f2))


#num_germ = (len(re.findall(r'гермион[ ,а,е,ы,у,ой,ин,овский]', f2)))
# 
num_germ = (len(re.findall(r'гермион[а-я]{0,6}', f2)))              # Формы Имени Гермиона

num_hagr = (len(re.findall(r'[ха,о]грид[а-я]{0,6}', f2)))                       # Формы Имени Хагрид (Огрид)

num_damb = (len(re.findall(r'д[а,у]мбл[ ,ь]дор[а-я]{0,6}', f2)))          # Формы Имени Дамблдор (Думбльдор)
    
    
print('')
print('Инормация о формах имен Героев: ')

print('Количество форм Имени Гермиона: ', (num_germ))

print('Количество форм Имени Дамблдор (Думбльдор): ', (num_damb))

print('Количество форм Имени Хагрид (Огрид):', (num_hagr))

print('')

name_forms_list = (list(set(name_forms)))               # Массив с неповторяющимися Формами имени
name_forms_list.sort()

print('Формы Имен и их количество: ')


for i in range (len(name_forms_list)):                  # Цикл, выводящий форму имени и количество этих форм
    print(name_forms_list[i])
    n = 0
    for k in range (len(name_forms)):
        if name_forms[k] == name_forms_list[i]:
            n = n + 1
    print(n)
    print(' ')
