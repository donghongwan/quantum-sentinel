import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score
import lime
from lime.lime_tabular import LimeTabularExplainer

class ExplainableAI:
    def __init__(self, model):
        self.model = model

    def train_model(self, X, y):
        """Train the model on the provided data."""
        self.model.fit(X, y)

    def explain_instance(self, instance, X_train, feature_names):
        """Explain a specific instance using LIME."""
        explainer = LimeTabularExplainer(X_train, feature_names=feature_names, class_names=['class 0', 'class 1'], discretize_continuous=True)
        exp = explainer.explain_instance(instance, self.model.predict_proba, num_features=10)
        return exp

    def plot_explanation(self, exp):
        """Plot the explanation for a specific instance."""
        plt.figure(figsize=(10, 6))
        plt.imshow(exp.as_pyplot_figure(), aspect='auto')
        plt.show()

if __name__ == "__main__":
    # Example usage
    from sklearn.datasets import load_iris
    iris = load_iris()
    X = iris.data
    y = iris.target
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    model = LogisticRegression()
    xai = ExplainableAI(model)
    xai.train_model(X_train, y_train)

    instance = X_test[0]
    exp = xai.explain_instance(instance, X_train, iris.feature_names)
    xai.plot_explanation(exp)
