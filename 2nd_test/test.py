# Компьютерная Лингвистика
# Гордей Зуев
# Контрольная Работа за Второе полугодие

# Задание A !!!

dict = {}
with open('text_for_test.txt', encoding='utf8') as f:
  f = f.read()
  text = f.replace('?', '.').replace('!', '.').replace('...', '.')
  for sentence in text.split("."):
      dict[sentence] = len([j for j in sentence.split() if len(j)==1 ])
  length = text.split(' ')
  countw = text.count('.')

print("Среднее количество слов в предложении: ", (len(length)/countw))

n = [(value, key) for key, value in dict.items()]
print ("В предложении ", max(n)[1], " больше всего односимвольных слов: ", max(n)[0], end =' ', sep =' ') 

# Задание B !!!

import collections

def compute_tf(text):
    tf_text = collections.Counter(text)
    for i in tf_text:
        tf_text[i] = tf_text[i]/float(len(text))
    return tf_text

list = []
with open('text_for_test.txt', 'r', encoding='utf-8' ) as f:
    wrds = f.read()
    for word in wrds.split():
        list.append (wrds)

print(" ") #пустое место чтобы красиво было :)
tf_wrd = input("Введите слово, чтобы посчитать его частотность.")  
     
a = compute_tf(list)
print("Частотность слова: ", a[tf_wrd])


#Коне ц...
