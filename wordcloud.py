import pandas as pd 
from wordcloud import WordCloud 
import matplotlib.pyplot as plt

def create_wordcloud_from_csv(csv_file, text_column):
    df = pd.read_csv(csv_file)

    text = ' '.join(df['Word'].astype(str))
    wordcloud = WordCloud(width=800, height=400, background_color='white').generate(text)

    wordcloud_path = 'wordcloud.png'
    plt.figure(figsize=(10,5))
    plt.imshow(wordcloud, interpolation='bilinear')
    plt.axis('off')
    plt.title('Word Cloud from Pride and Prejudice')
    plt.savefig(wordcloud_path)
    plt.close()

    return wordcloud_path

csv_file = '/top_100.csv'
text_column = 'Word'
create_wordcloud_from_csv(csv_file, text_column)

