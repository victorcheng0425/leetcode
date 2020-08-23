class Solution {
    public int reverse(int x) {
        int rev = 0;
        int pre = 0;
        while(x != 0){
            rev = rev*10 + x%10;
            if((rev-x%10)/10 != pre){
                return 0;
            }
            x = x/10;
            pre = rev;
            
        }
        return rev;
    }
}
