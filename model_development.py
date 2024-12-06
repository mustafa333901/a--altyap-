import tensorflow as tf

# --------------------
# 2. Model Geliştirme
# --------------------
class ModelDevelopment:
    def __init__(self, input_shape):
        self.input_shape = input_shape

    def build_model(self):
        """Derin öğrenme modeli oluşturur."""
        model = tf.keras.Sequential([
            tf.keras.layers.Dense(128, activation='relu', input_shape=(self.input_shape,)),
            tf.keras.layers.Dense(64, activation='relu'),
            tf.keras.layers.Dense(1, activation='sigmoid')
        ])
        model.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])
        return model

    def train_model(self, model, X_train, y_train, epochs=10, batch_size=32):
        """Modeli eğitir."""
        model.fit(X_train, y_train, epochs=epochs, batch_size=batch_size)
        return model
