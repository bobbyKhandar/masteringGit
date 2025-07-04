image="image.png"
if(image.endswith('.png') or image.endswith('.jpg') or image.endswith('.jpeg')):
    print("Image file detected.")
else:
    print("Not an image file.")

if image.startswith('image'):
    print("Image file starts with 'image'.")
else:
    print("Image file does not start with 'image'.")

if image.endswith('.png'):
    print("Image file ends with '.png'.")