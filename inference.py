import pickle
import numpy as np
import pandas as pd

file_to_read = open('churn_model.pkl', 'rb')
clf = pickle.loads(file_to_read.read())

if __name__ == '__main__':
    X_test = pd.read_csv('datasets/X_test.csv')
    y_pred_true = np.loadtxt('preds.csv')
    y_pred = clf.predict(X_test)

    print(f'Equals predictions: {np.array_equal(y_pred_true, y_pred)}')
