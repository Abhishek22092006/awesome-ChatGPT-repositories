from PIL import Image

# Open the image
image = Image.open("your_image.jpg")

# Rotate the image (e.g., 90 degrees)
rotated_image = image.rotate(90)

# Save the rotated image
rotated_image.save("rotated_image.jpg")

# Or show the rotated image
rotated_image.show()
