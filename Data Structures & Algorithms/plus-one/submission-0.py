class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:

        single_number = int("".join([str(n) for n in digits]))

        single_number = single_number + 1

        single_number = [int(digit) for digit in str(single_number)]

        return single_number        