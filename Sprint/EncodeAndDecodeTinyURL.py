class Codec:
    def __init__(self):
        self.codecs = {}
        self.short_to_long = {}
        self.long_to_short = {}
        self.alphabet = string.ascii_letters + string.digits
        
    def encode(self, longUrl):
        """Encodes a URL to a shortened URL.
        
        :type longUrl: str
        :rtype: str
        """
        if longUrl not in self.long_to_short:
            short = self.get_short(longUrl)
            self.short_to_long[short] = longUrl
            self.long_to_short[longUrl] = short
            return 'http://tinyurl.com/' + short
            
    def decode(self, shortUrl):
        """Decodes a shortened URL to its original URL.
        
        :type shortUrl: str
        :rtype: str
        """
        shortUrl = shortUrl[-6:]
        if shortUrl in self.short_to_long:
            return self.short_to_long[shortUrl]
        
    def get_short(self, longUrl):
        code = ''.join(random.choice(self.alphabet) for i in range(6))
        if code in self.short_to_long:
            code = self.get_short(longUrl)
        return code

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(url))
