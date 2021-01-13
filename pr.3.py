with open ('globulet.txt','r') as f:
    a=f.readline()
    r=int(a)+3
    albastre=int(a)+r-2
    t=int(a)+r+albastre
with open ('bradut.txt','w') as f:
    f.write(str(t))