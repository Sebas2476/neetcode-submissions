class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
            Char_count_t = {}
            Char_count_s = {}

            for i in s:
                Char_count_t[i] = Char_count_t.get(i, 0) + 1

            for j in t: 
                Char_count_s[j] = Char_count_s.get(j, 0) + 1

            if Char_count_s == Char_count_t:
                return True
            return False


