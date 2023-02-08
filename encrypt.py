import string
from colorama import Fore, Back, Style

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