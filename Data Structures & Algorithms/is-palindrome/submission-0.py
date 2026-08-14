class Solution:
    def isPalindrome(self, s: str) -> bool:
        s_list = []
        for char in s:
            if char.isalnum():
                s_list.append(char.lower())
        return s_list == s_list[::-1]
