import pickle

f = open("列表.dat",mode='rb')
lb = pickle.load(f)
f.close()
print(lb)

 
