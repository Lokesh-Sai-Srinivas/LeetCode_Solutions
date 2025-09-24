"""
Problem: 166 - Fraction to Recurring Decimal  
Description: Given two integers representing a fraction, return its decimal representation as a string. If the fractional part repeats, enclose the repeating part in parentheses.  
Date: 2025-09-24
"""

class Solution {
public:
    string fractionToDecimal(int numerator, int denominator) {
        if (numerator == 0)
            return "0";

        string result;

        if ((numerator < 0) ^ (denominator < 0))
            result += "-";

        long num = labs(numerator);
        long den = labs(denominator);

        long intPart = num / den;
        result += to_string(intPart);

        long rem = num % den;
        if (rem == 0)
            return result;

        result += ".";

        unordered_map<long, long> remPos;
        string fracPart;

        while (rem != 0) {
            if (remPos.count(rem)) {
                fracPart.insert(remPos[rem], "(");
                fracPart += ")";
                result += fracPart;
                return result;
            }

            remPos[rem] = fracPart.size();
            rem *= 10;
            fracPart += to_string(rem / den);
            rem %= den;
        }

        result += fracPart;
        return result;
    }
};
