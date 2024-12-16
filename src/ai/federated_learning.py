import numpy as np
import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Dropout
from tensorflow.keras.utils import to_categorical
from tensorflow.keras.datasets import mnist

class FederatedLearning:
    def __init__(self, model):
        self.model = model

    def train_model(self, X, y):
        """Train the model on the provided data."""
        self.model.fit(X, y, epochs=10, batch_size=128)

    def aggregate_models(self, models):
        """Aggregate the models from different clients."""
        aggregated_weights = np.mean([model.get_weights() for model in models], axis=0)
        self.model.set_weights(aggregated_weights)

if __name__ == "__main__":
    # Example usage
    (X_train, y_train), (X_test, y_test) = mnist.load_data()
    X_train = X_train.reshape(-1, 784) / 255.0
    X_test = X_test.reshape(-1,  784) / 255.0
    y_train = to_categorical(y_train)
    y_test = to_categorical(y_test)

    model = Sequential()
    model.add(Dense(128, activation='relu', input_shape=(784,)))
    model.add(Dropout(0.2))
    model.add(Dense(10, activation='softmax'))

    model.compile(loss='categorical_crossentropy', optimizer='adam', metrics=['accuracy'])

    federated_learning = FederatedLearning(model)
    # Simulate training on different clients
    client_models = []
    for _ in range(5):  # Simulating 5 clients
        client_model = Sequential()
        client_model.add(Dense(128, activation='relu', input_shape=(784,)))
        client_model.add(Dropout(0.2))
        client_model.add(Dense(10, activation='softmax'))
        client_model.compile(loss='categorical_crossentropy', optimizer='adam', metrics=['accuracy'])
        client_model.fit(X_train, y_train, epochs=1, batch_size=128)
        client_models.append(client_model)

    # Aggregate the models from clients
    federated_learning.aggregate_models(client_models)
    # Evaluate the aggregated model
    loss, accuracy = federated_learning.model.evaluate(X_test, y_test)
    print(f"Aggregated model accuracy: {accuracy:.4f}")
