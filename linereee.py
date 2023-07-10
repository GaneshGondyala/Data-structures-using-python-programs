a=[1,6,2,3,4,78,9]
l=0
k=int(input())
r=len(a)-1
for i in range(len(a)):
    if a[l]==k:
        print(l,"left")
        break
    elif a[r]==k:
        print(r,"right")
        break
    else:
        l=l+1
        r=r-1
else:
    print("not")
