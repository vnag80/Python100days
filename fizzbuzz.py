for num in range(1,101):
    if num % 3 == 0:
        if num % 5 == 0:
            print('FIZZBUZZ')
        else:
            print('FIZZ')
    elif num % 5 == 0:
        print('BUZZ')
    else:
        print(num)