class Solution:
    def countSubarrays(self, arr, k):
        # code here
        prefixSums = {}
        res = 0
        currSum = 0
    
        for val in arr:
            # Add current element to sum so far
            currSum += val
    
            # If currSum is equal to desired sum, then a new subarray is found
            if currSum == k:
                res += 1
    
            # Check if the difference exists in the prefixSums dictionary
            if currSum - k in prefixSums:
                res += prefixSums[currSum - k]
    
            # Add currSum to the dictionary of prefix sums
            prefixSums[currSum] = prefixSums.get(currSum, 0) + 1
    
        return res
