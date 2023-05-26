import tensorflow as tf
import keras
from keras import models, layers

class JASMINE:
    model = models.Sequential([
        layers.Flatten(input_shape = (8, 8)),
        layers.Dense(32, activation="relu"),
        layers.Dense(1, activation="sigmod")
    ])

    model.compile(optimizer="sgd", loss="softmax")



    model.save("./src/IA/memory/jasmin.h5")