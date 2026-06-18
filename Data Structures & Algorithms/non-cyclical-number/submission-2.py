class Solution:
    def isHappy(self, n: int) -> bool:

        ans= sum((int(num)**2) for num in str(n))
        listofnums = []

        while ans != 1:

            ans = sum((int(num)**2) for num in str(ans))

            if(ans in listofnums):
                return False

            if (ans == 1):
                return True
            else: 
                listofnums.append(ans)
        
        return True