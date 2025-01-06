class Solution:
    def sumClosest(self, a, t):
        # code here
        arr.sort()
    
        left = 0
        right = len(arr) - 1
        closest_sum = float('inf')
        closest_pair = []
        max_diff = -1
        
        while left < right:
            current_sum = arr[left] + arr[right]
            
            # Check if this pair is closer to the target
            if abs(current_sum - target) < abs(closest_sum - target):
                closest_sum = current_sum
                closest_pair = [arr[left], arr[right]]
                max_diff = abs(arr[left] - arr[right])
            elif abs(current_sum - target) == abs(closest_sum - target):
                # If the sum is equally close, check for maximum absolute difference
                if abs(arr[left] - arr[right]) > max_diff:
                    closest_pair = [arr[left], arr[right]]
                    max_diff = abs(arr[left] - arr[right])
            
            # Move pointers to narrow the range
            if current_sum < target:
                left += 1
            elif current_sum > target:
                right -= 1
            else:
                break  # Exact match found
        
        return closest_pair if closest_pair else []
