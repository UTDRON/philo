import json
from wordcloud import WordCloud
import matplotlib.pyplot as plt
from collections import Counter

with open("normalized_reviews.json", "r", encoding="utf-8") as f:
    data = json.load(f)

all_text = " ".join(entry['review'] for entry in data)

word_counts = Counter(all_text.split())

max_freq = max(word_counts.values())
inverted_freq = {word: max_freq - freq + 1 for word, freq in word_counts.items()}

wordcloud = WordCloud(
    width=800,
    height=400,
    background_color='white',
    colormap='viridis',
    max_words=200
).generate_from_frequencies(inverted_freq)

plt.figure(figsize=(15, 7.5))
plt.imshow(wordcloud, interpolation='bilinear')
plt.axis('off')
plt.title("Inverse Word Cloud of Normalized Duolingo Reviews", fontsize=18)
plt.show()
