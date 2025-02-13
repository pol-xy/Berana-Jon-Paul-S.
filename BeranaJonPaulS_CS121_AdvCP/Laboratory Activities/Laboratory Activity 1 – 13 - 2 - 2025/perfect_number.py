num = int(input("Enter a number: "))
divisor_sum = 0

for i in range(1, num):
    if num % i == 0:
        divisor_sum += i

if num == divisor_sum:
    print(f"{num} is a perfect number")
else:
    print(f"{num} is not a perfect number")

          


