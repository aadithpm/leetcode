class Solution {
    public int[] twoSum(int[] nums, int target) {
        int[] indices = new int[2];
        HashMap<Integer, Integer> sumMapping = new HashMap<>();
        for(int i = 0; i < nums.length; i++){
            if(sumMapping.containsKey(nums[i])){
                indices[0] = sumMapping.get(nums[i]);
                indices[1] = i;
                break;
            }
            else{
                sumMapping.put(target - nums[i], i);
            }
        }
        return indices;
    }
}