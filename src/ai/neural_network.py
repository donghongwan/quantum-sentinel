import numpy as np
from sklearn.neural_network import MLPClassifier

class NeuralNetwork:
    def __init__(self, hidden_layer_sizes=(100,), activation='relu', max_iter=200):
        self.model = MLPClassifier(hidden_layer_sizes=hidden_layer_sizes, activation=activation, max_iter=max_iter)

    def train(self, X, y):
        """Train the neural network on the provided data."""
        self.model.fit(X, y)

    def predict(self, X):
        """Make predictions using the trained neural network."""
        return self.model.predict(X)

    def evaluate(self, X, y):
        """Evaluate the neural network on the test data."""
        predictions = self.predict(X)
        return np.mean(predictions == y)

if __name__ == "__main__":
    # Example usage
    # Generate synthetic data
    X = np.random.rand(100, 5)
    y = np.random.randint(0, 2, size=100)

    nn = NeuralNetwork(hidden_layer_sizes=(10, 10), activation='relu')
    nn.train(X, y)
    accuracy = nn.evaluate(X, y)
    print("Neural Network Accuracy:", accuracy)
