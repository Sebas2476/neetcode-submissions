class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        mapping = {")": "(", "}": "{", "]": "["}

        for char in s:
            if char == "(" or char == "[" or char == "{":
                stack.append(char)
            if char == ")" or char == "]" or char == "}":
                if not stack:
                    return False
                if stack[-1] in mapping[char]:
                     stack.pop()
                else:
                     return False
    
        if not stack:
            return True
        return False