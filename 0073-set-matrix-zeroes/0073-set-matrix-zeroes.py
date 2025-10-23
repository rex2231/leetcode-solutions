class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        
        first_row_zero = False
        first_col_zero = False

        for i in range(len(matrix)):
            if matrix[i][0] == 0:
                first_row_zero = True

        for j in range(len(matrix[0])):
            if matrix[0][j] == 0:
                first_col_zero = True

        # mark 0's in ref row and col
        for i in range(1,len(matrix)):
            for j in range(1,len(matrix[0])):
                if matrix[i][j] == 0:
                    matrix[i][0] = 0
                    matrix[0][j] = 0
        
        # set zero for needed row nd cols
        for i in range(1,len(matrix)):
            for j in range(1,len(matrix[0])):
                if matrix[i][0] == 0 or matrix[0][j] == 0:
                    matrix[i][j] = 0
        
        # zero fill the first row nd col
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if first_row_zero:
                    matrix[i][0]=0
                if first_col_zero:
                    matrix[0][j]=0