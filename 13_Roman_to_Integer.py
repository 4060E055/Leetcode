
print("------------first anser-------------------")
# -------------first anser-------------------------
class Solution:
    def romanToInt(self, s: str) -> int:
        roman_number = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}

        s_to_int = []
        ans = 0
        for i in s:
            s_to_int.append(roman_number[i])

        for i in range(len(s_to_int) - 1):

            if s_to_int[i] < s_to_int[i + 1]:
                ans -= s_to_int[i]

            else:
                ans += s_to_int[i]

        return ans + s_to_int[len(s_to_int) - 1]


if __name__ == "__main__":
    s = "MCMXCIV"  # 1990
    # s = "LVIII"
    new = Solution()
    print(new.romanToInt(s))
print("------------faster runtime anser-------------------")


# ----------------------------faster runtime anser-----------------


class Solution:
    def romanToInt(self, s: str) -> int:
        roman_number = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}

        s_to_int = []
        ans = 0
        n = 0
        for i in s[::-1]:
            s_to_int.append(roman_number[i])  # 反向選取羅馬符號，找出對應數字
            if n != 0:

                if s_to_int[n] < s_to_int[n - 1]:
                    ans -= s_to_int[n]
                    n += 1
                else:
                    ans += s_to_int[n]
                    n += 1
            else:
                ans += s_to_int[n]
                n += 1

        return ans


if __name__ == "__main__":
    s = "MCMXCIV"  # 1994
    # s = "LVIII"
    new = Solution()
    print(new.romanToInt(s))

print("-------------more faster runtime anser------------------")


# ----------------------------faster runtime anser-----------------


class Solution:
    def romanToInt(self, s: str) -> int:
        roman_number = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}

        s_to_int = []
        ans = 0
        n = 0
        for i in s[::-1]:
            s_to_int.append(roman_number[i])  # 反向選取羅馬符號，找出對應數字

            ans += roman_number[i]

            if s_to_int[n] < s_to_int[n - 1] and n > 0:
                ans -= s_to_int[n] * 2

            n += 1

        return ans


if __name__ == "__main__":
    s = "MCMXCIV"  # 1994
    # s = "LVIII"
    new = Solution()
    print(new.romanToInt(s))
