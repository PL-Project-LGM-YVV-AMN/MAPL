import re
def not_in_row_or_column(mat,size,target_row,target_column):
    temp_vec = []
    new_mat = []
    for row in range(size):
        if row != 0:
            new_mat.append(temp_vec.copy())
            temp_vec.clear()
        for column in range(size):
            if row != target_row and column != target_column:
                temp_vec.append(mat[row][column])
    new_mat.append(temp_vec)
    new_mat = list([x for x in new_mat.copy() if x])
    return new_mat

def det(mat):
    mat_cpy = mat.copy()
    if len(mat) <= 1:
        return float(re.sub(r'\[|\]',"",str(mat_cpy)))
    else:
        sum = 0
        for row in range(len(mat)):
            sum += pow(-1,row)*mat[row][0]*det(not_in_row_or_column(mat_cpy,len(mat_cpy),row,0))
        return sum

def helper_adjoint(mat):
    temp_vec = []
    adjoint_mat = []
    for row in range(len(mat)):
        adjoint_mat.append(temp_vec[:])
        temp_vec.clear()
        for column in range(len(mat)):
            val = pow(-1,column)*det(not_in_row_or_column(mat,len(mat),row,column))
            temp_vec.append(val)
    adjoint_mat.append(temp_vec[:])
    temp_vec.clear()
    adjoint_mat = [x for x in adjoint_mat.copy() if x]
    return adjoint_mat





r1 = [1,2,3]
r2 = [4,5,6]
r3 = [7,8,9]
mat1 = [r1,r2,r3]
mat = [[1,2],[3,4]]
