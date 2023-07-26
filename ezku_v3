import sys
sys.set_int_max_str_digits(10000000)

def encrypt(input):
  input = [*input]

  binary_encoded = [[*bin(ord(chr))[2:].zfill(7)] for chr in input]
  
  encrypted = []
  for i in range(7):
      rearranged = [byte[i] for byte in binary_encoded]
      encrypted.append(int("".join(rearranged), 2))
  
  return " ".join(map(str, encrypted))


def decrypt(input):
  input = input.split(" ")

  binary_encoded = [[*bin(int(num))[2:]] for num in input]
  max_size = len(list(filter(lambda i: len(i) == max([len(l) for l in binary_encoded]), binary_encoded))[0])
  binary_encoded_zfill = [[*"".join(arr).zfill(max_size)] for arr in binary_encoded]
  
  decrypted = []
  for i in range(max_size):
      rearranged = [byte[i] for byte in binary_encoded_zfill]
      decrypted.append(chr(int("".join(rearranged), 2)))
      
  return "".join(decrypted)
