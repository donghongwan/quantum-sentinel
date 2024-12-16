import numpy as np
from nltk.sentiment import SentimentIntensityAnalyzer
import nltk

class SentimentAnalysis:
    def __init__(self):
        nltk.download('vader_lexicon')
        self.sia = SentimentIntensityAnalyzer()

    def analyze_sentiment(self, text):
        """Analyze the sentiment of the given text."""
        sentiment_scores = self.sia.polarity_scores(text)
        return sentiment_scores

if __name__ == "__main__":
    # Example usage
    sa = SentimentAnalysis()
    text = "The recent security breach has raised concerns among users."
    sentiment = sa.analyze_sentiment(text)
    print("Sentiment Scores:", sentiment)
