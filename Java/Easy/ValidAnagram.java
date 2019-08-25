class Solution {
    public boolean isAnagram(String s, String t) {
        if(s.length() != t.length())
            return false;
        
        Map<Character, Integer> charMap = new HashMap<>();
        
        for(char c: s.toCharArray()){
            if(charMap.containsKey(c))
                charMap.put(c, charMap.get(c) + 1);
            else
                charMap.put(c, 1);
        }
        
        for(char c: t.toCharArray()){
            if(charMap.containsKey(c)){
                if(charMap.get(c) == 0)
                    return false;
                else
                    charMap.put(c, charMap.get(c) - 1);
            }
            else
                return false;
        }
        return true;
    }
}