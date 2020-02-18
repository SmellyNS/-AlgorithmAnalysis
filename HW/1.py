def levenshtein_matrix(s1, s2, matrix_flag):
    n, m = len(s1), len(s2) #1
    current_row = range(n + 1) #2
    matrix = [current_row] #3
    for i in range(1, m + 1): #4
        current_row = [i] + [0] * n #5
        for j in range(1, n + 1): #6
            current_row[j] = matrix[i - 1][j - 1] #7
            if s1[j - 1] != s2[i - 1]: #8
                current_row[j] += 1 #9
            current_row[j] = min(current_row[j], matrix[i-1][j] + 1,
                                 current_row[j - 1] + 1) #10
        matrix.append(current_row) #11
    if matrix_flag: #12
        print_matrix(matrix) #13
    return matrix[m][n] #14
