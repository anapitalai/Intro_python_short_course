##pip install opencv-python

import cv2

# Load an image from a file
image = cv2.imread('sample.jpg')

# Check if the image was loaded successfully
if image is not None:
    # Display the image in a window
    cv2.imshow('My Image', image)

    # Wait for a key press and then close the image window
    cv2.waitKey(0)
    cv2.destroyAllWindows()
else:
    print("Image not found or could not be loaded.")
