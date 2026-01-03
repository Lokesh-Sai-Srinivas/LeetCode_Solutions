class Solution {
    public int maxFreqSum(String str) {
        int [] arr = new int [26];
        for(char ch : str.toCharArray()){
            arr[ch - 'a']++;
        }
        int freq1 = 0,freq2 = 0;
        for(int i = 0 ; i < arr.length ;i++){
            if(i == 'a' - 'a' || i == 'e' - 'a' || i == 'i' - 'a' || i == 'o' - 'a' || i == 'u' - 'a'){
                if(freq1 < arr[i] ){
                    freq1 = arr[i];
                }
            }else {
                if(freq2 < arr[i]){
                    freq2 = arr[i];
                }
            }
        }
        return freq1 + freq2;
    }
}