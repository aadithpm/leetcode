class Solution(object):
    def numPrimeArrangements(self, n):
        """
        :type n: int
        :rtype: int
        """
        prime = [True for i in range(n + 1)]
        i = 2
        while i * i <= n:
            if prime[i]:
                for j in range(i * i, n + 1, i):
                    prime[j] = False
            i += 1
        
        primes = sum(prime[2:] )
        return math.factorial(primes) * math.factorial(n - primes) % (10 ** 9 + 7)
