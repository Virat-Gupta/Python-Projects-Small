alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

def convert(text,shift):
    shifted_string = [alphabet[(ord(c) - 97 + shift)%26] for c in text]
    print(''.join(shifted_string))

if (direction.lower() in ("encrypt","e")):
    convert(text,shift)
elif (direction.lower() in ("decrypt","d")):
    convert(text,-shift)

