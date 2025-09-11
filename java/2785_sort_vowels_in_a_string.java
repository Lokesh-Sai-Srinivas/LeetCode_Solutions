"""
Problem: 2785 - Sort Vowels in a String  
Description: Given a string s, sort only the vowels of the string in ascending order and return the resulting string. The relative positions of the consonants and non-vowel characters must remain unchanged. Vowels are defined as 'a', 'e', 'i', 'o', 'u' (both lowercase and uppercase).  
Date: 2025-09-11  
"""

class Solution {
    public String sortVowels(String s) {
        int n = s.length();
        char[] t = s.toCharArray();
        Set<Character> vowelsSet = new HashSet<>(Arrays.asList(
            'a','e','i','o','u','A','E','I','O','U'
        ));
        List<Character> vowles = new ArrayList<>();
        List<Integer> idx = new ArrayList<>();

        for(int i = 0; i < n; i++){
            char ch = s.charAt(i);
            if(vowelsSet.contains(ch)){
                vowles.add(ch);
                idx.add(i);
            }
        }
        Collections.sort(vowles);
        for (int i = 0; i < idx.size(); i++) {
            t[idx.get(i)] = vowles.get(i);
        }
        return new String(t);
    }
}
