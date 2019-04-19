class Solution(object):
    def sieve(self, n):
        final_primes = []
        primes = [True] * n
        primes[0], primes[1] = False, False

        for idx, val in enumerate(primes):
            if val:
                final_primes.append(idx)
                for factors in range(idx * idx, n, idx):
                    primes[factors] = False

        return final_primes
    
    def countPrimes(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n < 3:
            return 0
        return len(self.sieve(n))