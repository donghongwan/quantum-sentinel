import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from sklearn.ensemble import GradientBoostingClassifier
from sklearn.tree import export_graphviz
import graphviz

class ExplainableBoosting:
    def __init__(self, model):
        self.model = model

    def train_model(self, X, y):
        """Train the model on the provided data."""
        self.model.fit(X, y)

    def explain_model(self, feature_names):
        """Generate a visual explanation of the model."""
        # Export the first tree in the ensemble
        dot_data = export_graphviz(self.model.estimators_[0, 0], out_file=None, 
                                    feature_names=feature_names, filled=True, rounded=True, 
                                    special_characters=True)  
        return graphviz.Source(dot_data)

if __name__ == "__main__":
    # Example usage
    from sklearn.datasets import load_iris
    iris = load_iris()
    X = iris.data
    y = iris.target
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    model = GradientBoostingClassifier()
    eb = ExplainableBoosting(model)
    eb.train_model(X_train, y_train)

    accuracy = accuracy_score(y_test, eb.model.predict(X_test))
    print("Explainable Boosting Model Accuracy:", accuracy)

    # Generate explanation
    feature_names = iris.feature_names
    explanation = eb.explain_model(feature_names)
    explanation.render("explainable_boosting_tree", view=True)
