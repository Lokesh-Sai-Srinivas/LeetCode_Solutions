class Solution {
    public char nextGreatestLetter(char[] letters, char target) {
        if(target == 'z') return letters[0];

        for(char ch : letters) {
            if(ch > target) return ch;
        }
        
        return letters[0];
    }
}
