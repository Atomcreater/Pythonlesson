#Integer to Roman
#https://leetcode.com/problems/integer-to-roman/description/?source=submission-ac
class Solution:
    def intToRoman(self, num: int) -> str:

        M = 0
        CM = 0
        D = 0
        CD = 0
        XC = 0
        C = 0
        L = 0
        XL = 0
        X = 0
        IX = 0
        V = 0
        IV = 0
        I = 0
        M = num // 1000
        num = num - M * 1000
        if num // 900 == 1:
            CM = 1
            num = num - 900
        else:
            D = num // 500
            num = num - D * 500
        if num // 400 == 1:
            CD = 1
            num = num - 400
        else:
            C = num // 100
            num = num - C * 100
        if num // 90 == 1:
            XC = 1
            num = num - XC * 90
        else:
            L = num // 50
            num = num - L * 50
        if num // 40 == 1:
            XL = 1
            num = num - XL * 40
        else:
            X = num // 10
            num = num - X * 10
        if num // 9 == 1:
            IX = 1
            num = num - 9
        else:
            V = num // 5
            num = num - V * 5
        if num // 4 == 1:
            IV = 1
            num = num - 4
        else:
            I = num

        return (
                    'M' * M + 'CM' * CM + 'D' * D + 'CD' * CD + 'C' * C + 'XC' * XC + 'L' * L + 'XL' * XL + 'X' * X + 'IX' * IX + 'V' * V + 'IV' * IV + 'I' * I)