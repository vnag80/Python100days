text = input("Please enter the text to encode/decode")
op = input(" Enter E for encode and D for decode")
shift = int(input("Enter the shift key value"))
alphabates = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
result = '';
for char in text:
 if op == 'E':
    result += alphabates[(alphabates.index(char) + shift) % len(alphabates)]
 if op == 'D' :
     result += alphabates[(alphabates.index(char) - shift + len(alphabates)) % len(alphabates)]
print(result)