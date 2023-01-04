import random

names = ['Angela','saran','venkat','sanvi', 'Sravanthi'];
print(len(names));
sel = random.randint(0, len(names) - 1)
print(names[sel] + " Is going to pay bill");