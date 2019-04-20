import java.util.*;

class Solution {
    
    public int singleNumber(int[] nums) {
        /*
        Map<Integer, Integer> numsMap = new HashMap<>();
        
        for(int number: nums){
            if(numsMap.containsKey(number))
                numsMap.remove(number);
            else
                numsMap.put(number, 1);
        }
        
        return new ArrayList<Integer>(numsMap.keySet()).get(0);
        */
        
        int singleNumber = 0;
        for(int number: nums){
            singleNumber ^= number;
        }
        return singleNumber;
    }
}