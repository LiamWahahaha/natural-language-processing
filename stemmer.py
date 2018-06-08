import nltk

raw_test_string = 'feet cats wolves talked'

test_string = raw_test_string.split(' ')

stemmer = nltk.stem.porter.PorterStemmer()

print(test_string)

for string in test_string:
    print(stemmer.stem(string))
