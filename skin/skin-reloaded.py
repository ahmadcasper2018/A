import numpy as np
import pandas as pd
import seaborn as sns
from PIL import Image
from tensorflow.keras.layers import (
    Input,
    Lambda,
    Dense,
    Flatten,
    Conv2D,
    MaxPooling2D,
    Dropout,
    BatchNormalization,
    GlobalMaxPooling2D,
)
from tensorflow.keras.models import Model
from tensorflow.keras.applications import ResNet152V2
from tensorflow.keras.preprocessing import image
from tensorflow.keras.preprocessing.image import ImageDataGenerator, load_img
from tensorflow.keras.models import Sequential
import tensorflow as tf
from sklearn.model_selection import train_test_split

IMAGE_SIZE = [28, 28]

# read the data
data = pd.read_csv("../datasets/skin/hmnist_28_28_RGB.csv")
other = pd.read_csv("../datasets/skin/HAM10000_metadata.csv")
target = data["label"]
input = data.drop(columns=["label"])

input = np.array(input).reshape(-1, 28, 28, 3)
input = input / 255.0
# build the model
X_train, X_test, y_train, y_test = train_test_split(
    input, target, test_size=0.2, random_state=42
)
i = Input(shape=(28, 28, 3))
x = Conv2D(32, (3, 3), activation="relu", padding="same")(i)
x = BatchNormalization()(x)
x = Conv2D(32, (3, 3), activation="relu", padding="same")(x)
x = BatchNormalization()(x)
x = MaxPooling2D((2, 2))(x)
x = Dropout(0.2)(x)
x = Conv2D(64, (3, 3), activation="relu", padding="same")(x)
x = BatchNormalization()(x)
x = Conv2D(64, (3, 3), activation="relu", padding="same")(x)
x = BatchNormalization()(x)
x = MaxPooling2D((2, 2))(x)
x = Dropout(0.2)(x)
x = Conv2D(128, (3, 3), activation="relu", padding="same")(x)
x = BatchNormalization()(x)
x = Conv2D(128, (3, 3), activation="relu", padding="same")(x)
x = BatchNormalization()(x)
x = MaxPooling2D((2, 2))(x)
x = Dropout(0.2)(x)

x = GlobalMaxPooling2D()(x)
x = Flatten()(x)
x = Dropout(0.2)(x)
x = Dense(256, activation="relu")(x)
x = Dropout(0.2)(x)
x = Dense(7, activation="softmax")(x)

model = Model(i, x)
