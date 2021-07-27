"""
z = 0

while z < 5:
    z += 1
    print(z)

for i in range(7, 21, 3):
    print(i)

num = 0

while num < 3:
    num = num + 1
else:
    for j in range(num, num+3):   #3, 6
        #print("j --> ", j)
        print("Num -->", num)

print("La Pizza de Don Cangrejo \\\nes la mejor.")
print()
print("Para ti\ny para mí.")

print("La Witsi Witsi Arañar","subió","a su telaraña.")

print("Mi nombre es", "Python.", end=" ")
print("Monty Python.")

print("Mi nombre es", end="")
print("Monty Python.")

print('Hoy', 'amanecimos' + 'rica', 'sabrosa' + 'deliciosa', 'porque', 'puedo', sep='-')

print("Mi", "nombre", "es", sep="_", end="*")
print("Monty", "Python.", sep="*", end="*\n")

print("Tu","Nerd","es", "libertad", "y")
print("diversión")

print("    *\n   * *\n  *   *\n *     *\n***   ***\n  *   *\n  *   *\n  *****", end = "  ")

print()
print(-6 // 4)
print(6. // -4)

print(6 // 4)
print(6. // 4)


print((2**2)**3)

print(1//2*3)
print(0)

print(2//4)

x = 2/4

print(4/x)

a = 11 % 4
a = a % 4
b = 4 % a
print(b)

print(1/2+3//3+4**2)
"""
"""
x = input()
y = input()

print(x+y)

a = int(input())
b = int(input())

a = a / b
b = b / a

print(b)
"""

"""
j = int(input())
k = int(input())

j = j % k
j = j % k
k = k % j

print(k)
"""

"""
def print_prime(number):
    factor = 2
    while factor <= number:
        if number % factor == 0:
            print(factor)
            number = number / factor
        else:
            factor += 1

    return 'Done'

print_prime(101)


def is_power_of_two(n):
    while n % 2 == 0 and n > 1:
        n = n / 2
    if n == 1:
        return True

    return False

print(is_power_of_two(0))
print()
print(is_power_of_two(1))
print()
print(is_power_of_two(8))
print()
print(is_power_of_two(9))


def sum_divisor(n):
    sum = 0
    aux = n-1
    
    while aux > 0:
        if n % aux == 0:
            sum += aux
        aux-=1
    return sum

print(sum_divisor(0))
print(sum_divisor(3))
print(sum_divisor(36))
print(sum_divisor(102))


def multiplication_table(number):
    multiplier = 1

    while multiplier <= 5:
        result = multiplier * number
        if result > 25:
            break

        print(str(number) + "x" + str(multiplier) + "=" + str(result))

        multiplier += 1

multiplication_table(3)

multiplication_table(5)

multiplication_table(8)

"""

def cacluate(*num):
    li = []
    avg = sum(num)/len(num)
    for i in num:
        if i > avg:
            li.append(i)
    return avg,li
count = cacluate(12,13,14,15,16)

print (count)


sara = [44, 54, 64, 74, 104]

sarados = [data+6 for data in sara ]

print(sarados)

