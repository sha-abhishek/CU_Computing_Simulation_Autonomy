class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        hash_t = {}
        if len(t) != len(s):
            return False

        else:
            for i in range(len(s)):
                if s[i] in hash_t:
                    hash_t[s[i]] += 1

                else:
                    hash_t[s[i]] = 1

            for j in range(len(t)):
                if t[j] in hash_t:
                    hash_t[t[j]] -= 1

                else:
                    return False

            key = hash_t.keys()

            for k in key:
                if hash_t[k] != 0:
                    return False

            return True 




# testing out the solution

s = 'anagram'
t = 'margana'

u = 'cat'
v = 'kat'

test1 = Solution()
test2 = Solution()

print(test1.isAnagram(s,t))
print(test2.isAnagram(u,v))