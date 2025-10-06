t1=[31,28,31,30,31,30,31,31,30,31,30,31]
t2=["janvier","fevrier","mars","avril","mai","juin","juillet","aout","septembre","octobre","novembre","decembre"]
for i in range(12):
    t2.insert(2*i+1,t1[i])
print(t2)