import fractions

#mat1 벡터를 a배해서 mat2 벡터에 더함
def as_vector(mat1,a,mat2):
    m = len(mat1)
    for i in range(m):
        mat2[i] = mat2[i] + a * mat1[i]
    return mat2

#벡터를 a로 나눔
def div_vector(mat,a):
    m = len(mat)
    for i in range(m):
        #mat[i] /= a
        mat[i] = fractions.Fraction(mat[i],a)
    return mat

#벡터의 행을 서로 바꿈
def rc_vector(mat,a1,a2):
    mat[a1],mat[a2] = mat[a2],mat[a1]

#Square_Matrix 인 mat와 크기가 동일한 identity_matrix를 생성
def identity_matrix(mat):
    m = len(mat)
    n = len(mat[0])
    idmat = []
    if (m != n):
        return(f"이 프로그램은 Square Matrix의 Inverse Matrix를 구하는것만 지원합니다.\n입력해주신 Matrix는 {m} X {n} Matrix로 Square Matrix가 아닙니다.")
    else:
        for i in range(m):
            row_list = []
            for j in range(n):
                if (i == j):
                    row_list.append(1)
                else:
                    row_list.append(0)
            idmat.append(row_list)
    return(idmat)

#입력받은 mat을 Gauss-Jordan Elimination 하기위해 pivoting
def pivoting(mat):
    pivoted_mat = []
    count = 0
    m = (len(mat))
    n = len(mat[0])
    for i in range(m):
        for j in range(n):
            if (mat[j][count] != 0):
                pivoted_mat.append(mat[j])
                mat[j] = []
                count += 1
                for k in range(m):
                    mat[j].append(0)
                if (count == m):
                    break;
        if (count == m):
            break;
    if (len(mat) == len(pivoted_mat)):
        return(pivoted_mat)
    else:
        pass

#mat 의 Inverse Matrix를 구하기 위해 mat 과 mat의 idmat 을 Forward_elimination
def for_eli(mat,idmat):
    m = len(mat)
    for i in range(m):
        s = mat[i][i]
        if (s == 0):
            return("Error: Matrix is not Invertable")
        if (i == m-1):
            div_vector(mat[i],s)
            div_vector(idmat[i],s)
        else:
            div_vector(mat[i],s)
            div_vector(idmat[i], s)
        for j in range(i+1,m):
            as_vector(idmat[i], -mat[j][i], idmat[j])
            as_vector(mat[i], -mat[j][i], mat[j])

    return mat,idmat

#mat의 Inverse Matrix를 구하기 위해 Forward_elimination이 끝난 mat 과 idmat 을 Backward_elimination
def back_eli(mat,idmat):
    m = len(mat)
    for i in range(m):
        s = mat[m-i-1][m-i-1]
        if (s == 0):
            return ("Error: Matrix is not Invertable")
        for j in range(i+1,m):
            as_vector(idmat[m-i-1],-mat[m-j-1][m-i-1],idmat[m-j-1])
            as_vector(mat[m-i-1],-mat[m-j-1][m-i-1],mat[m-j-1])

    return mat,idmat


#mat = [[1,2,3],[2,5,3],[1,0,8]]
#mat = [[2,0,1],[-2,3,4],[-5,5,6]]
mat = [[2,2,0],[-2,1,1],[3,0,1]]
idmat = identity_matrix(mat)
pivoted_mat = pivoting(mat)

for_eli(pivoted_mat,idmat)
print(for_eli(pivoted_mat,idmat))
back_eli(pivoted_mat,idmat)
print(back_eli(pivoted_mat,idmat))
inverse_mat = idmat

for i in range(len(inverse_mat)) :
    for j in range(len(inverse_mat[0])) :
        if (inverse_mat[i][j] - int(inverse_mat[i][j])) != 0 :
            frac = fractions.Fraction(inverse_mat[i][j])
            inverse_mat[i][j] = str(frac.numerator) + "/" + str(frac.denominator)

print(inverse_mat)
