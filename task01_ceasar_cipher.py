def caesar_cipher(text,shift,encrypt=True):
    result = ""
    if not encrypt:
         shift = -shift   #in decryption reverse the shift
    for char in text:
        if char.isalpha():
            ascii_offset =65 if char.isupper() else 97
            result+= chr((ord(char)- ascii_offset + shift) % 26 + ascii_offset)
        else:
            result+=char #caesar_cipher doesnt modify other characters(.,_)
           
    return result 
 
text= input("enter your text to encrypt it or decrypt it:")
shift=int(input("enter the shift number:"))
encrypt=input("do yo want to encrypt or decrypt:").lower()=='encrypt'
output=caesar_cipher(text,shift,encrypt)
print(f"result is :{output}")