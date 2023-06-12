"""
Given the two integer values of a fraction, numerator and denominator, implement a function that returns the fraction in string format. If the fractional part repeats, enclose the repeating part in parentheses.



1. edge cases if numerator is zero return 0
2. 

"""

def fraction_to_decimal(numerator, denominator):
    if numerator == 0:
        return 0
    result, remainder_map = "", {}
    
    if (numerator < 0) ^  (denominator < 0):
        result += '-'
        numerator = abs(numerator)
        denominator = abs(denominator)
    
    quotient, remainder = divmod(numerator, denominator)
    remainder *= 10
    result += str(int(quotient))

    if remainder == 0:
        return result
    else:
        result += "."
        while remainder != 0:
            if remainder in remainder_map:
                beginning = remainder_map[remainder]
                left = result[0: beginning]
                right = result[beginning:len(result)]
                result = left + "(" + right + ")"
                return result
            remainder_map[remainder] = len(result)
            quotient, remainder = divmod(remainder, denominator)
            result += str(int(quotient))
            remainder *= 10
    return result

print(fraction_to_decimal(5, 333))