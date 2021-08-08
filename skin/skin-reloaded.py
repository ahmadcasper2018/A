import numpy as np
import pandas as pd
import seaborn as sns
from PIL import Image

data = pd.read_csv('../datasets/skin/hmnist_28_28_RGB.csv')
other = pd.read_csv('../datasets/skin/HAM10000_metadata.csv')
target = data['label']
input = data.drop(columns=['label'])

input = np.array(input).reshape(-1, 28, 28, 3)
input = input / 255.0
