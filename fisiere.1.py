with open('input.txt','r') as f:
    n=f.readline()
    n=n.split()
for i in n:
    if ord(i) in range(65,91):
        nr=''
        with open ('litereA.txt','w') as f:
            nr+=f.write(i)
    if ord(i) in range(48,58):
        nn=''
        with open('cifre.txt','w') as f:
            nn+=f.write(i)
    if((ord(i) in range(42,48))or ((ord(i) in range(60,63)))):
        nc=''
        with open('operatori.txt','w') as f:
            nc+=f.write(i)
    if ord(i) in range(97,123):
        nl=''
        with open ('litereB.txt','w') as f:
            nl+=f.write(i)