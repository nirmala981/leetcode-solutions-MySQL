class Solution:
    def longestPalindrome(self, s):
        if len(s) < 2:
            return s

        start = 0
        end = 0

        for i in range(len(s)):

            # Odd length palindrome
            left = i
            right = i

            while left >= 0 and right < len(s) and s[left] == s[right]:
                left -= 1
                right += 1

            length1 = right - left - 1

            # Even length palindrome
            left = i
            right = i + 1

            while left >= 0 and right < len(s) and s[left] == s[right]:
                left -= 1
                right += 1

            length2 = right - left - 1

            length = max(length1, length2)

            if length > end - start:
                start = i - (length - 1) // 2
                end = i + length // 2

        return s[start:end + 1]
        