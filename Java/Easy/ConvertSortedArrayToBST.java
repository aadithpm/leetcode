class Solution {
    public TreeNode sortedArrayToBST(int[] nums) {
        return constructTree(nums, 0, nums.length - 1);
    }
    
    public TreeNode constructTree(int[] nums, int l, int h){
        if(l > h)
            return null;
        int mid = (l + h) / 2;
        TreeNode root = new TreeNode(nums[mid]);
        root.left = constructTree(nums, l, mid - 1);
        root.right = constructTree(nums, mid + 1, h);
        return root;
    }
}