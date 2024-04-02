number = input()
sum_even = 0
sum_odd = 0

for el in number:
    if int(el) % 2 == 0:
        sum_even += int(el)
    else:
        sum_odd += int(el)

print(f"{sum_odd} {sum_even}")
