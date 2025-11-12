import json
from wordcloud import WordCloud
import matplotlib.pyplot as plt
from collections import Counter

with open("normalized_reviews.json", "r", encoding="utf-8") as f:
    data = json.load(f)

all_text = " ".join(entry['review'] for entry in data)

tokens = all_text.split()

trigrams = [" ".join(tokens[i:i+3]) for i in range(len(tokens)-2)]

trigram_counts = Counter(trigrams)

phrase_cloud = WordCloud(
    width=800,
    height=400,
    background_color='white',
    colormap='viridis',
    max_words=200
).generate_from_frequencies(trigram_counts)

plt.figure(figsize=(15, 7.5))
plt.imshow(phrase_cloud, interpolation='bilinear')
plt.axis('off')
plt.title("3-Word Phrase Cloud of Normalized Duolingo Reviews", fontsize=18)
plt.show()
