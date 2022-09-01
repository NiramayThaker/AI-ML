import pandas as pd
import numpy as np
import sklearn
from sklearn import linear_model
import matplotlib.pyplot as pyplot
from matplotlib import style
import pickle

data = pd.read_csv("student-mat.csv", sep=";")
data = data[["G1", "G2", "G3", "studytime", "failures", "absences"]]

predict = "G3"

x = np.array(data.drop([predict], 1))
y = np.array(data[predict])
x_train, x_test, y_train, y_test = sklearn.model_selection.train_test_split(x, y, test_size=0.1)

# Finding Best model out of 40 training
# best = 0
# for _ in range(40):
# 	x_train, x_test, y_train, y_test = sklearn.model_selection.train_test_split(x, y, test_size=0.1)
#
# 	Linear = linear_model.LinearRegression()
# 	Linear.fit(x_train, y_train)
# 	acc = Linear.score(x_test, y_test)
# 	print(acc)
#
# 	if acc > best:
# 		best = acc
# 		with open("student_model.pickle", "wb") as f:
# 			pickle.dump(Linear, f)

pickle_in = open("student_model.pickle", "rb")
Linear = pickle.load(pickle_in)


print("CO: ", Linear.coef_)
print("Intercept: ", Linear.intercept_)

print()
prediction = Linear.predict(x_test)
for i in range(len(prediction)):
	print(prediction[i])
	print(x_test[i])
	print(y_test[i])
	print()

p = "absences"
style.use("ggplot")
pyplot.scatter(data[p], data["G3"])
pyplot.xlabel(p)
pyplot.ylabel("Final grade")
pyplot.show()
