num = int(input("enter your number:  "))
original = num

# Even / Odd
if num % 2 == 0:
    print("Even Number")
else:
    print("Odd Number")

# Prime check
is_prime = True

if num < 2:
    is_prime = False
else:
    for i in range(2, num):
        if num % i == 0:
            is_prime = False
            break

if is_prime:
    print("Prime Number")
else:
    print("Not Prime Number")

# Palindrome check
rev = 0
temp = num

while temp > 0:
    digit = temp % 10
    rev = rev * 10 + digit
    temp = temp // 10

print("Reverse:", rev)

if rev == original:
    print("Palindrome")
else:
    print("Not Palindrome")
    
# Armstrong check
temp = original
total = 0

while temp > 0:
    digit = temp % 10
    total += digit ** 3
    temp = temp // 10

if total == original:
    print("Armstrong Number")
else:
    print("Not Armstrong Number")
    
    
# Factorial check
factorial = 1

if original < 0:
    print("Factorial not possible for negative numbers")
else:
    for i in range(1, original + 1):
        factorial *= i

    print("Factorial:", factorial)
    
    
# Digit sum
temp = original
digit_sum = 0

while temp > 0:
    digit = temp % 10
    digit_sum += digit
    temp = temp // 10

print("Digit Sum:", digit_sum)


# Largest digit
temp = original
largest = 0

while temp > 0:
    digit = temp % 10

    if digit > largest:
        largest = digit

    temp = temp // 10

print("Largest Digit:", largest)


# Smallest digit
temp = original
smallest = 9

while temp > 0:
    digit = temp % 10

    if digit < smallest:
        smallest = digit

    temp = temp // 10

print("Smallest Digit:", smallest)
