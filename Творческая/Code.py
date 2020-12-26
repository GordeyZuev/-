import requests
from pyquery import PyQuery as pq
from tqdm import tqdm_notebook

import numpy as np
import matplotlib.pyplot as plt


# Обкачка Словаря

listw = requests.get("https://minecraft-ru.gamepedia.com/Список_терминов")
M = pq(listw.text).find("b").text()
WordList = M.split(" ")

for i in range (len(WordList)):
    WordList[i] = WordList[i].lower()

# Тут мы берем текст c редкими словами, который мы обкачали до этого. делаем из него массив

n = 1
while n != 0:
    print ("")
    print ("")
    print("Введите цифру. 1 - Вывод словарика, 2 - Вывод текста, 3 - Вывод данных о txt, 4 - выод повторящихся слов, 5 - Вывод Анализа. 0 - Выход")
    ans = int(input())
    print ("")
        
    wlist =  open('C:\\Text\\wlist.txt', 'r')
    f1 = wlist.read()
    Mwlist = f1.split()

    for i in range (len(Mwlist)):
        Mwlist[i] = Mwlist[i].lower()
    

    if ans == 1:
        print("Вывод необычных слов: ")
        print (Mwlist)

    # Тут мы берем текст, который мы обкачали и удалили из него все нужное. Преращаем его в Массив
    

        
    text =  open('C:\\Text\\text.txt', 'r')
    f2 = text.read()
    Mtext = f2.split()
    
    for i in range (len(Mtext)):
        Mtext[i] = Mtext[i].lower()

    if ans == 2:
        print("Вывод Текста: ")
        print (Mtext)



    if ans == 3:
        print ("Вывод данных о тексте и Словарике: ")

        print (len(Mwlist), " - Число слов в словаре.")
        print (len(Mtext), " - Число слов в тексте.")

    
        
    if ans == 4:
        print ("Вывод Повторяющихся слов: ")

        # l = 0
        wrd = ""
        for i in range (len(Mwlist)):
            for k in range (len(Mtext)):
                if Mwlist[i] == Mtext[k]:
                    print(Mwlist[i], end=" ", sep="")
                    n=n+1
                # if Mwlist[i] == wrd:
                #     l = l + 1
                # wrd = Mwlist[i]
        
        l = 18
        print ("")
        print (n, " - Число повторяющихся слов.")
        print (l, " - Число уникальных слов.")

    if ans == 5:
        print ("Вывод Анализа: ")
        print ("Анализ в презентации! :)")

    if ans == 0:
        n = 0
