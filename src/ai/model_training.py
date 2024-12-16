import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
import joblib

class ModelTraining:
    def __init__(self, model=None):
        self.model = model if model else RandomForestClassifier()

    def train(self, X, y):
        """Train the model on the provided data."""
        self.model.fit(X, y)

    def evaluate(self, X_test, y_test):
        """Evaluate the model on the test data."""
        predictions = self.model.predict(X_test)
        return accuracy_score(y_test, predictions)

    def save_model(self, filename):
        """Save the trained model to a file."""
        joblib.dump(self.model, filename)

    def load_model(self, filename):
        """Load a model from a file."""
        self.model = joblib.load(filename)

if __name__ == "__main__":
    # Example usage
    # Generate synthetic data
    X = np.random.rand(100, 5)
    y = np.random.randint(0, 2, size=100)

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    trainer = ModelTraining()
    trainer.train(X_train, y_train)
    accuracy = trainer.evaluate(X_test, y_test)
    print("Model Accuracy:", accuracy)

    # Save the model
    trainer.save_model("trained_model.pkl")
