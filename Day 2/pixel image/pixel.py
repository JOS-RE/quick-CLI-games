# Import Libraries
from PIL import Image
import matplotlib.pyplot as plt

# Read image
img = Image.open('mario.jpg')
# show image
plt.imshow(img)
plt.show()

small_img = img.resize((8, 8), Image.BILINEAR)

# resize
o_size = (1000, 1000)  # output size
res = small_img.resize(o_size, Image.NEAREST)
# save image
res.save('mario_8x8.png')
# display image
plt.imshow(res)
plt.show()


def photo2pixelart(image, i_size, o_size):
    """
    image: path to image file
    i_size: size of the small image eg:(8,8)
    o_size: output size eg:(10000,10000)
    """
    # read file
    img = Image.open(image)

    # convert to small image
    small_img = img.resize(i_size, Image.BILINEAR)

    # resize to output size
    res = small_img.resize(img.size, Image.NEAREST)

    # Save output image
    filename = f'mario_{i_size[0]}x{i_size[1]}.png'
    res.save(filename)

    # Display images side by side
    plt.figure(figsize=(16, 10))
    # original image
    plt.subplot(1, 2, 1)
    plt.title('Original image', size=18)
    plt.imshow(img)  # display image
    plt.axis('off')  # hide axis
    # pixel art
    plt.subplot(1, 2, 2)
    plt.title(f'Pixel Art {i_size[0]}x{i_size[1]}', size=18)
    plt.imshow(res)
    plt.axis('off')
    plt.show()


photo2pixelart(image='mario.jpg', i_size=(32, 32),
               o_size=img.size)

# Function Call
photo2pixelart(image='mario.jpg', i_size=(80, 80),
               o_size=img.size)
