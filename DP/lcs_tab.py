def lcs_tab(s1, s2, tab):
     for i in range(1, len(s1)+1):
         for j in range(1, len(s2)+1):
            if s1[i-1] == s2[j-1]:
                tab[i][j] = 1 + tab[i-1][j-1]
            else:
                tab[i][j] = max(tab[i-1][j], tab[i][j-1])


if __name__ == "__main__":
    s1 = "AXZY"
    s2 = "AXY"
    m = 4
    n = 3
    tab = [[0] * (n + 1) for _ in range(m+1)]
    lcs_tab(s1,s2,tab)
    print(tab[m][n])
    