class Solution {
    public void moveZeroes(int[] nums) {
        if(nums == null || nums.length == 0)
            return;
        
        int i = 0;
        for(int number: nums){
            if(number != 0)
                nums[i++] = number;
        }
        
        while(i < nums.length){
            nums[i++] = 0;
        }
    }
}