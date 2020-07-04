class Solution {
    public int[] plusOne(int[] digits) {
        int s = 1;
        for(int x = digits.length-1; x >= 0; x--){
            if(digits[x] == 9 && s == 1){
                digits[x] = 0;
            }else{
                digits[x] += s;
                break;
            }
            if(s != 0 && x == 0){
                int []array = new int[digits.length+1];
                for(int y = 0; y < digits.length; y++){
                    array[y+1] = digits[y];
                }
                array[0] = s;
                return array;
            }
            
        }
        return digits;
    }
}
