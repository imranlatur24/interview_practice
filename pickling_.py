import pickle

f = open("myfile.txt","wb")
d = {1:'imran',2:'irfan'}
content = pickle.dump(d,f)
print('pickle process completed')
f.close()

