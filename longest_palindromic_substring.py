class Solution:
    def expand_around_center(self , s, left, right):
        while left >= 0 and right < len(s) and s[left] == s[right]:
            left -= 1
            right += 1
        return s[left + 1:right]
    def longest_palindromic_substring(self , s):
        if not s:
            return ""
        
        longest = ""
        
        for i in range(len(s)):
            odd_palindrome = self.expand_around_center(s, i, i)
            if len(odd_palindrome) > len(longest):
                longest = odd_palindrome
            
            even_palindrome = self.expand_around_center(s, i, i + 1)
            if len(even_palindrome) > len(longest):
                longest = even_palindrome
        
        return longest

        


    

a = Solution()
print(a.longest_palindromic_substring("abbd"))

    

