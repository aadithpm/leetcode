def fizzBuzz(self, n: int) -> List[str]:
        ans = []
        for i in range(1, n + 1):
            this_s = ''
            
            if i % 3 == 0:
                this_s += 'Fizz'
            
            if i % 5 == 0:
                this_s += 'Buzz'
            
            ans.append(this_s if this_s != '' else str(i))
        
        return ans
