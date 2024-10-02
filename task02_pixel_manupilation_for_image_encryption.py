from PIL import Image

def encrypt_image(image_path,key):
   
 img = Image.open(image_path)
 pixels=img.load()
 width,hight=img.size
 for y in range(hight):
  for x in range(width):
    r,b,g=pixels[x,y]
    r=(r+key)%256
    b=(b+key)%256
    g=(g+key)%256
    pixels[x,y]=r,g,b
 img.save('encrypted_image.jpg')
 print("image encrypted and saved as encrypted_image.jpg")
def decypt_image(image_path,key):
 img = Image.open(image_path)
 pixels=img.load()
 width,hight=img.size
 for y in range(hight):
  for x in range(width):
   r,b,g=pixels[x,y]
   r=(r-key)%256
   b=(b-key)%256
   g=(g-key)%256
   pixels[x,y]=r,g,b
  img.save('decrypted_image.jpg')
  print("image decrypted and saved as decrypted_image.jpg")
   
image_path=("C:/Users/TARBIGO/Downloads/image.jpg")
key=46
encrypt_image(image_path,key)
decypt_image(image_path,key)





