class Solution:
    def isValid(self, s: str) -> bool:
        br_hash_t = {')':'(','}':'{',']':'['}
        br_stack = []
        print(len(s))
        for i in s:
            if i == '(' or i == '{' or i == '[':
                br_stack.append(i)
                #print(br_stack)

            if i == ')' or i == '}' or i == ']':
                if len(br_stack) < 1:
                    return False
                else:
                    p = br_stack.pop()
                    if br_hash_t[i] == p:
                        continue
                    else:
                        return False
            #print(br_stack)

        if len(br_stack)==0:
            return True
        else:
            return False 

# test strings below
input_str = '[](({}))[][]'
input_str2 = '}{()()'
input_str3 = '(())jsjs{jj}[s]j'

sol = Solution()
print(sol.isValid(input_str3))
