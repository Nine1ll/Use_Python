alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'] # index 0 ~ 25

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

def encrypt(text, shift):
  encode = []
  for c in text :
    index = 0
    for i in range(len(alphabet)) :
      if alphabet[i] == c :
        index = i + shift
    if index >= len(alphabet) :
      index = index - len(alphabet)
    encode.append(alphabet[index])
  return encode

print(f"{''.join(encrypt(text, shift))}")
