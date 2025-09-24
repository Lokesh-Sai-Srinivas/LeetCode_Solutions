"""
Problem: 166 - Fraction to Recurring Decimal  
Description: Given two integers representing a fraction, return its decimal representation as a string. If the fractional part repeats, enclose the repeating part in parentheses.  
Date: 2025-09-24
"""

class Solution {
    public String fractionToDecimal(int numerator, int denominator) {
        if (numerator == 0) return "0";

        StringBuilder result = new StringBuilder();

        // Handle sign
        if ((numerator < 0) ^ (denominator < 0)) result.append("-");

        long num = Math.abs((long) numerator);
        long den = Math.abs((long) denominator);

        // Integer part
        result.append(num / den);
        long rem = num % den;
        if (rem == 0) return result.toString();

        result.append(".");
        Map<Long, Integer> remPos = new HashMap<>();
        StringBuilder fracPart = new StringBuilder();

        while (rem != 0) {
            if (remPos.containsKey(rem)) {
                fracPart.insert(remPos.get(rem), "(");
                fracPart.append(")");
                result.append(fracPart);
                return result.toString();
            }

            remPos.put(rem, fracPart.length());
            rem *= 10;
            fracPart.append(rem / den);
            rem %= den;
        }

        result.append(fracPart);
        return result.toString();
    }
}
