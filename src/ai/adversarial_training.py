import numpy as np
import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Dropout
from tensorflow.keras.utils import to_categorical
from tensorflow.keras.datasets import mnist
from tensorflow.keras.optimizers import Adam

class AdversarialTraining:
    def __init__(self, model):
        self.model = model

    def generate_adversarial_samples(self, X, y, epsilon=0.1):
        """Generate adversarial samples using the FGSM method."""
        adversarial_samples = X + epsilon * np.sign(np.random.randn(*X.shape))
        return adversarial_samples

    def train_model(self, X, y, adversarial_samples):
        """Train the model on the original and adversarial samples."""
        self.model.fit(X, y, epochs=10, batch_size=128, validation_data=(adversarial_samples, y))

if __name__ == "__main__":
    # Example usage
    (X_train, y_train), (X_test, y_test) = mnist.load_data()
    X_train = X_train.reshape(-1, 784) / 255.0
    X_test = X_test.reshape(-1, 784) / 255.0
    y_train = to_categorical(y_train)
    y_test = to_categorical(y_test)

    model = Sequential()
    model.add(Dense(128, activation='relu', input_shape=(784,)))
    model.add(Dropout(0.2))
    model.add(Dense(10, activation='softmax'))

    model.compile(loss='categorical_crossentropy', optimizer=Adam(lr=0.001), metrics=['accuracy'])

    adversarial_training = AdversarialTraining(model)
    adversarial_samples = adversarial_training.generate_adversarial_samples(X_train, y_train)
    adversarial_training.train_model(X_train, y_train, adversarial_samples)
