def levenshtein_matrix(s1, s2, matrix_flag):
    n, m = len(s1), len(s2) #1
    current_row = range(n + 1) #2
    matrix = [current_row] #3
    for i in range(1, m + 1): 
        current_row = [i] + [0] * n #4
        for j in range(1, n + 1): 
            current_row[j] = matrix[i - 1][j - 1] #5
            if s1[j - 1] != s2[i - 1]: #6
                current_row[j] += 1 #7
            current_row[j] = min(current_row[j], matrix[i-1][j] + 1,
                                 current_row[j - 1] + 1) #8
        matrix.append(current_row) #9
    if matrix_flag: #10
        print_matrix(matrix) #11
    return matrix[m][n] #12
