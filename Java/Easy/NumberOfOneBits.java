public class Solution {
    public int hammingWeight(int n) {
        int one_count = 0;
        while(n != 0){
            one_count += 1;
            n &= n - 1;
        }
        return one_count;
    }
}