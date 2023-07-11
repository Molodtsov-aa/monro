from PIL import Image

image = Image.open('Molodtsov.jpg')
rotated_image = image.rotate(45)
rotated_image.save("rotated.jpg")

rotated_image = Image.open("lenna.jpg")

cmyk_image = rotated_image.convert("RGB")

image_monro = Image.open('monro.jpg')
red, green, blue = image_monro.split()
red.save('red.jpg')
green.save('green.jpg')
blue.save('blue.jpg')

new_monro = Image.merge("RGB", (red, green, blue))
new_monro.save('new_monro.jpg')

monro_left = Image.open("red.jpg")
coordinates = ((100, 0, 696, 522))
cropped_left = monro_left.crop(coordinates)
cropped_left.save('cropped_left.jpg')

monro_two = Image.open("red.jpg")
coordinates = ((50, 0, 646, 522))
cropp_right = monro_two.crop(coordinates)
cropp_right.save('cropp_right.jpg')

image1 = Image.open("cropped_left.jpg")
image2 = Image.open("cropp_right.jpg")
image_sm = Image.blend(image1, image2, 0.5)
image_sm.save('image_sm.jpg')


monro_left_blue = Image.open("blue.jpg")
coordinates = ((0, 0, 596, 522))
cropped_left_blue = monro_left_blue.crop(coordinates)
cropped_left_blue.save('cropped_left_blue.jpg')


monro_two_blue = Image.open("blue.jpg")
coordinates = ((50, 0, 646, 522))
cropp_right_blue = monro_two_blue.crop(coordinates)
cropp_right_blue.save('cropp_right_blue.jpg')


image11 = Image.open("cropped_left_blue.jpg")
image22 = Image.open("cropp_right_blue.jpg")
image_sm_blue = Image.blend(image11, image22, 0.5)
image_sm_blue.save('image_sm_blue.jpg')

monro_two_green = Image.open("green.jpg")
coordinates = ((50, 0, 646, 522))
cropp_two_green = monro_two_green.crop(coordinates)
cropp_two_green.save('cropp_two_green.jpg')


final_monro = Image.merge("RGB", (image_sm, image_sm_blue, cropp_two_green))
final_monro.save('final_monro.jpg')

mini_monro = Image.open("final_monro.jpg")
mini_monro.thumbnail((80, 80))
mini_monro.save('mini_monro.jpg')
print(mini_monro.size)