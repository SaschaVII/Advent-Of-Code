import numpy as z
def a(b):
    c=1
    for d in b:c*=d
    return c
def b(b):
    c=0
    for d in b:c+=d
    return c
def c(d,e):return b(d) if e=="+" else a(d)
if __name__=="__main__":
    d="inputTest.txt"
    with open(d) as e:f=e.readlines()
    g=[];h=0;i=[];o=[];p=[];v=0
    for j in f:
        k=j.strip()
        if not k:continue
        m=[]
        for n in k.split():
            if "*" in n or "+" in n:i.append(n)
            else:m.append(int(n))
        if m:g.append(m)
    print("lines:  ",len(f));print("columns:  ",len(f[0]))
    for q in range(len(f[0])-1):
        r=[f[s][q] for s in range(len(f)-1)]
        if r.count(" ")<4:o.append(int("".join(r)))
        else:p.append(o);o=[]
    p.append(o)
    z.transpose(g)
    for w in i:h+=c(p[v],w);v+=1
    print(h)