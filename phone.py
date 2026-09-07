# Input: digits = "23"
# Output: ["ad","ae","af","bd","be","bf","cd","ce","cf"]
# Example 2:
 
# Input: digits = ""
# Output: []
# Example 3:
 
# Input: digits = "2"
# Output: ["a","b","c"]E

digits = input()

d = {
    '2': 'abc',
    '3': 'def',
    '4': 'ghi',
    '5': 'jkl',
    '6': 'mno',
    '7': 'pqrs',
    '8': 'tuv',
    '9': 'wxyz'
}

if digits == "":
    print([])
else:
    res = [""]

    for digit in digits:
        temp = []

        for x in res:
            for y in d[digit]:
                temp.append(x + y)

        res = temp

    print(res)