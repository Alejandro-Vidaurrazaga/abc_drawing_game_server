import pickle

file_to_read = open('Logistic.pkl', 'rb')
clf = pickle.loads(file_to_read.read())