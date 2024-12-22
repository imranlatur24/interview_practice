import pickle

f = open("myfile.txt","rb")
content = pickle.load(f)
print(content)
f.close()

