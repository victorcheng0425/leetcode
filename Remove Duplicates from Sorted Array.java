class Solution {
    public int removeDuplicates(int[] nums) {
        int flag = 0;
        for(int x = 1; x < nums.length; x++){
            if(nums[flag] == nums[x]){
                continue;
            }
            flag++;
            nums[flag] = nums[x];
        }
        return flag+1;
    }
}
