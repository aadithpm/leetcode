class Solution {
    public String countAndSay(int n) {
        String start_str = "1";
        for(int i = 1; i < n; i++){
            start_str = iterCountAndSay(start_str);
        }
        return start_str;
    }
    
    public static String iterCountAndSay(String start_str){
        StringBuilder sb = new StringBuilder();
        char refChar = start_str.charAt(0);
        int count = 1;
        
        for(int i = 1; i < start_str.length(); i++){
            if(start_str.charAt(i) == refChar)
                count++;
            else{
                sb.append(count);
                sb.append(refChar);
                count = 1;
                refChar = start_str.charAt(i);
            }
        }
        
        sb.append(count);
        sb.append(refChar);
        return sb.toString();
    }
}
