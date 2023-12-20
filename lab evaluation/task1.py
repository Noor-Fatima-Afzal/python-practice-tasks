def prime_or_not(a):
    lis = []
    for i in range(a):
        x = int(input("Enter number: "))
        lis.append(x)
    print("Entered numbers:", lis)

    for num in lis:
        is_prime = True
        for j in range(2, num):
            if num % j == 0:
                is_prime = False
                break
        if is_prime:
            print(f"{num} is prime.")
        else:
            print(f"{num} is not prime.")

prime_or_not(2)
