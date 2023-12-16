class Solution:
    def asteroidCollision(self, asteroids: list[int]) -> list[int]:
        """
        We are given an array asteroids of integers representing asteroids in a row.

        For each asteroid, the absolute value represents its size, 
        and the sign represents its direction (positive meaning right, negative meaning left).
        Each asteroid moves at the same speed.

        Find out the state of the asteroids after all collisions. 
        If two asteroids meet, the smaller one will explode. If both are the same size,
        both will explode. Two asteroids moving in the same direction will never meet.
        """
        
        def positive(value):
            if value > 0:
                return True 
            else: return False

        if (all([positive(asteroid) for asteroid in asteroids])) or (all([not positive(asteroid) for asteroid in asteroids])):
            return asteroids
        
        
        result = []
        n = len(asteroids)
        i = 0
        while i < n:
            if len(result):
                result.append(asteroids[i])
                
            else:
                prev, current = result[-1], asteroids[i]
                
                if prev < 0 or current > 0:
                    result.append(current)
                    
                else:
                    if prev == abs(current):
                        result.pop()
                    elif prev < abs(current):
                        result.pop()
                        i -= 1
            i += 1
        return result
        
        
        # new_asteroids = []
        # for i in range(len(asteroids)):
        #     # if asteroid is travelling left, and left asteroid is travelling right
            
        #     if i == len(asteroids) - 1:
        #         new_asteroids.append(asteroids[i])
        #         continue
            
        #     if asteroids[i] < 0 and asteroids[i+1] > 0:
                
        #         if abs(asteroids[i]) == asteroids[i+1]:
        #             # append neither
        #             continue
                    
                
        #         elif asteroids[i] > asteroids[i+1]:
        #             # append i
        #             new_asteroids.append(asteroids[i])
        #             continue
        #         else:
        #             # new_asteroids.append(asteroids[i-1])
        #             continue
                    
                    
        #     else:
        #         print(f"appending {asteroids[i]}")
        #         new_asteroids.append(asteroids[i])
                    
        # return new_asteroids
                
            
        
        
        
        

test_case = Solution()

# print(test_case.asteroidCollision([5,10,5]))

# print(test_case.asteroidCollision([-5,-10,-5]))


print(test_case.asteroidCollision([5,10,-5]))


print(test_case.asteroidCollision([8, -8]))
print(test_case.asteroidCollision([10,2,-5]))



