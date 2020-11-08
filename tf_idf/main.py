from collections import Counter
import math

def compute_tfidf(corpus):

    def compute_tf(text):

        tf_text = Counter(text)

        for i in tf_text:

            tf_text[i] = tf_text[i]/float(len(text))

        return tf_text

    def compute_idf(word, corpus):

        return math.log10(len(corpus)/sum([1.0 for i in corpus if word in i]))

 

    documents_list = []

    for text in corpus:

        tf_idf_dictionary = {}

        computed_tf = compute_tf(text)

        for word in computed_tf:

            tf_idf_dictionary[word] = computed_tf[word] * compute_idf(word, corpus)

        documents_list.append(tf_idf_dictionary)

    return documents_list

text1 = ['my','name','is','Gordey', 'an', 'i', 'am', 'sixteen', 'years', 'old', 'and', 'i', 'enjoy', 'eating', 'pizza']
text2 = ['me','and','my','brother', 'play', 'football', 'every', 'weer', 'and', 'we', 'do', 'it', 'very', 'well']

corpus = [text1, text2]


print (compute_tfidf(corpus))
