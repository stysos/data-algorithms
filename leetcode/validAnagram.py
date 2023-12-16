class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        return sorted(s) == sorted(t)
        
test_case = Solution()

test_case.isAnagram(s = "anagram", t = "nagaram")