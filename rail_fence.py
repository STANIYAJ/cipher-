s=input()
ar1=list()
ar2=list()
count=0
for c in s:
    if count%2==0:
        ar1.append(c)
        count+=1
    else:
        ar2.append(c)
        count+=1

for i in ar1:
    print(i,end=' ')

for i in ar2:
    print(i,end=' ')
