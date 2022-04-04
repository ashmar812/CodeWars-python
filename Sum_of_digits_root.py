#Given n, take the sum of the digits of n. If that value has more than one digit, continue reducing in this way until a single-digit number is produced. The input will be a non-negative integer
def digital_root(n):
    while(n>9):
        n=sum(list(map(int, str(n).strip())))
    return n
