class Solution:
    def isValid(self, s: str) -> bool:
        Stack=[]
        Hashmap={")":"(","}":"{","]":"["}
        for c in s:
            if c in Hashmap:
                if Stack and Stack[-1] == Hashmap[c]:
                    Stack.pop()
                else:
                    return False
            else:
                Stack.append(c)
        return True if not Stack else False                
        