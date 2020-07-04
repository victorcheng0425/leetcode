class Solution {
    public boolean containsDuplicate(int[] nums) {
        HashMap<Integer, Integer> hash_map = new HashMap<Integer, Integer>();
        for(int x = 0; x < nums.length; x++){
            if(hash_map.get(nums[x]) == null){
                hash_map.put(nums[x], 1);
            }else{
                return true;
            }
        }
        return false;
    }
}
