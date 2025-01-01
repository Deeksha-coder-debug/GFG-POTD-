class Solution:

    def anagrams(self, arr):
        '''
        words: list of word
        n:      no of words
        return : list of group of anagram {list will be sorted in driver code (not word in grp)}
        '''

        #code here
        res = []
        mp = {}
        
        for i in range(len(arr)):
            s = arr[i]
            
            # Find the key by sorting the string
            s = ''.join(sorted(s))
            
            # If key is not present in the hash map, add
            # an empty group (list) in the result and
            # store the index of the group in hash map
            if s not in mp:
                mp[s] = len(res)
                res.append([])
            
            # Insert the string in its correct group
            res[mp[s]].append(arr[i])
        
        return res
