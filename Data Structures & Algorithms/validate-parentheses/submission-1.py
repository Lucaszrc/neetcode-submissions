class Solution:
    def isValid(self, s: str) -> bool:
        list1 = []
        closeToOpen = {")" : "(", "]" : "[", "}" : "{"}
        for char in s:
            if char in closeToOpen:
                if list1 and list1[-1] == closeToOpen[char]:
                    list1.pop()
                else:
                    return False
            else:
                list1.append(char)
        return True if not list1 else False