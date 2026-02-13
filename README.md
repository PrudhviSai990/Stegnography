# Stegnography
# 🔒 Image Steganography with OpenCV

This project demonstrates a simple steganography technique using **Python** and **OpenCV**.  
It allows you to **hide a secret message inside an image** and later retrieve it using a passcode.

---

## 📌 Features
- Encrypts a text message into an image by modifying pixel values.
- Protects the hidden message with a passcode.
- Decrypts the message only if the correct passcode is provided.
- Uses OpenCV for image manipulation.

---

## 🛠️ Requirements
Make sure you have the following installed:
- Python 3.x
- OpenCV (`pip install opencv-python`)
- OS module (comes with Python)

---

## 🚀 How It Works
1. The program reads an image (`np.jpg` by default).
2. The user enters:
   - A secret message
   - A passcode
3. The message is encoded into the image by replacing pixel values.
4. The modified image is saved as `encryptedImage.jpg`.
5. For decryption:
   - The user enters the passcode.
   - If correct, the hidden message is retrieved and displayed.
   - If incorrect, access is denied.

---
