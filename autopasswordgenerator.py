import random;
letters = ["A","B","C"];
len_letter = len(letters)
numbers = ['0','1','2','3','4','5','6','7','8','9']
len_numbers = len(numbers)
symbols = ['%','*','$','#','@']
len_symbols = len(symbols)
num_letters = int(input("Enter Number of Letters"))
num_numbers = int(input("Enter Number of numbers"))
num_symbols = int(input("Enter Number of symbols"))
print(f"{num_symbols}  {num_letters} {num_numbers}")
password = '';
for num in range(0,num_letters):
    password += letters[random.randint(0,len_letter-1)]
for num in range(0, num_numbers):
    password += numbers[random.randint(0, len_letter - 1)]
for num in range(0, num_symbols):
    password += symbols[random.randint(0, len_letter - 1)]
print(password);
