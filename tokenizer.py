import nltk
text = "This is Liam's text, isn't it?"

tokenizer = nltk.tokenize.WhitespaceTokenizer()
print('WhitespaceTokenizer:', tokenizer.tokenize(text))

tokenizer = nltk.tokenize.TreebankWordTokenizer()
print('TreebankWordTokenizer:', tokenizer.tokenize(text))

tokenizer = nltk.tokenize.WordPunctTokenizer()
print('WordPunctTokenizer:', tokenizer.tokenize(text))
