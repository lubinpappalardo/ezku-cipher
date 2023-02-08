from colorama import Fore, Style
import string


def decrypt():

  alphabet = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
  
  #break the code in an array with each numbers
  code = [*str(input(Fore.WHITE + "Enter code : ")).split()]
  #print(code)
    
  binary_list = []
  high_lenght = 0
  
  for i in range(len(code)):
    code_converted = [*f"{int(code[i]):#010b}"[2:]]
    code_converted.reverse()
    #print(code_converted)
    print("".join(code_converted))
    if len(code_converted) > high_lenght:
      high_lenght = len(code_converted)

  print(high_lenght)

  for i in range(len(code)):
    code_converted = [*f"{int(code[i]):#010b}"[2:]]
    code_converted.reverse()
    while len(code_converted) != high_lenght:
      code_converted.append("0")
    print("".join(code_converted))
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
  
  #reconvert binary to numbers
  for i in range(len(final_byte)):
    code = int(final_byte[i], 2)
    print(code, end=" ")

  print("")
  
  for i in range(len(final_byte)):
    code = int(final_byte[i], 2)
    if code != 0:
      decrypted_code = alphabet[code - 1]
      print(Fore.GREEN + str(decrypted_code), end="")


def encrypt():
  #break the word in an array with each letters
  word = str(input(Fore.WHITE + "Enter word : ").lower())
  word = [*word]
  
  binary_list = []
  
  #each letter of the word has his position in the alphabet converted in binary
  for i in range(len(word)):
    binary = string.ascii_lowercase.index(word[i]) + 1
    #print(binary)
    print(f"{binary:#010b}"[2:])
    binary_list.append(f"{binary:#010b}"[2:])
  
  #print(binary_list)
  
  byte_index = 7
  new_byte = []
  final_byte = []
  
  #create new set of byte with the last bit of each byte, then the one before the last, and etc...
  for i in range(7):
    for i in range(len(binary_list)):
      bi = [*binary_list[i]]
      new_byte.append(bi[byte_index])
    #print("".join(new_byte))
    byte_index -= 1
    final_byte.append("".join(new_byte))
    new_byte.clear()
  
  #print(final_byte) #raw array of the answer in binary

  def sum(l):
    total = 0
    for val in l:
      total = total + int(val)
    return total
  
  #reconvert binary to numbers
  for i in range(len(final_byte)):
    #print(final_byte[len(final_byte) - 1 - i])
    if sum([*final_byte[len(final_byte) - 1 - i]]) != 0:
      code = int(final_byte[len(final_byte) - 1 - i], 2) #reverse the order of the answer
      print(Fore.GREEN + str(code), end=" ")
      

while True:

  print(Style.RESET_ALL)

  try:
    choice = int(input(Fore.BLUE + "Choose your action :\n1 - Encrypt\n2 - Decrypt\n> "))
  except:
    print(Fore.RED + "Invalid syntax, enter a number")
    choice = 0
  
  if choice == 1:
    try:
      encrypt()
    except Exception as e:
      print(Fore.RED + "An error has occured: " + str(e))

  elif choice == 2:
    try:
      decrypt()
    except Exception as e:
      print(Fore.RED + "An error has occured: " + str(e))

  elif choice != 0:
    print(Fore.RED + "Action not valid")