class Solution {
    public List<String> fizzBuzz(int n) {
        if(n <= 0)
            return new ArrayList();
        TreeMap<Integer, String> wordMap = new TreeMap<>((a, b) -> a - b);
        wordMap.put(3, "Fizz");
        wordMap.put(5, "Buzz");
        
        List<String> thisStrs = new LinkedList();
        
        for(int i = 1; i <= n; i++){
            
            StringBuilder fizzBuzz = new StringBuilder();
            
            for(int number: wordMap.keySet()){
                if(i % number == 0)
                    fizzBuzz.append(wordMap.get(number));
            }
            
            thisStrs.add((fizzBuzz.length() == 0) ? String.valueOf(i) : fizzBuzz.toString());
        }
        
        return thisStrs;
    }
}