from colorama import Fore, Back, Style
import string
import math

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