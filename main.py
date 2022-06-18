from decryption import decryption
import os

fileName = input("Please input an encrypted filename: ")

while True:
  if os.path.exists(fileName):
    break
  else:
    fileName = input("Please input a valid encrypted filename: ")

f = open(fileName,"r")
code = f.read()
plaintext = decryption(code)

print("\nYour plaintext is:\n", plaintext)
