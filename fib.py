fib = int(input("Digite o numero que deseja a sequência de fibonacci: "))

fib0 = 0
fib1 = 1
cont = 0

print(f"a sequência fibonacci do número {fib} será: ")
print(f'{fib0}\n{fib1}')

while fib1 < fib:
    fib1 = fib1 + fib0
    print(fib1)
    fib0 = fib1 - fib0
    cont += 1
