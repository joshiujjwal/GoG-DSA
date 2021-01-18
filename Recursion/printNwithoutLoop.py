def printNos(N):
    if N == 0:
        return
    else:
        printNos(N-1)
    print(N, end=" ")
    return 


if __name__  == "__main__":
    printNos(64)