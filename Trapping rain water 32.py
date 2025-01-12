class Solution:
    def maxWater(self, a):
        # code here
        n=len(a)
        l=[0]*n
        r=[0]*n
        l[0]=a[0]
        r[n-1]=a[n-1]
        res=0
        for i in range(1,n):
            l[i]=max(l[i-1],a[i])
        for i in range(n-2,-1,-1):
            r[i]=max(r[i+1],a[i])
        for i in range(1,n-1):
            mini=min(l[i-1],r[i+1])
            if mini>a[i]:
                res+=mini-a[i]
        return res
