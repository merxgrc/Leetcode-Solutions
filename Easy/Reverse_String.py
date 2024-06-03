# Constraints:
#
#     1 <= s.length <= 105
#     s[i] is a printable ascii character.

class Solution(object):
    def reverseString(self, s):
        """
        :type s: List[str]
        :rtype: None Do not return anything, modify s in-place instead.
        """
        p1 = 0
        p2 = len(s)-1

        while p1 < p2:
            temp = s[p1]
            s[p1] = s[p2]
            s[p2] = temp
            p1+=1
            p2-=1

