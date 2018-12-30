class Solution:
    def fizzBuzz(self, n):
        fizzbuzz = []
        for i in range(1, n + 1):
            if i % 3 == 0 and i % 5 == 0:
                fizzbuzz.append('FizzBuzz')
            elif i % 3 == 0:
                fizzbuzz.append('Fizz')
            elif i % 5 == 0:
                fizzbuzz.append('Buzz')
            else:
                fizzbuzz.append(str(i))
        return fizzbuzz