import json
import nltk
from nltk.corpus import stopwords, wordnet
from nltk.stem import WordNetLemmatizer
from nltk.tokenize import word_tokenize
import re

nltk.download('stopwords')
nltk.download('punkt')
nltk.download('wordnet')
nltk.download('omw-1.4') 

with open("duolingo_reviews.json", "r", encoding="utf-8") as f:
    data = json.load(f)

stop_words = set(stopwords.words('english'))
lemmatizer = WordNetLemmatizer()

def normalize_text(text):
    text = text.lower()
    text = re.sub(r'[^a-z\s]', ' ', text)
    tokens = word_tokenize(text)
    tokens = [lemmatizer.lemmatize(word) for word in tokens if word not in stop_words]
    return ' '.join(tokens)

normalized_data = []
for entry in data:
    normalized_review = normalize_text(entry['review'])
    normalized_data.append({
        "rating": entry['rating'],
        "review": normalized_review
    })

with open("normalized_reviews.json", "w", encoding="utf-8") as f:
    json.dump(normalized_data, f, indent=2, ensure_ascii=False)

print(f"Saved {len(normalized_data)} normalized reviews to 'normalized_reviews.json'")
