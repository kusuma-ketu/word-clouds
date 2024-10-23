from collections import Counter
import pandas as pd

with open ('p&p.txt', 'r', encoding='utf-8') as file:
    text=file.read()

words = text.lower().split()

word_counts = Counter(words)

top_100 = word_counts.most_common(100)

df = pd.DataFrame(top_100, columns=['Word', 'Count'])

df.to_csv('top_100.csv', index=True)

print('saved')