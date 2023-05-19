import pandas as pd
import numpy as np

from glob import glob

import cv2
import matplotlib.pylab as plt

plt.style.use('ggplot')

# Getting image data
cat_files = glob('training_set/cats/*.jpg')
dog_files = glob('training_set/dogs/*.jpg')

# Getting hold on specific image
img_mpl = plt.imread(cat_files[20])
img_cv2 = cv2.imread(cat_files[20])

# Plotting the image pixels
# pd.Series(img_mpl.flatten()).plot(kind='hist',
#                                   bins=50,
#                                   title='Distribution of Pixel Values')
# plt.show()


# Displaying image
# fig, ax = plt.subplots(figsize=(10, 10))
# ax.imshow(img_mpl)
# ax.axis('off')
# plt.show()

# Display RGB Channels of our image
# fig, axs = plt.subplots(1, 3, figsize=(15, 5))
# axs[0].imshow(img_mpl[:, :, 0], cmap='Reds')
# axs[1].imshow(img_mpl[:, :, 1], cmap='Greens')
# axs[2].imshow(img_mpl[:, :, 2], cmap='Blues')
# axs[0].axis('off')
# axs[1].axis('off')
# axs[2].axis('off')
# axs[0].set_title('Red channel')
# axs[1].set_title('Green channel')
# axs[2].set_title('Blue channel')
# plt.show()


# Matplotlib vs cv2 Numpy Arrays
# cv2 reads in channels as BGR
# matplotlib reads in channels as RGB
# fig, axs = plt.subplots(1, 2, figsize=(10, 5))
# axs[0].imshow(img_cv2)
# axs[1].imshow(img_mpl)
# axs[0].axis('off')
# axs[1].axis('off')
# axs[0].set_title('CV2 Image')
# axs[1].set_title('Matplotlib Image')
# plt.show()


# Image Manipulation
img = plt.imread(dog_files[11])
fig, ax = plt.subplots(figsize=(8, 8))
ax.imshow(img)
ax.axis('off')
plt.show()

# Convertion to gray scale
img_gray = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)
fig, ax = plt.subplots(figsize=(8, 8))
ax.imshow(img_gray, cmap='Greys')
ax.axis('off')
ax.set_title('Grey Image')
plt.show()


# Different Size
img_resize = cv2.resize(img, (100, 200))
fig, ax = plt.subplots(figsize=(8, 8))
ax.imshow(img_resize)
ax.axis('off')
plt.show()

img_resize = cv2.resize(img, (5000, 5000), interpolation = cv2.INTER_CUBIC)
fig, ax = plt.subplots(figsize=(8, 8))
ax.imshow(img_resize)
ax.axis('off')
plt.show()
