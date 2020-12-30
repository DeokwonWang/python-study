def getPrime(n):
    ret = n
    if n == 0 or n == 1:
        return

    if n == 2 or n == 3:
        return ret

    for i in range(3, n+1, 2):
        for j in range(3, n, 2):
            a = i%j
            if a == 0:
                break

            else:
                ret = i
                break

    return ret

ret = getPrime(int(input('정수를 입력하세요: ')))
print(ret)
