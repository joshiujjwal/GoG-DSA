def sumOfDigits(n):
    if n // 10 == 0:
        return n
    else:
        return n % 10 + sumOfDigits(n//10)
        

if __name__ == "__main__":
    print(sumOfDigits(99999))
