def countDigits(n):
    if n // 10 == 0:
        return 1
    else:
        return 1 + countDigits(n//10)
        

if __name__ == "__main__":
    print(countDigits(99999))
