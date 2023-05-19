import pandas as pd
import numpy as np

from glob import glob

import cv2
import matplotlib.pylab as plt

plt.style.use('ggplot')

cat_files = glob('training_set/cats/*.jpg')
dog_files = glob('training_set/training_set/dogs/*.jpg')

img_mp1 = plt.imread(cat_files[20])
img_cv2 = cv2.imread(cat_files[20])

print(type(img_mp1))
print(type(img_cv2))
