n = 0
a = ["a","b","c","d","e","f",'g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']

while (n == 0):
    word1 = str(input("Введите слово на русском языке: "))
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

    

n = 0

while (n == 0):
    word2 = str(input("Введите слово на английском языке: "))
    s = []
    s = list(word2)
    
    check = 0
    for i in s:
        if i in a:
            check = check + 1
        if check == len(s):
            n = 1
    if n == 0:
        print ('')
        print ('Введите верно')

        

d = {word1 : "Русский", word2 : "Английский"}

print ("")
print (d)

