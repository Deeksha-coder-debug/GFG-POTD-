class Solution:
    #Function to count the number of possible triangles.
    def countTriangles(self, a):
        # code here
        c=0
        a.sort()
        for i in range(len(a)-1,1,-1):
            x=0
            y=i-1
            while x<y:
                if a[x]+a[y]>a[i]:
                    c+=y-x
                    y-=1
                else:
                    x+=1
        return c
