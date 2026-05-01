class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = ''.join(c.lower() for c in s if c.isalnum())

        f, l = 0, len(s)-1

        if f == l: return True

        while l>f:
            if s[f] != s[l]:
                return False

            f += 1
            l -= 1

        return True
        