class Solution:
    def isHappy(self, n: int) -> bool:
        cache = set([])
        
        while True:
            new_number = 0
          
            while n > 0:
                new_number += (n % 10)**2
                n //= 10
            
            if new_number in cache:
                return False
            
            cache.add(new_number)

            if new_number == 1:
                return True

            n = new_number