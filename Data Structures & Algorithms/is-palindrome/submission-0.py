class Solution:
    def isPalindrome(self, s: str) -> bool:
        clean_s = ""
        for char in s:
            if char.isalnum():
                clean_s += char.lower()

        rev = clean_s[::-1]

        return rev == clean_s

