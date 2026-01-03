public class Solution {
    public static int canBeTypedWords(String text, String brokenLetters) {
        boolean[] broken = new boolean[26];
        for (char ch : brokenLetters.toCharArray()) {
            broken[ch - 'a'] = true;
        }

        int count = 0;
        boolean canType = true;

        for (char ch : text.toCharArray()) {
            if (ch == ' ') {
                if (canType) count++;
                canType = true;
            } else if (broken[ch - 'a']) {
                canType = false;
            }
        }

        if (canType) count++; 

        return count;
    }
}