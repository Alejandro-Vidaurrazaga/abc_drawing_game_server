from sklearn.metrics import recall_score, precision_score, accuracy_score
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
import pandas as pd
import numpy as np
import pickle


def train_model():
    df = pd.read_csv('cellular_churn_greece.csv')
    X_train, X_test, y_train, y_test = train_test_split(df.drop('churned', axis='columns'), df['churned'],
                                                        test_size=0.2,
                                                        random_state=1)

    clf = RandomForestClassifier(200, max_depth=5, n_jobs=-1)
    clf.fit(X_train, y_train)
    y_pred = clf.predict(X_test)

    print(f'Accuracy: {accuracy_score(y_test, y_pred)}')
    print(f'Precision: {precision_score(y_test, y_pred)}')
    print(f'Recall: {recall_score(y_test, y_pred)}')

    file_to_write = open('churn_model.pkl', 'wb')
    file_to_write.write(pickle.dumps(clf))


if __name__ == '__main__':
    df = pd.read_csv('cellular_churn_greece.csv')
    X_train, X_test, y_train, y_test = train_test_split(df.drop('churned', axis='columns'), df['churned'],
                                                        test_size=0.2,
                                                        random_state=1)

    clf = RandomForestClassifier(200, max_depth=5, n_jobs=-1)
    clf.fit(X_train, y_train)
    y_pred = clf.predict(X_test)

    print(f'Accuracy: {accuracy_score(y_test, y_pred)}')
    print(f'Precision: {precision_score(y_test, y_pred)}')
    print(f'Recall: {recall_score(y_test, y_pred)}')

    file_to_write = open('churn_model.pkl', 'wb')
    file_to_write.write(pickle.dumps(clf))

    X_test.to_csv('X_test.csv', index=False)
    np.savetxt('preds.csv', y_pred)
