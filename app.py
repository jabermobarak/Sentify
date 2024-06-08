from flask import Flask, render_template, request
from nltk.sentiment import SentimentIntensityAnalyzer
import nltk

app = Flask(__name__)

# Download necessary NLTK resources
nltk.download('punkt')
nltk.download('vader_lexicon')

# Initialize the Sentiment Intensity Analyzer
sid = SentimentIntensityAnalyzer()


@app.route('/', methods=['GET', 'POST'])


def index():
    text = ''  # Initialize text variable

    positive_count = 0
    negative_count = 0
    neutral_count = 0

    if request.method == 'POST':
        # Get the input text from the form
        text = request.form['text']

        # Split input into sentences
        sentences = [sentence.strip() for sentence in text.split('\n') if sentence.strip()]

        # Analyze sentiment for each sentence
        for sentence in sentences:
            sentiment_score = sid.polarity_scores(sentence)
            if sentiment_score['compound'] >= 0.05:
                positive_count += 1
            elif sentiment_score['compound'] <= -0.05:
                negative_count += 1
            else:
                neutral_count += 1

    return render_template('index.html', text=text, positive_count=positive_count, negative_count=negative_count, neutral_count=neutral_count)

if __name__ == '__main__':
    app.run(debug=True)
