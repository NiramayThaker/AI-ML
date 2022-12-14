import sklearn
from sklearn.utils import shuffle
from sklearn.neighbors import KNeighborsClassifier
import pandas as pd
import numpy as np
from sklearn import linear_model, preprocessing

data = pd.read_csv("car.data", sep=",")

# Transferring Non-numerical data into Numerical data
le = preprocessing.LabelEncoder()
buying = le.fit_transform(data["buying"])
maint = le.fit_transform(data["maint"])
door = le.fit_transform(data["door"])
persons = le.fit_transform(data["persons"])
lug_boot = le.fit_transform(data["lug_boot"])
safety = le.fit_transform(data["safety"])
cls = le.fit_transform(data["class"])

predict = "cls"
x = list(zip(buying, maint, door, persons, lug_boot, safety, cls))
y = list(cls)

x_train, x_test, y_train, y_test = sklearn.model_selection.train_test_split(x, y, test_size=0.1)

model = KNeighborsClassifier(n_neighbors=10)  # 5 is a Hyper parameter(Number of neighbours to look for)
model.fit(x_train, y_train)
acc = model.score(x_test, y_test)
print(acc)  # Print Accuracy of the output base on test data

predicted = model.predict(x_test)
names = ["unacc", "acc", "good", "vgood"]

for x in range(len(x_test)):
	print("Predicted: ", names[predicted[x]], "Data: ", x_test[x], "Actual: ", names[y_test[x]])
	n = model.kneighbors([x_test[x]], 5, True)
	print("N: ", n)
