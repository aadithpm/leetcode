class Solution:
    def validIP4(self, IP: str) -> bool:
        candidates = IP.split('.')
        if len(candidates) == 4:
            for candidate in candidates:
                if candidate.isnumeric() and 0 <= int(candidate) < 256 and (len(candidate) == 1 or candidate[0] != '0'):
                    continue
                else:
                    return False
            return True
        return False
    
    def validIP6(self, IP: str) -> bool:
        candidates = IP.split(':')
        if len(candidates) == 8:
            for candidate in candidates:
                if 0 < len(candidate) <= 4 and self.isValidIPHex(candidate):
                    continue
                else:
                    return False
            return True
        return False
    
    def isValidIPHex(self, sequence):
        return all(char in string.hexdigits for char in sequence)

    def validIPAddress(self, IP: str) -> str:
        if self.validIP4(IP):
            return 'IPv4'
        if self.validIP6(IP):
            return 'IPv6'
        return 'Neither'
