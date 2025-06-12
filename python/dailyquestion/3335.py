class Solution:
    def lengthAfterTransformations(self, s: str, t: int) -> int:
        for i in range(t):
            new_string = ''
            for j in range(len(s)):
                if ord(s[j]) == 122:
                    new_string += 'ab'
                else:
                    new_string += chr(ord(s[j])+1)
            s = new_string
        return len(new_string)