def decrypt():

  def cipher(code):

    code = [*code.split()]
    binary_list = []
    high_lenght = 0
    
    for i in range(len(code)):
      code_converted = [*f"{int(code[i]):#010b}"[2:]]
      code_converted.reverse()
      if len(code_converted) > high_lenght:
        high_lenght = len(code_converted)
  
    for i in range(len(code)):
      code_converted = [*f"{int(code[i]):#010b}"[2:]]
      code_converted.reverse()
      while len(code_converted) != high_lenght:
        code_converted.append("0")
      binary_list.append("".join(code_converted))
  
    byte_index = high_lenght - 1
    new_byte = []
    final_byte = []
  
    #create new set of byte with the last bit of each byte, then the one before the last, and etc...
    for i in range(high_lenght):
      for i in range(len(binary_list)):
        bi = [*binary_list[i]]
        new_byte.append(bi[byte_index])
      byte_index -= 1
      final_byte.append("".join(new_byte))
      new_byte.clear()
    
    
    for i in range(len(final_byte)):
      code = int(final_byte[i], 2)
      if code != 0:
        decrypted_code = chr(code - 1)
        print(Fore.GREEN + str(decrypted_code), end="")

  #break the word in an array with each letters
  code = str(input(Fore.WHITE + "Enter code : "))
  if len(code.split()) == 1:
    cipher(code)
  else: 
    code = code.split("/")
    for i in range(len(code)):
      cipher(code[i])
      print(" ", end="")
  

def encrypt():

  def cipher(word):

    word = [*word]
    binary_list = []
    ascii = []

    #create a list of the ascii characters
    for i in range(128):
        ascii.append(chr(i))

    for i in range(len(word)):
      if word[i] in ascii:
        binary = ascii.index(word[i]) + 1 #find the index of the character in the ascii list
        binary_list.append(f"{binary:#010b}"[2:]) #convert that index in binary and append it to a list
      else:
        pass
    
    byte_index = 7
    new_byte = []
    final_byte = []
    
    #create new set of byte with the last bit of each byte, then the one before the last, and etc...
    for i in range(byte_index):
      for i in range(len(binary_list)):
        bi = [*binary_list[i]]
        new_byte.append(bi[byte_index])
      byte_index -= 1
      final_byte.append("".join(new_byte)) #append new binary code to a list
      new_byte.clear()
    
    #reconvert binary to numbers
    for i in range(len(final_byte)):
      code = int(final_byte[len(final_byte) - 1 - i], 2) #reverse the order of the answer
      print(Fore.GREEN + str(code), end=" ")
      
  #break the word in an array with each letters
  text = str(input(Fore.WHITE + "Enter text : "))
  split_text = text.split(" ")
  if len(split_text) == 1:
    cipher(split_text[0])
  else: 
    for i in range(len(split_text)):
      cipher(split_text[i])
      print("/ ", end="")
