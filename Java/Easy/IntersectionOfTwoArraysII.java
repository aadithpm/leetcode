class Solution {
    public int[] intersect(int[] nums1, int[] nums2) {
        HashMap<Integer, Integer> map = new HashMap<>();
        ArrayList<Integer> intersection = new ArrayList<>();
        
        for(int num: nums1){
            if(map.containsKey(num))
                map.put(num, map.get(num) + 1);
            else
                map.put(num, 1);
        }
        
        for(int num: nums2){
            if(map.containsKey(num) && map.get(num) != 0){
                intersection.add(num);
                map.put(num, map.get(num) - 1);
            }
        }
        
        return intersection.stream()
            .mapToInt(i -> i)
            .toArray();
        
    }
}