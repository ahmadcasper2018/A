import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from PIL import Image

data = pd.read_csv('datasets/skin/hmnist_28_28_RGB.csv')
other = pd.read_csv('datasets/skin/HAM10000_metadata.csv')
target = data['label']
input = data.drop(columns=['label'])
