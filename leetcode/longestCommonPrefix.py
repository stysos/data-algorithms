class Solution:
    
    def longestCommonPrefix(self, strs: list[str]) -> str:
        
        lengths = [len(string) for string in strs]
      
        substring = ""

        if strs[0] == "":
            print("returning on empty")
            return strs[0]
        
        elif len(strs) == 1:
            print("returning on length")
            return strs[0]
        
        
        for i in range(min(lengths)):
            
            char = strs[0][i] 
            
            for string in strs[1:]:
                if string[i] == char:
                    print("passing")source 
                    pass
                else:
                    return substring
            
            substring += char
            
        return substring

            
            
test_case = Solution()

print(test_case.longestCommonPrefix(["ab", "a"]))