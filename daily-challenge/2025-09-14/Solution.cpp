"""
Problem: 966 - Vowel Spellchecker  
Description: Given a wordlist and a list of queries, return the word from the wordlist that matches each query with the following priority: (1) exact match, (2) case-insensitive match, (3) vowel-error match (where vowels are treated as interchangeable). If no match is found, return an empty string.  
Date: 2025-09-14  
"""

using namespace std;

class Solution {
public:
    string devowel(const string& word) {
        string res;
        for (char c : word) {
            char lower = tolower(c);
            if (lower == 'a' || lower == 'e' || lower == 'i' || lower == 'o' || lower == 'u')
                res += '*';
            else
                res += lower;
        }
        return res;
    }

    vector<string> spellchecker(vector<string>& wordlist, vector<string>& queries) {
        unordered_set<string> exactWords(wordlist.begin(), wordlist.end());
        unordered_map<string, string> caseMap;
        unordered_map<string, string> vowelMap;

        for (const string& word : wordlist) {
            string lower = word;
            for (char& c : lower) c = tolower(c);
            string devoweled = devowel(word);
            if (caseMap.find(lower) == caseMap.end()) caseMap[lower] = word;
            if (vowelMap.find(devoweled) == vowelMap.end()) vowelMap[devoweled] = word;
        }

        vector<string> result;
        for (const string& query : queries) {
            if (exactWords.count(query)) {
                result.push_back(query);
            } else {
                string lower = query;
                for (char& c : lower) c = tolower(c);
                string devoweled = devowel(query);
                if (caseMap.count(lower)) {
                    result.push_back(caseMap[lower]);
                } else if (vowelMap.count(devoweled)) {
                    result.push_back(vowelMap[devoweled]);
                } else {
                    result.push_back("");
                }
            }
        }
        return result;
    }
};
