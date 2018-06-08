import nltk

raw_text = 'feet cats wolves talked'
tokenizer = nltk.tokenize.TreebankWordTokenizer()
tokens = tokenizer.tokenize(raw_text)

print('{:17}{}'.format('original text',':'), raw_text)
stemmer = nltk.stem.PorterStemmer()
print('{:17}{}'.format('after stemming',':'), ' '.join('{:6}'.format(stemmer.stem(token)) for token in tokens))

stemmer = nltk.stem.WordNetLemmatizer()
print('{:17}{}'.format('after lemmatizing',':'), ' '.join('{:6}'.format(stemmer.lemmatize(token)) for token in tokens))
