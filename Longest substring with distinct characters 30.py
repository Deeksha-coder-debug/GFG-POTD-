class Solution: 
    def longestUniqueSubstr(self, s):
            # code here
            freq = {}
            start = 0
            max_length = 0
            
            for end in range(len(s)):
                # Add the current character to the frequency dictionary
                char = s[end]
                freq[char] = freq.get(char, 0) + 1
                
                # If the frequency of any character is more than 1, shrink the window
                while freq[char] > 1:
                    freq[s[start]] -= 1
                    if freq[s[start]] == 0:
                        del freq[s[start]]
                    start += 1
                
                # Update the maximum length of the substring
                max_length = max(max_length, end - start + 1)
            
            return max_length
