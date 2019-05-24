class Solution {
    public int maxSubArray(int[] nums) {
        int maximum = Integer.MIN_VALUE;
        int sum = 0;
        for(int i = 0; i < nums.length; i++){
            if(sum < 0){
                sum = nums[i];
                System.out.println("Sum: " + sum + "\nNums: " + nums[i]);
            }
            else
                sum += nums[i];
            maximum = sum > maximum ? sum: maximum;
        }
        return maximum;
    }
}