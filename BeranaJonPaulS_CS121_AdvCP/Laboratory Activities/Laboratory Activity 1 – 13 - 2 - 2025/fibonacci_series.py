fib = int(input("Enter the number of terms: "))
firstTerm, secondTerm = 0, 1

if fib <= 0:
    print("Invalid Number.")
else:
    print("Fibonacci Series: ", end=(""))
    for i in range(fib):
        print(firstTerm, end=" ")
        firstTerm, secondTerm = secondTerm, firstTerm + secondTerm
          
