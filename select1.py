a=[7,4,7,1,2]
for i in range(len(a)):
    s=a[i]
    s1=i
    for j in range(i+1,len(a)):
        if s>a[j]:
            s=a[j]
            s1=j
    a[i],a[s1]=a[s1],a[i]
print(a)
