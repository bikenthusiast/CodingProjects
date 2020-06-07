import tensorflow
import keras
import pandas as pd
import numpy as np
import sklearn
from sklearn import linear_model


data = pd.read_csv("DataInput/student-mat.csv", sep=";")
# Since our data is seperated by semicolons we need to do sep=";"
# Trim data
data = data[["G1", "G2", "G3", "studytime", "failures", "absences"]]
print (data.head())

predict = "G3"

X = np.array(data.drop([predict], 1))
y = np.array(data[predict])

x_train, x_test, y_train, y_test = sklearn.model_selection.train_test_split(X, y, test_size = 0.1)

linear = linear_model.LinearRegression()
linear.fit(x_train, y_train)
acc = linear.score(x_test, y_test) # acc stands for accuracy
print(acc)
print('Coefficient: \n', linear.coef_) # These are each slope value
print('Intercept: \n', linear.intercept_) # This is the intercept
predictions = linear.predict(x_test) # Gets a list of all predictions

for x in range(len(predictions)):
    print(predictions[x], x_test[x], y_test[x])