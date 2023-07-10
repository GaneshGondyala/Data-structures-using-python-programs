s=[1,7,9,2,4,6,7]
for i in range(len(s)-1):
    d=False
    for j in range(len(s)-1-i):
        if s[j]>s[j+1]:
            s[j],s[j+1]=s[j+1],s[j]
            d=True
        print(s)
    if d==False:
        break
print(s)
