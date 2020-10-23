n = 0
a = ["a","b","c","d","e","f",'g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']

while (n == 0):
    word1 = str(input("Введите слово на русском языке: "))
    word1 = (word1.lower())
    s = []
    s = list(word1)
    
    check = 0
    for i in s:
        if i in a:
            check = check + 1
        if check == 0:
            n = 1
    if n == 0:
        print ('')
        print ('Введите верно') 

while (n == 1):
    word2 = str(input("Введите слово на английском языке: "))
    word2 = (word2.lower())
    s = []
    s = list(word2)
    
    check = 0
    for i in s:
        if i in a:
            check = check + 1
        if check == len(s):
            n = 0
    if n == 1:
        print ('')
        print ('Введите верно')

print ("")
print ("Русское Слово - ", word1, "Английское слово - ", word2)

