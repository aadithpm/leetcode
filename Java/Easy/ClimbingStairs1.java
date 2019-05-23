class Solution {
    
    public int climbStairs(int n) {
        int memo[] = new int[n + 1];
        return climb_stairs(0, n, memo);
    }
    
    public int climb_stairs(int i, int n, int memo[]){
        if(i > n)
            return 0;
        if(i == n)
            return 1;
        if(memo[i] > 0)
            return memo[i];
        
        memo[i] = climb_stairs(i + 1, n, memo) + climb_stairs(i + 2, n, memo);
        return memo[i];
    }
}