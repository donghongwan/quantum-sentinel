import numpy as np
from sklearn.datasets import make_moons
from sklearn.neural_network import MLPClassifier

class GenerativeModels:
    def __init__(self):
        self.model = MLPClassifier(hidden_layer_sizes=(10,), max_iter=1000)

    def generate_data(self, n_samples=100):
        """Generate synthetic data using a simple generative model."""
        X, y = make_moons(n_samples=n_samples, noise=0.1)
        return X, y

    def train_model(self, X, y):
        """Train the generative model on the synthetic data."""
        self.model.fit(X, y)

if __name__ == "__main__":
    # Example usage
    gm = GenerativeModels()
    X, y = gm.generate_data(n_samples=200)
    gm.train_model(X, y)
    print("Synthetic data generated and model trained.")
