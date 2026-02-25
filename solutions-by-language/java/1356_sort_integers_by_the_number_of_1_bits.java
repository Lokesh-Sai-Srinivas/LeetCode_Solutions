class Solution {
    public int[] sortByBits(int[] arr) {
        for(int i = 0; i<arr.length; i++){
            arr[i] += 10001*Integer.bitCount(arr[i]);
        }
        Arrays.sort(arr);
        for(int i = 0; i<arr.length; i++){
            arr[i] -= 10001*(arr[i]/10001);
        }
        return arr;
    }
}