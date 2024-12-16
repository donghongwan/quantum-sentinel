import nltk
from nltk.tokenize import word_tokenize
from nltk.sentiment import SentimentIntensityAnalyzer

class NaturalLanguageProcessing:
    def __init__(self):
        nltk.download('punkt')
        nltk.download('vader_lexicon')
        self.sia = SentimentIntensityAnalyzer()

    def analyze_report(self, report):
        """Analyze a security report for sentiment and keywords."""
        tokens = word_tokenize(report)
        sentiment = self.sia.polarity_scores(report)
        return tokens, sentiment

if __name__ == "__main__":
    nlp = NaturalLanguageProcessing()
    report = "The system was compromised, but the threat was neutralized quickly."
    tokens, sentiment = nlp.analyze_report(report)
    print("Tokens:", tokens)
    print("Sentiment:", sentiment)
