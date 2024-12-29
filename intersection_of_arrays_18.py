class Solution:
    def intersectionWithDuplicates(self, a, b):
        # code here
        res=[]
        a=set(a)
        b=set(b)
        for i in a:
            if i in b:
                res.append(i)
        return res
