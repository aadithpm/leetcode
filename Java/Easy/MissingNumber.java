class Solution {
    public int missingNumber(int[] nums) {
        int bigSum = 0;
        int smallSum = 0;
        int i = 0;
        for(i = 0; i < nums.length; i++){
            bigSum += i;
            smallSum += nums[i];
        }
        return bigSum + i - smallSum;
    }
}