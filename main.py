from PIL import Image

img = Image.open("input.jpg")
resized_img = img.resize((1400, 560))
resized_img.save("output_image.jpeg")