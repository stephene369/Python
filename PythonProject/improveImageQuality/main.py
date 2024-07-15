# Import the Images module from pillow
from PIL import Image

# Open the image by specifying the image path.
image_path = "monCv.png"
image_file = Image.open(image_path)

# the default
image_file.save("image_name.png", quality=500)

# Changing the image resolution using quality parameter
# Example-1
image_file.save("image_name2.png", quality=100)

# Example-2
image_file.save("image_name3.png", quality=20)
