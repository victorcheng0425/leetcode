class Solution {
    public void reverseString(char[] s) {
        int j = s.length-1;
        for(int i = 0; i <= s.length-1; i++){
            if(i == j || i>j){
                break;
            }else{
                char tmp = s[i];
                s[i] = s[j];
                s [j] = tmp;
                j--;
            }
            //System.out.println(s);
        }
    }
}
