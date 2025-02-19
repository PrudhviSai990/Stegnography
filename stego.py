import cv2
import os

# Read the image
img = cv2.imread("np.jpg") # Replace with the correct image path
height, width, _ = img.shape

msg = input("Enter secret message:")
password = input("Enter a passcode:")

d = {}
c = {}

for i in range(255):
    d[chr(i)] = i
    c[i] = chr(i)

row = 0
col = 0
z = 0

for i in range(len(msg)):
    if row < height and col < width:
        img[row, col, z] = d[msg[i]]
        col += 1
        if col == width:
            col = 0
            row += 1
        z = (z + 1) % 3

cv2.imwrite("encryptedImage.jpg", img)
os.system("start encryptedImage.jpg")  # Use 'start' to open the image on Windows

message = ""
row = 0
col = 0
z = 0

pas = input("Enter passcode for Decryption")
if password == pas:
    for i in range(len(msg)):
        if row < height and col < width:
            message = message + c[img[row, col, z]]
            col += 1
            if col == width:
                col = 0
                row += 1
            z = (z + 1) % 3
    print("Decryption message:", message)
else:
    print("YOU ARE NOT auth")
