def FindAutoCount(n):
    if n is None:
        return 0

    for i in range(len(n)):
        count = 0

        for digit in n:
            if int(digit) == i:
                count += 1

        if int(n[i]) != count:
            return 0

    unique = set(n)

    return len(unique)


n = input("Enter the number: ")

result = FindAutoCount(n)

print(result)