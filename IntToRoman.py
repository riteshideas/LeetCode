import math
class Solution:

    def __init__(self):
        self.roman = {
            "I" : 1,
            "V" : 5,
            "X" : 10,
            "L" : 50,
            "C" : 100,
            "D" : 500,
            "M" : 1000
            }


    def intToRoman(self, num: int) -> str:


        return_letter = ""
        # Check if input is the same as any number in the roman dict

        for key in self.roman:
            if num == self.roman[key]:
                return_letter += key


        # Else get from subtraction or addition

        if return_letter == "":
            
            # Need to find which values num is between
            for key in self.roman:


            

        return return_letter


mySol = Solution()
print(mySol.intToRoman(int(input())))
