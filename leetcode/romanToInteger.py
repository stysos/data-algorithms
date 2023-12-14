class Solution: 
    
    def romanToInt(self, s: str) -> int:
        
        char_map = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000
        }
        
        
        sum = 0
        previous = 10000
        for char in s:
            current = char_map[char]
            if current > previous:
                sum += current - 2*previous
            else:
                sum += current
            previous = current
            
        
        return sum
    
    
test_case = Solution()

test_case.romanToInt("MCMXCIV")