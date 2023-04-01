dicti = {1:'I', 4:'IV', 5:'V', 9: 'IX', 10:'X', 40:'XL', 50:'L', 90:'XC', 100:'C', 400: 'CD', 500:'D', 900:'CM', 1000:'M'}
dictiInv = {dicti[k]:k for k in dicti.keys()}
dictiList = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
class RomanNumerals:
    def to_roman(val):
        sol = []
        for i in dictiList:
            if val//i>0:
                sol.append(dicti[i]* (val//i))
            val = val%i
            if val == 0:
                break
        return ''.join(sol)

    def from_roman(roman_num):
        out = 0
        while len(roman_num)>0:
            if roman_num[:2] in dictiInv:
                out+=dictiInv[roman_num[:2]]
                roman_num = roman_num[2:]
            else:
                out+=dictiInv[roman_num[:1]]
                roman_num = roman_num[1:]
        return out