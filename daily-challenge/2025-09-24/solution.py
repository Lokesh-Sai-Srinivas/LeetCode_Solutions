"""
Problem: 166 - Fraction to Recurring Decimal  
Description: Given two integers representing a fraction, return its decimal representation as a string. If the fractional part repeats, enclose the repeating part in parentheses.  
Date: 2025-09-24
"""

class Solution:
    def fractionToDecimal(self, numerator: int, denominator: int) -> str:
        if numerator == 0:
            return "0"

        result = []

        # Handle sign
        if (numerator < 0) ^ (denominator < 0):
            result.append("-")

        num = abs(numerator)
        den = abs(denominator)

        # Integer part
        result.append(str(num // den))
        rem = num % den
        if rem == 0:
            return "".join(result)

        result.append(".")
        rem_pos = {}
        frac_part = []

        while rem != 0:
            if rem in rem_pos:
                frac_part.insert(rem_pos[rem], "(")
                frac_part.append(")")
                result.extend(frac_part)
                return "".join(result)

            rem_pos[rem] = len(frac_part)
            rem *= 10
            frac_part.append(str(rem // den))
            rem %= den

        result.extend(frac_part)
        return "".join(result)
