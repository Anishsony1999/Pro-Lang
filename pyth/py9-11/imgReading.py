

path = "C:/Users/HP/OneDrive/Desktop/Lang/img/2.jpeg"


with open(path,'rb') as img:
    image = img.read()
    
with open("new_img.png",'wb') as img:
    img.write(image)