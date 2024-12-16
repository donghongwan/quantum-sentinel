class AIConfig:
    """AI model configurations."""
    MODEL_NAME = "MyAIModel"
    MODEL_VERSION = "1.0"
    TRAINING_DATA_PATH = "data/training_data.csv"
    EPOCHS = 50
    BATCH_SIZE = 32
    LEARNING_RATE = 0.001

    @staticmethod
    def init_app(app):
        """Initialize the app with AI configurations."""
        app.config['MODEL_NAME'] = AIConfig.MODEL_NAME
        app.config['MODEL_VERSION'] = AIConfig.MODEL_VERSION
        app.config['TRAINING_DATA_PATH'] = AIConfig.TRAINING_DATA_PATH
        app.config['EPOCHS'] = AIConfig.EPOCHS
        app.config['BATCH_SIZE'] = AIConfig.BATCH_SIZE
        app.config['LEARNING_RATE'] = AIConfig.LEARNING_RATE

if __name__ == "__main__":
    # Example usage
    print("Model Name:", AIConfig.MODEL_NAME)
    print("Learning Rate:", AIConfig.LEARNING_RATE)
