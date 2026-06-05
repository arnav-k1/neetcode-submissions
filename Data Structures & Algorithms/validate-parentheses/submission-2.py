class Solution:
    def isValid(self, s: str) -> bool:
        
        #make a dictionary
        s_dict = {")" : "(", "]" : "[", "}" : "{"}
        my_list = []

        for symbol in s:
            if symbol == "(" or symbol == "{" or symbol == "[":
                my_list.append(symbol)
            if (symbol == ")" or symbol == "}" or symbol == "]"):
                if not my_list:
                    return False
                if my_list[-1] == s_dict[symbol]:
                    my_list.pop()
                else:
                    return False
        
        return (not my_list)