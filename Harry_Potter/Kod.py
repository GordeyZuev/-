# Гордей Зуев, Илья Свиридов, Арсений Смирнов ;)

import re

k1 = open('Garri-Potter-I-Prints-Polukrovka.txt','r')           #(1) (на три гермионы показывает больше...)
k2 = open('Garri_Potter_I_Dary_Smerti.txt','r')                 #(1) (на одну гермиону показывает больше...)
k3 = open('Garri_Potter_I_Kubok_Ognya.txt','r')                 #(1)
k4 = open('Garri_Potter_I_Orden_Fenixa.txt','r')                #(1)
k5 = open('Garri_Potter_I_Taynaya_Komnata.txt','r')             #(1)
k6 = open('Garri_Potter_I_Uznik_Azkabana.txt','r')              #(1)
k7 = open('Garri_Potter_I_Filosofsky_Kamen.txt','r')            #(1)

ans = -1
pas = int(input('Выберете вариант отобржения: '))


while ans != 0:
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
    if ans == 0:
        print('')
        print('До свидания!')
    
    
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

    
    if (ans<8) and (ans>0):
        #С помощью Регулярных Выржения ищем нужное
        name_forms = (re.findall(r'д[а-я]мбл[а-я]{0,1}дор[а-я]{0,6}|[а-я]{1,2}грид[а-я]{0,6}|гермион[а-я]{0,6}', f2))


        #num_germ = (len(re.findall(r'гермион[ ,а,е,ы,у,ой,ин,овский]', f2)))
        # 
        num_germ = (len(re.findall(r'гермион[а-я]{0,6}', f2)))                              # Формы Имени Гермиона

        num_hagr = (len(re.findall(r'[а-я]{1,2}грид[а-я]{0,6}', f2)))                       # Формы Имени Хагрид (Огрид)

        num_damb = (len(re.findall(r'д[а-я]мбл[а-я]{0,1}дор[а-я]{0,6}', f2)))               # Формы Имени Дамблдор (Думбльдор)
    
        print('')
        print('')
        print('Книга ',(ans), '; Количество форм Имен: ', sep='')
        print('')

        print('Форм имени Гермиона: ', (num_germ))

        print('Форм имени Дамблдор (Думбльдор): ', (num_damb))

        print('Форм Имени Хагрид (Огрид):', (num_hagr))

        print('')

        name_forms_list = (list(set(name_forms)))                       # Массив с неповторяющимися Формами имени
        name_forms_list.sort()


        if pas == 1:
            print('Формы Имен и их количество: ')
            print('')
            for i in range (len(name_forms_list)):                      # Цикл, выводящий форму имени и количество этих форм
                print(name_forms_list[i])
                n = 0
                for k in range (len(name_forms)):
                    if name_forms[k] == name_forms_list[i]:
                        n = n + 1
                print(n)
                print('')



# Гордей Зуев, Илья Свиридов, Арсений Смирнов ;)
# Сотая строка для Красоты
