from nltk.stem import WordNetLemmatizer

raw_text = 'running lying cars m!spleed feet cats wolves talked'

text = raw_text.split(' ')

wnl = WordNetLemmatizer()

for word in text:
    print('{} -> {}'.format(word, wnl.lemmatize(word)))
