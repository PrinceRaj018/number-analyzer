while True:
    print("1. Even / Odd")
    print("2. Prime Check")
    print("3. Palindrome Check")
    print("4. Armstrong Check")
    print("5. Factorial")
    print("6. Digit Sum")
    print("7. Largest Digit")
    print("8. Smallest Digit")
    print("9. Exit")
    print("-" * 30)

    choice = int(input("Enter choice: "))

    if choice == 9:
        break

    elif choice == 1:
        num = int(input("enter your number: "))

        if num % 2 == 0:
            print("Even Number")
        else:
            print("Odd Number")

    elif choice == 2:
        num = int(input("enter your number: "))

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

    elif choice == 3:
        num = int(input("enter your number: "))
        original = num

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

    elif choice == 4:
        num = int(input("enter your number: "))
        original = num

        total = 0
        temp = num

        while temp > 0:
            digit = temp % 10
            total += digit ** 3
            temp = temp // 10

        if total == original:
            print("Armstrong Number")
        else:
            print("Not Armstrong Number")

    elif choice == 5:
        num = int(input("enter your number: "))

        factorial = 1

        if num < 0:
            print("Factorial not possible for negative numbers")

        else:
            for i in range(1, num + 1):
                factorial *= i

            print("Factorial:", factorial)

    elif choice == 6:
        num = int(input("enter your number: "))

        digit_sum = 0
        temp = num

        while temp > 0:
            digit = temp % 10
            digit_sum += digit
            temp = temp // 10

        print("Digit Sum:", digit_sum)

    elif choice == 7:
        num = int(input("enter your number: "))

        largest = 0
        temp = num

        while temp > 0:
            digit = temp % 10

            if digit > largest:
                largest = digit

            temp = temp // 10

        print("Largest Digit:", largest)

    elif choice == 8:
        num = int(input("enter your number: "))

        smallest = 9
        temp = num

        while temp > 0:
            digit = temp % 10

            if digit < smallest:
                smallest = digit

            temp = temp // 10

        print("Smallest Digit:", smallest)
