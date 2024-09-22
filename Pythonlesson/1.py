s =  input()

n=len(s)
res=0
for i in range(n):
    mas= [False] * 256

    for j in range(i,n):
        if mas[ord(s[j])]==True:
            break
        else:
            res=max(res,j-i+1)
            mas[ord(s[j])]=True
print( res )