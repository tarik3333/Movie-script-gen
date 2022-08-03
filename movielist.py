
liste = []

def findRoman(number):
    num = [1, 4, 5, 9, 10, 40, 50, 90,
        100, 400, 500, 900, 1000]
    sym = ["I", "IV", "V", "IX", "X", "XL",
        "L", "XC", "C", "CD", "D", "CM", "M"]
    i = 12
    result = ""
      
    while number:
        div = number // num[i]
        number %= num[i]

        while div:
            result += sym[i]
            div -= 1
        i -= 1
    return result

for number in range(1, 155):
    liste.append(findRoman(number))

print(liste)
               
