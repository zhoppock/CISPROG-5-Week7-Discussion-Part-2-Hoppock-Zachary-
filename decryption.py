def decryption(code):
  print("\nYour encrypted text is:", code)
  encryptedText = code
  distance = 4
  text = ""
  for ch in encryptedText:
    ordvalue = ord(ch)
    cipherValue = ordvalue - distance
    if cipherValue < ord('!'):
      cipherValue = ord('~') - (distance - abs(ord('!') - ordvalue - 1))
    text += chr(cipherValue)
  print("The decrypted text is:", text)
  return text