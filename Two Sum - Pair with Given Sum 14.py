#Two Sum - Pair with Given Sum
class Solution:
	def twoSum(self, arr, target):
		# code here
		st=0
		end=len(arr)-1
		arr.sort()
		while st<end:
		    if arr[st]+arr[end]==target:
		        return True 
		    elif arr[st]+arr[end]<target: 
		        st+=1
		    else: 
		        end-=1
		return False
