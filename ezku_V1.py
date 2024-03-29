import string

def decrypt():

  def cipher(code):

    code = [*code.split()]
    binary_list = []

    alphabet = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
      
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
      #print("".join(code_converted))
      binary_list.append("".join(code_converted))
  
    byte_index = high_lenght - 1
    new_byte = []
    final_byte = []
  
    #create new set of byte with the last bit of each byte, then the one before the last, and etc...
    for i in range(high_lenght):
      for i in range(len(binary_list)):
        bi = [*binary_list[i]]
        new_byte.append(bi[byte_index])
      #print("".join(new_byte))
      byte_index -= 1
      final_byte.append("".join(new_byte))
      new_byte.clear()
    
    for i in range(len(final_byte)):
      code = int(final_byte[i], 2)
      if code != 0:
        decrypted_code = alphabet[code - 1]
        print(Fore.GREEN + str(decrypted_code), end="")

  #break the word in an array with each letters
  code = str(input(Fore.WHITE + "Enter code : "))
  if len(code.split()) < 2:
    cipher(code)
  else: 
    code = code.split("/")
    #print(code)
    for i in range(len(code)):
      cipher(code[i])
      print(" ", end="")
  


def encrypt():

  def cipher(word):

    word = [*word]
    binary_list = []

    for i in range(len(word)):
      if word[i].isalpha():
        binary = string.ascii_lowercase.index(word[i]) + 1
        #print(f"{binary:#010b}"[2:])
        binary_list.append(f"{binary:#010b}"[2:])
      else:
        #do nothing
        print("", end="")
    
    byte_index = 7
    new_byte = []
    final_byte = []
    
    #create new set of byte with the last bit of each byte, then the one before the last, and etc...
    for i in range(byte_index):
      for i in range(len(binary_list)):
        bi = [*binary_list[i]]
        new_byte.append(bi[byte_index])
      byte_index -= 1
      final_byte.append("".join(new_byte))
      new_byte.clear()
  
    def sum(l):
      total = 0
      for val in l:
        total = total + int(val)
      return total
    
    #reconvert binary to numbers
    for i in range(len(final_byte)):
      code = int(final_byte[len(final_byte) - 1 - i], 2) #reverse the order of the answer
      print(Fore.GREEN + str(code), end=" ")
      
  #break the word in an array with each letters
  word = str(input(Fore.WHITE + "Enter word : ").lower())
  if len(word.split()) < 2:
    cipher(word)
  else: 
    word = word.split()
    for i in range(len(word)):
      cipher(word[i])
      print("/ ", end="")
