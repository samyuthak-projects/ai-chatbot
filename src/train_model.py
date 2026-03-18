from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB

# training data
texts = [
    "hello", "hi", "hey", "good morning",
    "how are you", "how are you doing",
    "what is your name", "who are you",
    "bye", "goodbye", "see you later"
]

labels = [
    "greeting", "greeting", "greeting", "greeting",
    "how_are_you", "how_are_you",
    "name", "name",
    "goodbye", "goodbye", "goodbye"
]

vectorizer = CountVectorizer()
X = vectorizer.fit_transform(texts)

model = MultinomialNB()
model.fit(X, labels)

print("Model trained successfully!")