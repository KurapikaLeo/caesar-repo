

# caesar encryption 
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
            'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p',
            'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']



def encrypt(plain_text, shift_amount):
  cipher_text = ""
  for letter in plain_text:
    position = alphabet.index(letter)
    new_position = position + shift_amount
    new_letter = alphabet[new_position]
    cipher_text += new_letter
  print(f"The encoded text is {cipher_text}")

def decrypt(cipher_text, shift_amount):
  plain_text = ""
  for letter in cipher_text:
    position = alphabet.index(letter)
    new_position = position - shift_amount
    plain_text += alphabet[new_position]
  print(f"The decoded text is {plain_text}")


from art import logo

print(logo)


should_end = False
while not should_end:    # if should end is false , the user is asked to input the following fields : direction, text, shift
    
    while True:
      try:
        direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
        print("choose correct option: encode or decode ")
        if direction == 'encode' or direction == 'decode':
          break
      except:
        direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
        continue


    
    text = input("Type your message:\n").lower()
       
    
    
    
    while True:
      try:
        shift = int(input("Type the shift number:\n"))
        if type(shift) == int:
          break
      except ValueError:
         print("it should be a number!!")
         continue

   
    shift = shift % 26  #this makes the shift number smaller, the shift mod the alphabet 

    
    def main():
      if direction == 'encode':
        encrypt(plain_text = text, shift_amount = shift)
      else:
        decrypt(cipher_text = text, shift_amount = shift)

    main()
  
    restart = input("Type 'yes' if you want to go again. Otherwise type 'no'.\n")
    if restart == "no":
        should_end = True
        print("bye:)")



