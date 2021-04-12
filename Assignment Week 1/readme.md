# Steps Followed

# 1.1.
Uploaded image to Colab, imported the libraries. Used cv2.cvtColor for grayscale and cv2.threshold for black and white

# 1.2. 
Used inbuilt code snippet, only photo taking was possible on Colab, video capture is easy on PC using cap = cv2.VideoCapture(0)

# 1.3.
Masked the red colors, changed pixels to blue and cv2_imshow(img) to show the edited image


# 2
4 translations, 4 rotations and 2 blurs using openCV functions

# 3
Convert the RGB color image to grayscale, use a bilateral filter and an adaptive threshold, merge them using bitwise_and

