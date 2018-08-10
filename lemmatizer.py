from nltk.stem import WordNetLemmatizer

# Create lemmatizer object
input_words = ['writing', 'calves', 'be', 'branded', 'horse', 'randomize',
               'possibly', 'provision', 'hospital', 'kept', 'scratchy', 'code']

# Create a list of lemmatizer names for display
lemmatizer = WordNetLemmatizer()

lemmatizer_names = ['Noun Lemmatizer', 'Verb Lemmatizer']
formatted_text = '{:>16}' * (len(lemmatizer_names) + 1)
print('\n', formatted_text.format('INPUT WORD', *lemmatizer_names), '\n', '='*68)

# Lemmatize each word and display the output
for word in input_words:
    output = [word, lemmatizer.lemmatize(word, pos='n'), lemmatizer.lemmatize(word, pos='v')]
    print('\n', formatted_text.format(*output))
