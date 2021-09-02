import pickle
#
file_to_read = open('Logistic.pkl', 'rb')
# file_to_read = open('Random_Forest.pkl', 'rb')
clf = pickle.loads(file_to_read.read())
import pandas as pd
from matplotlib import pyplot as plt

df = pd.read_csv('emnist-letters-train.csv')
y = df.iloc[:, 1]
X = df.iloc[:, 1:]

plt.imshow(X.iloc[69, :].T.to_numpy().reshape(28, 28), cmap='gray')
print(y[69])
print(X.iloc[69, :].T.to_numpy().reshape(28, 28))
# plt.show()