class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        if len(s) % 2 == 1:
            return False
        for i in s:
            if i == "(" or i == "[" or i == "{":
                stack.append(i)
            else:
                if len(stack) <= 0:
                    return False
                else:
                    temp = stack.pop()
                if i == ")" and temp == "(":
                    pass
                elif i == "]" and temp == "[":
                    pass
                elif i == "}" and temp == "{":
                    pass
                else:
                    return False
        if len(stack) != 0:
            return False
        return True