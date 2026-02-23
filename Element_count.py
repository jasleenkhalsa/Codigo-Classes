str = "Python Session"
dict = {}

string = str.replace(" ", "").lower()

for i in string:
    if i in dict:
        dict[i] +=1
    else:
        dict[i] = 1 

print(dict)