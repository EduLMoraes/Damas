import tensorflow as tf
import keras
from keras import layers, models, regularizers

class JASMINE:
    def __new__(cls):
        if not hasattr(cls, "instance"):
            cls.instance = super(JASMINE, cls).__new__(cls)
        return cls.instance

    def __init__(self, board):
        self.model = models.Sequential([
            layers.Flatten(input_shape = (8, 8)),
            layers.Dense(32, activation="relu", kernel_regularizer = regularizers.l1(0.01)),
            layers.Dense(1, activation="sigmoid"),
            layers.Dropout(0.25)
        ])
        self.board = board

    def train(self, x_train, y_train):
        self.model.fit(x_train, y_train, epochs=10000)

    def compile(self):
        self.model.compile(optimizer="adam", loss="binary_crossentropy")

    def play(self):
        return self.model.predict(self.board)

    def save(self):
        self.model.save("./src/IA/memory/jasmin.h5")