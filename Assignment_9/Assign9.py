import nltk
import re
import string
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize, sent_tokenize
from nltk.probability import FreqDist
from nltk.stem import PorterStemmer, LancasterStemmer, WordNetLemmatizer
nltk.download('punkt')
nltk.download('stopwords')
nltk.download('wordnet')
nltk.download('omw-1.4')

# Question 1: Favorite Topic Paragraph i.e technology
text = """I love exploring the world of artificial intelligence. It's fascinating how machines can learn and mimic human behavior.
From self-driving cars to voice assistants, AI has transformed technology. It is revolutionizing industries and solving complex problems.
Learning about neural networks, natural language processing, and deep learning excites me.
The future of AI holds endless possibilities and continuous innovation."""

# 1. Convert to lowercase and remove punctuation
text_lower = text.lower().translate(str.maketrans('', '', string.punctuation))

# 2. Tokenize text into words and sentences
word_tokens = word_tokenize(text_lower)
sentence_tokens = sent_tokenize(text_lower)

# 3. Remove stopwords
stop_words = set(stopwords.words('english'))
filtered_words = [word for word in word_tokens if word not in stop_words]

# 4. Word Frequency Distribution
freq_dist = FreqDist(filtered_words)

print("Word Frequency Distribution (Excluding Stopwords):")
for word, freq in freq_dist.items():
    print(f"{word}: {freq}")

# Question 2: Stemming and Lemmatization
porter = PorterStemmer()
lancaster = LancasterStemmer()
lemmatizer = WordNetLemmatizer()

# Apply stemming
porter_stemmed = [porter.stem(word) for word in filtered_words]
lancaster_stemmed = [lancaster.stem(word) for word in filtered_words]

# Apply lemmatization
lemmatized = [lemmatizer.lemmatize(word) for word in filtered_words]

print("\nPorter Stemmer:", porter_stemmed)
print("Lancaster Stemmer:", lancaster_stemmed)
print("Lemmatized Words:", lemmatized)

# Question 3: Regular Expressions and Text Splitting
# a. Extract all words with more than 5 letters
words_5plus = re.findall(r'\b\w{6,}\b', text)
print("\nWords with more than 5 letters:", words_5plus)

# b. Extract all numbers
numbers = re.findall(r'\b\d+\b', text)
print("Numbers in text:", numbers)

# c. Extract all capitalized words
capitalized_words = re.findall(r'\b[A-Z][a-z]*\b', text)
print("Capitalized words:", capitalized_words)

# Text splitting:
# a. Split text into words with only alphabets
alpha_words = re.findall(r'\b[a-zA-Z]+\b', text)
print("Alphabetic words only:", alpha_words)

# b. Extract words starting with a vowel
vowel_words = re.findall(r'\b[aeiouAEIOU]\w*\b', text)
print("Words starting with a vowel:", vowel_words)

# Question 4: Custom Tokenization and Regex-based Text Cleaning
def custom_tokenizer(text):
    # Remove punctuation but keep contractions
    cleaned = re.sub(r"[^\w\s'-]", '', text)
    # Handle hyphenated words and decimals
    tokens = re.findall(r"[A-Za-z]+(?:-[A-Za-z]+)*|\d+\.\d+|\d+", cleaned)
    return tokens

custom_tokens = custom_tokenizer(text)
print("\nCustom Tokens:", custom_tokens)

# Regex Substitutions
sample_text = "Contact me at john.doe@example.com or visit https://openai.com. My number is +91 9876543210 or 123-456-7890."

# Replace email addresses
sample_text = re.sub(r'\b[\w.-]+?@\w+?\.\w+?\b', '<EMAIL>', sample_text)

# Replace URLs
sample_text = re.sub(r'(https?://\S+)', '<URL>', sample_text)

# Replace phone numbers
sample_text = re.sub(r'(\+?\d{1,3}\s?\d{10})|(\d{3}-\d{3}-\d{4})', '<PHONE>', sample_text)

print("Text after Substitutions:", sample_text)