class Solution {
    public void rotate(int[] nums, int k) {
        HashMap<Integer, Integer> hash_map = new HashMap<Integer, Integer>(); 
        for(int x = 0; x < nums.length; x++){
            if(hash_map.get(x) == null){
                int dest = (x+k)%nums.length;
                hash_map.put(dest, nums[dest]);
                nums[dest] = nums[x];
            }else{
                int dest = (x+k)%nums.length;
                hash_map.put(dest, nums[dest]);
                nums[dest] = hash_map.get(x);
                hash_map.remove(x);
            }
        }
    }
}
