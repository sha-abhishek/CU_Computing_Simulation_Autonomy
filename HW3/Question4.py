class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l = len(s)
        arr = [0]*26
        flag = 0
        maxl = 0
        
        for i in range(l):
            idx = ord(s[i])-97  # ASCII for english letters >> 97-122
            if arr[idx] == 0:
                arr[idx] = 1
                flag = flag + 1
                if maxl < flag:
                    maxl = flag
                
            else:
                if maxl < flag:
                    maxl = flag
                arr = [0]*26
                arr[idx] = 1
                flag = 1

        return maxl


sol = Solution()

inp = "abcababcdeaabcdefghabcdefghijklmnopqrstuvwxyabcd"

print("max substring lenght = ", sol.lengthOfLongestSubstring(inp))
