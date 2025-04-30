import re
import nltk
from nltk.tokenize import word_tokenize, sent_tokenize
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer, WordNetLemmatizer
from sklearn.feature_extraction.text import CountVectorizer, TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from collections import Counter
from wordcloud import WordCloud
import matplotlib.pyplot as plt
from textblob import TextBlob
from keras.preprocessing.text import Tokenizer
from keras.models import Sequential
from keras.layers import Embedding, LSTM, Dense
import numpy as np

nltk.download('punkt')
nltk.download('stopwords')
nltk.download('wordnet')

# Q1: Text Preprocessing and Tokenization
paragraph = """Artificial Intelligence is transforming the world rapidly. Machines are now learning and adapting like humans.
From healthcare to finance, AI is solving complex problems. It helps automate tasks and predict future outcomes.
AI is also driving innovation in autonomous vehicles and robotics.
The future of AI looks bright and limitless."""

# Lowercase and remove punctuation
clean_text = re.sub(r'[^\w\s]', '', paragraph.lower())

# Tokenize into words and sentences
words_split = clean_text.split()
words_nltk = word_tokenize(clean_text)
sentences = sent_tokenize(clean_text)

# Compare Python split() vs NLTK word_tokenize()
print("Python split:", words_split)
print("NLTK word_tokenize:", words_nltk)

# Remove stopwords
stop_words = set(stopwords.words('english'))
filtered_words = [word for word in words_nltk if word not in stop_words]

# Frequency Distribution
freq = Counter(filtered_words)
print("Word Frequency (without stopwords):", freq)

# Q2: Extraction, Stemming, Lemmatization
alpha_words = re.findall(r'\b[a-zA-Z]+\b', clean_text)
filtered_alpha = [word for word in alpha_words if word not in stop_words]

stemmer = PorterStemmer()
lemmatizer = WordNetLemmatizer()

stemmed = [stemmer.stem(word) for word in filtered_alpha]
lemmatized = [lemmatizer.lemmatize(word) for word in filtered_alpha]

print("\nStemmed:", stemmed)
print("Lemmatized:", lemmatized)
print("Explanation: Stemming is quick but can produce non-words, lemmatization is grammar-aware and gives real words — preferable for clean NLP pipelines.")

# Q3: Feature Extraction with CountVectorizer and TF-IDF
texts = [
    "AI is the future of technology.",
    "Blockchain provides secure digital transactions.",
    "Natural language processing enables machines to understand human language."
]

cv = CountVectorizer()
bow = cv.fit_transform(texts)
print("\nBag of Words:", bow.toarray())

tfidf = TfidfVectorizer()
tfidf_matrix = tfidf.fit_transform(texts)
feature_names = tfidf.get_feature_names_out()

for i, text_vector in enumerate(tfidf_matrix):
    scores = zip(feature_names, text_vector.toarray()[0])
    sorted_scores = sorted(scores, key=lambda x: x[1], reverse=True)
    top_keywords = [word for word, score in sorted_scores[:3]]
    print(f"Text {i+1} Top 3 Keywords:", top_keywords)

# Q4: Similarity Calculations
text1 = """Artificial Intelligence enables machines to learn and improve automatically based on data."""
text2 = """Blockchain is a secure, decentralized system that records transactions across many computers."""

# Preprocess
def preprocess(text):
    return set(re.sub(r'[^\w\s]', '', text.lower()).split())

set1, set2 = preprocess(text1), preprocess(text2)

# Jaccard Similarity
jaccard = len(set1.intersection(set2)) / len(set1.union(set2))
print("\nJaccard Similarity:", jaccard)

# Cosine Similarity
vectorizer = TfidfVectorizer()
vectors = vectorizer.fit_transform([text1, text2])
cos_sim = cosine_similarity(vectors[0:1], vectors[1:2])[0][0]
print("Cosine Similarity:", cos_sim)

print("Insight: Jaccard works on overlap but ignores importance, Cosine uses frequency weight, usually better for text analysis.")

# Q5: Sentiment Analysis and Word Cloud
review = "The new smartphone is amazing with great features but the battery life is short."
blob = TextBlob(review)
print("\nSentiment Polarity:", blob.sentiment.polarity)
print("Subjectivity:", blob.sentiment.subjectivity)

# Classification
if blob.sentiment.polarity > 0:
    sentiment = "Positive"
elif blob.sentiment.polarity < 0:
    sentiment = "Negative"
else:
    sentiment = "Neutral"
print("Review Sentiment:", sentiment)

# Word Cloud
positive_reviews = "This laptop is excellent. Great performance and fantastic battery life."
wordcloud = WordCloud(background_color='white').generate(positive_reviews)

plt.imshow(wordcloud, interpolation='bilinear')
plt.axis('off')
plt.show()

# Q6: Text Generation with Keras
train_text = """Artificial intelligence enables machines to learn from data, improving their performance with experience. AI applications include image recognition, natural language processing, and autonomous vehicles."""

tokenizer = Tokenizer()
tokenizer.fit_on_texts([train_text])
sequences = []

total_words = len(tokenizer.word_index) + 1
token_list = tokenizer.texts_to_sequences([train_text])[0]

for i in range(1, len(token_list)):
    sequences.append(token_list[:i+1])

sequences = np.array(sequences)
X, y = sequences[:,:-1], sequences[:,-1]
y = np.eye(total_words)[y]

# Simple Model
model = Sequential([
    Embedding(total_words, 10, input_length=X.shape[1]),
    LSTM(50),
    Dense(total_words, activation='softmax')
])

model.compile(loss='categorical_crossentropy', optimizer='adam', metrics=['accuracy'])
model.fit(X, y, epochs=500, verbose=0)

# Generate Text
seed_text = "Artificial intelligence"
next_words = 3

for _ in range(next_words):
    token_list = tokenizer.texts_to_sequences([seed_text])[0]
    token_list = np.pad(token_list, (X.shape[1] - len(token_list), 0), 'constant')
    predicted = np.argmax(model.predict(token_list.reshape(1, -1), verbose=0), axis=-1)
    for word, index in tokenizer.word_index.items():
        if index == predicted:
            seed_text += " " + word
            break

print("\nGenerated Text:", seed_text)

