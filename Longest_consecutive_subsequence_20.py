class Solution:
    
    # arr[] : the input array
    
    #Function to return length of longest subsequence of consecutive integers.
    def longestConsecutive(self,arr):
        #code here
        if not arr:
            return 0
        a=set(arr)
        long_streak=0
        for i in arr:
            if i-1 not in a:
                st=i
                cur_streak=1
                while st+1 in a:
                    st+=1
                    cur_streak+=1
                    a.remove(st)
                long_streak=max(long_streak,cur_streak)
        return long_streak
