import json
from wordcloud import WordCloud
import matplotlib.pyplot as plt

with open("normalized_reviews.json", "r", encoding="utf-8") as f:
    data = json.load(f)

all_text = " ".join(entry['review'] for entry in data)

wordcloud = WordCloud(
    width=800,
    height=400,
    background_color='white',
    colormap='viridis',
    max_words=200
).generate(all_text)

plt.figure(figsize=(15, 7.5))
plt.imshow(wordcloud, interpolation='bilinear')
plt.axis('off')
plt.title("Word Cloud of Normalized Duolingo Reviews", fontsize=18)
plt.show()
