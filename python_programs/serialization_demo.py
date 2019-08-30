import pickle
L = [10, 20, "hi", {1: 2}, [30, 40], 50]
f = open("mydata_serialized", "w")
pickle.dump(L, f)
f.close()

f = open("mydata_serialized", "r")
L1 = pickle.load(f)
f.close()
print L1
