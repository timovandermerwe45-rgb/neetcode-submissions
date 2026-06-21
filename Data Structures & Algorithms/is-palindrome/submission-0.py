class Solution:
    def isPalindrome(self, s: str) -> bool:
        al_num_only = [c.lower() for c in s if c.isalnum()]
        al_num_only_rev = list(reversed(al_num_only))

        return al_num_only == al_num_only_rev

        
        