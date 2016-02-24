import pickle

n = [["callan", 2], ["john", 3]]

pickle.dump(n, open("data.p", "wb"))

x = pickle.load(open("data.p", "rb"))