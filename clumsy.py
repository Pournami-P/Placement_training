n = list(map(int, input().split()))

start = n[0]
end = n[1] if len(n) == 2 else 1

nums = list(range(start, end - 1, -1))

if len(nums) == 1:
    print(nums[0])
else:
    terms = []
    operators = []

    even_count = 0
    odd_count = 0

    for i in range(len(nums) - 1):
        current = nums[i]

        if current % 2 == 0:
            if even_count % 2 == 0:
                operators.append('/')
            else:
                operators.append('*')
            even_count += 1

        else:
            if odd_count % 2 == 0:
                operators.append('+')
            else:
                operators.append('-')
            odd_count += 1

    # First handle / and *
    values = [nums[0]]

    for i in range(len(operators)):
        if operators[i] == '/':
            values[-1] = values[-1] // nums[i + 1]

        elif operators[i] == '*':
            values[-1] = values[-1] * nums[i + 1]

        else:
            values.append(nums[i + 1])

    # Now handle + and -
    result = values[0]
    j = 1

    for i in range(len(operators)):
        if operators[i] == '+':
            result += values[j]
            j += 1

        elif operators[i] == '-':
            result -= values[j]
            j += 1

    print(result)