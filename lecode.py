class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) % 2 == 1 :
            return False
        dic={'(':')','{':'}','[':']'}
        stack = []
        for i in s:
            if bool(stack)==False or i in dic:
                stack.append(i)
            elif stack[-1] not in dic:
                return False
            else:
                if i == dic[stack[-1]]:
                    stack.pop()
                else:
                    return False
        #循环结束后
        if bool(stack)==False:
            return True
        else:
            return False








