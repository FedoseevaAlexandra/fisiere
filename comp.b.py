
#cu numere
a=[]
with open ('input.txt','r') as f:
    l=f.readline()
l=l.split(' ')
a.extend(l)
c1=0
for i in range(len(a)):              
    a[i]=int(a[i])
k=[] 
for d in range(len(a)):
    c2=a.count(a[d])
    if c2>c1:
        c1=c2
        k.clear()
        k.append(a[d])
    if c2==c1:
        if a[d] not in k:
          k.append(a[d])
k=str(k)
print(k)
