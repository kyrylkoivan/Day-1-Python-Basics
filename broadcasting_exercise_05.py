import numpy as np

# Generate random grayscale image (6x6)
image = np.random.randint(0, 256, (6, 6))

# Apply thresholding
binary_image = np.where(image > 128, 255, 0)

print("Binary Image:\n", binary_image)
