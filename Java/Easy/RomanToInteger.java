class Solution {
    public int romanToInt(String s) {
        int integer = 0;
        Map<Character, Integer> romanMapping = new HashMap<Character, Integer>(){{
            put('I', 1);
            put('V', 5);
            put('X', 10);
            put('L', 50);
            put('C', 100);
            put('D', 500);
            put('M', 1000);
        }};
        
        char[] romanWord = s.toCharArray();
        
        for(int i = 0; i < romanWord.length - 1; i++){
            if(romanMapping.get(romanWord[i]) < romanMapping.get(romanWord[i + 1]))
                integer -= romanMapping.get(romanWord[i]);
            else
                integer += romanMapping.get(romanWord[i]);
        }
        
        return integer + romanMapping.get(romanWord[romanWord.length - 1]);
    }
}