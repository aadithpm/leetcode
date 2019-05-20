class Solution {
    public int missingNumber(int[] nums) {
        List<Integer> range = new ArrayList<>();
        for(int i = 0; i <= nums.length; i++){
            range.add(i);
        }
        for(int i: nums){
            range.remove(new Integer(i));
        }
        return range.get(0);
    }
}