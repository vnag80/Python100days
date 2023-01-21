def prime_checker(number):
    primenumber = True
    half = int((number+1)/2)
    print(half)
    for num in range(2,half+1):

        if number % num == 0:
            primenumber = False;

    if primenumber:
        print(f"{number} is prime")
    else:
        print(f"{number} is not prime")

prime_checker(47)
