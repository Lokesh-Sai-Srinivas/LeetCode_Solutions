"""
Problem: 165 - Compare Version Numbers  
Description: Given two version numbers as strings, compare them and return -1 if version1 < version2, 1 if version1 > version2, or 0 if they are equal.  
Date: 2025-09-23
"""

class Solution {
public:
    int compareVersion(string version1, string version2) {
        int i = 0, j = 0, n1 = version1.size(), n2 = version2.size();
        while (i < n1 || j < n2) {
            int num1 = 0, num2 = 0;
            while (i < n1 && version1[i] != '.') {
                num1 = num1 * 10 + (version1[i++] - '0');
            }
            while (j < n2 && version2[j] != '.') {
                num2 = num2 * 10 + (version2[j++] - '0');
            }
            if (num1 < num2) return -1;
            if (num1 > num2) return 1;
            i++; j++;
        }
        return 0;
    }
};
