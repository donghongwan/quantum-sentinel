import numpy as np
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score

class TransferLearning:
    def __init__(self, base_model):
        self.base_model = base_model

    def train_on_source(self, X_source, y_source):
        """Train the base model on the source domain."""
        self.base_model.fit(X_source, y_source)

    def fine_tune(self, X_target, y_target):
        """Fine-tune the model on the target domain."""
        self.base_model.fit(X_target, y_target)

if __name__ == "__main__":
    # Example usage
    iris = load_iris()
    X = iris.data
    y = iris.target
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    base_model = RandomForestClassifier()
    tl = TransferLearning(base_model)
    tl.train_on_source(X_train, y_train)

    # Fine-tune on the same data for demonstration
    tl.fine_tune(X_test, y_test)
    accuracy = accuracy_score(y_test, tl.base_model.predict(X_test))
    print("Transfer Learning Model Accuracy:", accuracy)
