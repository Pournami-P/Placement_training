def CheckPassword(str, n):
    # At least 4 characters
    if n < 4:
        return 0

    # First character should not be a number
    if str[0].isdigit():
        return 0

    has_digit = False
    has_capital = False

    for ch in str:
        if ch == ' ' or ch == '/':
            return 0

        if ch.isdigit():
            has_digit = True

        if ch.isupper():
            has_capital = True

    if has_digit and has_capital:
        return 1

    return 0


str = input("Enter password: ")
n = len(str)

result = CheckPassword(str, n)

print(result)