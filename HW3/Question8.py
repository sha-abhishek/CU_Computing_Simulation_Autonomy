class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        l = len(s)
        counter = 0
        hash_t = {}
        for i in s:
            hash_t[i] = i

        for j in t:
            if hash_t[j]:
                counter = counter+1

        if counter == l:
            return True
        else:
            return False


s = 'anagram'
t = 'margana'

u = 'cat'
v = 'kat'

test1 = Solution()
test2 = Solution()

test1.isAnagram(s,t)
test2.isAnagram(u,v)