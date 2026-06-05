class Solution:
    def isPalindrome(self, s: str) -> bool:
        #first have to clean the string of non alphanumenric chars/spaces and make the string lowercase
        clean_string2 = s.lower()
        clean_string3 = [c for c in clean_string2 if c.isalnum()]

        #2pointers
        left_char_index = 0
        right_char_index = len(clean_string3)-1

        while right_char_index > left_char_index:
            if clean_string3[left_char_index] != clean_string3[right_char_index]:
                return False
            left_char_index +=1
            right_char_index -=1
        
        return True

