class Solution {
    public boolean isHappy(int n) {
        Set<Integer> loopedNumbers = new HashSet<Integer>();
        int square, remainder;
        while(loopedNumbers.add(n)){
            square = 0;
            while(n > 0){
                remainder = n % 10;
                square += remainder * remainder;
                n = n / 10;
            }
            if(square == 1)
                return true;
            else
                n = square;
        }
        return false;
    }
}