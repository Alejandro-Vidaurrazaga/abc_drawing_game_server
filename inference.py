import pickle

# file_to_read = open('Logistic.pkl', 'rb')
file_to_read = open('Random_Forest.pkl', 'rb')
clf = pickle.loads(file_to_read.read())