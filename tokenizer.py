from nltk.tokenize import sent_tokenize, word_tokenize, WordPunctTokenizer, WhitespaceTokenizer, TreebankWordTokenizer

# Define input text
input_text = "Do you know how tokenization workds? It's actually quite interesting! Let's analyze a couple of" \
             " sentences and figure it out."

# Sentence tokenizer
print('\nSentence tokenizer:')
print(sent_tokenize(input_text))

print('\nWord tokenizer:')
print(word_tokenize(input_text))

print('\nWord punct tokenizer:')
print(WordPunctTokenizer().tokenize(input_text))

print('\nTree bank word tokenizer:')
print(TreebankWordTokenizer().tokenize(input_text))

print('\nWhite space tokenizer:')
print(WhitespaceTokenizer().tokenize(input_text))

#tokenizer = WhitespaceTokenizer()
#print('WhitespaceTokenizer:', tokenizer.tokenize(input_text))

#tokenizer = TreebankWordTokenizer()
#print('TreebankWordTokenizer:', tokenizer.tokenize(input_text))

#tokenizer = WordPunctTokenizer()
#print('WordPunctTokenizer:', tokenizer.tokenize(input_text))
