import pickle

lb = ["华夏","中华","编程娃娃","Python","Scratch"]
f = open("列表.dat",mode='wb')
pickle.dump(lb,f)
f.close()


 
