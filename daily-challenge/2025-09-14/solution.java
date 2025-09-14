"""
Problem: 966 - Vowel Spellchecker  
Description: Given a wordlist and a list of queries, return the word from the wordlist that matches each query with the following priority: (1) exact match, (2) case-insensitive match, (3) vowel-error match (where vowels are treated as interchangeable). If no match is found, return an empty string.  
Date: 2025-09-14  
"""

public class Solution {
    public String[] spellchecker(String[] wordlist, String[] queries) {
        Set<String> exactWords = new HashSet<>(Arrays.asList(wordlist));
        Map<String, String> caseInsensitiveMap = new HashMap<>();
        Map<String, String> vowelErrorMap = new HashMap<>();

        for (String word : wordlist) {
            String lower = word.toLowerCase();
            String devoweled = devowel(lower);

            caseInsensitiveMap.putIfAbsent(lower, word);
            vowelErrorMap.putIfAbsent(devoweled, word);
        }

        String[] result = new String[queries.length];
        for (int i = 0; i < queries.length; i++) {
            String query = queries[i];
            if (exactWords.contains(query)) {
                result[i] = query;
            } else {
                String lower = query.toLowerCase();
                String devoweled = devowel(lower);
                if (caseInsensitiveMap.containsKey(lower)) {
                    result[i] = caseInsensitiveMap.get(lower);
                } else if (vowelErrorMap.containsKey(devoweled)) {
                    result[i] = vowelErrorMap.get(devoweled);
                } else {
                    result[i] = "";
                }
            }
        }
        return result;
    }

    private String devowel(String word) {
        StringBuilder sb = new StringBuilder();
        for (char c : word.toCharArray()) {
            if ("aeiou".indexOf(c) >= 0) {
                sb.append('*');
            } else {
                sb.append(c);
            }
        }
        return sb.toString();
    }
}
