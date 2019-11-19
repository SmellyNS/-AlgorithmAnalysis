import string
import random
from time import time


def Levenshtein(str1, str2):
    n = len(str1)
    m = len(str2)
    if not min(n,m):
        return max(n,m)
    return min(Levenshtein(str1, str2[:-1]) + 1,
               Levenshtein(str1[:-1], str2) + 1,
               Levenshtein(str1[:-1], str2[:-1]) + (str1[-1] != str2[-1]))


def Wagner_Fischer(a, b):
    n = len(a)
    m = len(b)
    if n > m:
        a, b = b, a
        n, m = m, n

    current_row = range(n + 1)
    for i in range(1, m + 1):
        previous_row, current_row = current_row, [i] + [0] * n
        for j in range(1, n + 1):
            add, delete, change = previous_row[j] + 1, current_row[j - 1] + 1, previous_row[j - 1]
            if a[j - 1] != b[i - 1]:
                change += 1
            current_row[j] = min(add, delete, change)

    return current_row[n]

def Damerau_Levenshtein(s1, s2):
    d = {}
    n = len(s1)
    m = len(s2)
    for i in range(-1,n+1):
        d[(i,-1)] = i+1
    for j in range(-1,m+1):
        d[(-1,j)] = j+1
 
    for i in range(n):
        for j in range(m):
            cost = s1[i] != s2[j]
            d[(i,j)] = min(
                           d[(i-1,j)] + 1, # delete
                           d[(i,j-1)] + 1, # insert
                           d[(i-1,j-1)] + cost, # substitute
                          )
            if i and j and s1[i]==s2[j-1] and s1[i-1] == s2[j]:
                d[(i,j)] = min (d[(i,j)], d[i-2,j-2] + cost) # transposition
 
    return d[n-1,m-1]


def TimeAnalysis(func, i, strlen1, strlen2):
    t1 = time()
    for i in range(i):
        str1 = ''.join(random.choice(string.ascii_lowercase) for i in range(strlen1))
        str2 = ''.join(random.choice(string.ascii_lowercase) for i in range(strlen2))
        func(str1,str2)
    t2 = time()
    return (t2-t1)/i


def main():
    a = input("Enter a: ")
    b = input("Enter b: ")
    print()
    times = []
    
    t1 = time()
    r_Levenshtein = Levenshtein(a, b)
    #for i in range(1000):
    #    Levenshtein(a, b)
    t2 = time()
    times.append(t2-t1)
    
    t1 = time()
    r_Wagner_Fischer = Wagner_Fischer(a, b)
    for i in range(1000):
        Wagner_Fischer(a, b)
    t2 = time()
    times.append(t2-t1)
    
    t1 = time()
    r_Damerau_Levenshtein = Damerau_Levenshtein(a, b)
    for i in range(1000):
        Damerau_Levenshtein(a, b)
    t2 = time()
    times.append(t2-t1)

    print("Levenshtein: ", r_Levenshtein)
    print("Time in ticks: ", times[0]*18.2)
    print()
    print("Wagner_Fischer: ", r_Wagner_Fischer)
    print("Time in ticks (average by 1000): ", times[1]*18.2/1000)
    print()
    print("Damerau_Levenshtein: ", r_Damerau_Levenshtein)
    print("Time in ticks (average by 1000): ", times[2]*18.2/1000)
    print()

    if input("Enter 'exit' if you dont want to continue time analysing") == "exit":
        return 0
    it = 50
    
    tableL =[]
    for i in range(8):
        tableL.append([])
        for j in range(8):
            tableL[i].append([])

    tableW =[]
    for i in range(8):
        tableW.append([])
        for j in range(8):
            tableW[i].append([])

    tableD =[]
    for i in range(8):
        tableD.append([])
        for j in range(8):
            tableD[i].append([])
    
    for i in range(1,9,2):
        for j in range(i,9,2):
            tableL[i-1][j-1] = TimeAnalysis(Levenshtein, it, i, j)
            print("Levenshtein: ", "{0:.15f}".format(tableL[i-1][j-1]))

            tableW[i-1][j-1] = TimeAnalysis(Wagner_Fischer, it, i, j)
            print("Wagner_Fischer: ", "{0:.15f}".format(tableW[i-1][j-1]))

            tableD[i-1][j-1] = TimeAnalysis(Damerau_Levenshtein, it, i, j)
            print("Damerau_Levenshtein: ", "{0:.15f}".format(tableD[i-1][j-1]))

    print("\t\t8\t\t6\t\t4\t\t2")
    for i in tableL:
        print('\n')
        for j in i:
            if j != []:
                print("{0:.10f}".format(j*18.2),end='\t')
    print('\n')
    
    for i in tableW:
        print('\n')
        for j in i:
            if j != []:
                print("{0:.10f}".format(j*18.2),end='\t')
    print('\n')
    
    for i in tableD:
        print('\n')
        for j in i:
            if j != []:
                print("{0:.10f}".format(j*18.2),end='\t')
    print('\n')
if __name__ == "__main__":
    main()
