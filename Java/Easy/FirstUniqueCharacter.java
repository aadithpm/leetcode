class Solution {
    public int firstUniqChar(String s) {
        HashMap<Character, Integer> charMap = new HashMap<>();
        char[] letters = s.toCharArray();
        for(char c: letters){
            if(!charMap.containsKey(c))
                charMap.put(c, 1);
            else
                charMap.put(c, charMap.get(c) + 1);
        }
        for(int i = 0; i < letters.length; i++){
            if(charMap.containsKey(letters[i]))
                if(charMap.get(letters[i]) == 1)
                    return i;
        }
        return -1;
    }
}