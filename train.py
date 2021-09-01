import pandas as pd
import numpy as np
import pickle
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score,classification_report


def save_model(my_model,model_filename):
    """
    Receives a machine learning model and a file name and saves it in the disk using pickle

    """

    with open(model_filename, 'wb') as handle:
        pickle.dump(my_model, handle)


def create_models(filename):
    df = create_dataframe(filename,0)




def create_dataframe(filename,target_letter):
    df = pd.read_csv(filename)

    not_letter_df = df[df.target != target_letter].sample(len(df[df.target == target_letter]))
    letter_df = df[df.target == target_letter]
    final_df = pd.concat([letter_df, not_letter_df], ignore_index=True)
    print(final_df.head(10))
    return final_df

def load_and_get_sets(filename,target):
    """
    function that gets a filename and the name of target feature
    then loads the data from the file and returns the train and test sets
    """

    df = pd.read_csv(filename)
    cols = ['pix' + str(i) for i in range(1, 785)]
    cols = ['target'] + cols
    df.columns=cols

    X = df.loc[:,df.columns!=target]
    y = df[target]


    X_train, X_test, y_train, y_test = train_test_split(X,y,test_size=.2,random_state=334)
    return X_train,X_test,y_train,y_test
#comment#
def main():
    """
    Main function that calls the other functions and controls the flow of the process required


    :return:
    """
    X_train, X_test, y_train, y_test = load_and_get_sets('datasets/A_Z Handwritten Data.csv','target')
    rf_clf = RandomForestClassifier()
    rf_clf.fit(X_train,y_train)
    clf = LogisticRegression()
    clf.fit(X_train,y_train)

    save_model(clf, 'Logistic.pkl')
    print('M.L model saved as Logistic.pkl')
    save_model(rf_clf, 'Random_Forest.pkl')

    print('M.L model saved as Random_Forest.pkl')






if __name__ == '__main__':
    main()


