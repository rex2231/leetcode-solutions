class Solution:
    def addDigits(self, num: int) -> int:
        while num>9:
            num_list = list(str(num))
            int_num_list = list(map(int,num_list)) 
            num = sum(int_num_list)
        return num