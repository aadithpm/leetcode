class Solution {
    public int rob(int[] nums) {
    if(nums.length == 0)
      return 0;
    int valueSoFar = 0;
    int currentLoot = 0;
    for(int num: nums){
      int temp = valueSoFar;
      valueSoFar = Math.max(currentLoot + num, valueSoFar);
      currentLoot = temp;
    }
    return valueSoFar;
    }
}