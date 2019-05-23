class Solution {
    
    public int climbStairs(int n) {
        double sqrtOfFive = Math.sqrt(5);
        return (int) ((Math.pow(( 1 + sqrtOfFive) / 2, n + 1) 
                      - Math.pow((1 - sqrtOfFive) / 2, n + 1)) / sqrtOfFive);
        
    }
    
}