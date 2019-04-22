import java.util.HashMap;
import java.util.Map;

class Solution {
    public int majorityElement(int[] nums) {
        Map<Integer, Integer> countMap = new HashMap<>();
        
        for(int num: nums){
            
            if(countMap.containsKey(num))
                countMap.put(num, countMap.get(num) + 1);
            else
                countMap.put(num, 1);
            
        }
        
        return countMap.entrySet().stream()
            .max((e1, e2) -> e1.getValue() > e2.getValue() ? 1 : -1)
            .get()
            .getKey();
            
    }
}