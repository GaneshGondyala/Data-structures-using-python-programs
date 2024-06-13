def a(s,l,h,k):
    m=(l+h)//2
    if l<=m:
        
        if s[m]==k:
            return ("found at index",m)
        elif s[m]>k:
            return a(s,l,m-1,k)
        elif s[m]<k:
            return a(s,m+1,h,k)

    else:
        return "not found"
s=[1,2,3,4,5,6,7,8]
l=0
h=len(s)-1
k=int(input("enter a number"))
v=a(s,l,h,k)
print(v)
#Bhanu edited this file

        
