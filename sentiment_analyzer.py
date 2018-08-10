from nltk.corpus import movie_reviews
from nltk.classify import NaiveBayesClassifier
from nltk.classify.util import accuracy as nltk_accuracy

# Extract features from the input list of words
def extract_feature(words):
    return dict([word, True] for word in words)

if __name__ == '__main__':
    # Load the reviews from the corpus
    fileids_pos = movie_reviews.fileids('pos')
    fileids_neg = movie_reviews.fileids('neg')

    # Extract the features from the reviews
    feature_pos = [(extract_feature(movie_reviews.words(fileids=[f])), 'Positive') for f in fileids_pos]
    feature_neg = [(extract_feature(movie_reviews.words(fileids=[f])), 'negative') for f in fileids_neg]

    # Define the train and test split (80% and 20%)
    threshold = 0.8
    num_pos = int(threshold * len(feature_pos))
    num_neg = int(threshold * len(feature_neg))

    # Create training and testing datasets
    feature_train = feature_pos[:num_pos] + feature_neg[:num_neg]
    feature_test = feature_pos[num_pos:] + feature_neg[num_neg:]

    # Print the number of datapoints used
    print('\nNumber of training datapoints:', len(feature_train))
    print('Number of test datapoints:', len(feature_test))

    # Train a Naive Bayes classifier
    classifier = NaiveBayesClassifier.train(feature_train)
    print('\nAccuracy of the classifier:', nltk_accuracy(classifier, feature_test))

    # Test input movie reviews
    N = 15
    print('\nTop ' + str(N) + ' most informative words:')
    for i, item in enumerate(classifier.most_informative_features()):
        print(str(i + 1) + '. ' + item[0])
        if i == N - 1:
            break

    input_reviews = [
        'The costumes in this movie were great',
        'I think the story was terrible and the characters were very weak',
        'People say that the director of the movie is amazing',
        'This is such an idiotic movie. I will not recommend it to anyone.'
    ]

    print('\nMovie review predictions:')
    for review in input_reviews:
        print('\nReview:', review)

        # Compute the probabilities
        probabilities =classifier.prob_classify(extract_feature(review.split()))

        # Pick the maximum value
        predicted_sentiment = probabilities.max()

        # Print outputs
        print('Predicted sentiment:', predicted_sentiment)
        print('Probability:', round(probabilities.prob(predicted_sentiment), 2))