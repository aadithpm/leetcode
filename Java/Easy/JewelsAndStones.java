class Solution {
    public int numJewelsInStones(String J, String S) {
        return S.chars().mapToObj(c -> (char) c)
            .filter(c -> J.contains(String.valueOf(c)))
            .collect(Collectors.toList())
            .size();
    }
}