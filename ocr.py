from Crypto.Cipher import AES
from Crypto.Util.Padding import pad
from Crypto.Random import get_random_bytes
import cv2
import pytesseract
import base64
import numpy as np

# OCR function to extract text
def ocr_core(img):
    return pytesseract.image_to_string(img)

# AES-256 encryption
def encrypt_text(text, key):
    cipher = AES.new(key, AES.MODE_CBC)
    iv = cipher.iv  # Initialization vector
    ciphertext = cipher.encrypt(pad(text.encode(), AES.block_size))
    return base64.b64encode(iv + ciphertext).decode()  # Combine IV and ciphertext

# Embed encrypted text into the image
def embed_text_in_image(image, encrypted_text):
    # Convert encrypted text to binary
    binary_text = ''.join(format(ord(c), '08b') for c in encrypted_text)
    flat_image = image.flatten()

    # Ensure there are enough pixels to embed the binary text
    if len(binary_text) > len(flat_image):
        raise ValueError("The image is too small to embed the encrypted text.")
    
    for i in range(len(binary_text)):
        # Get the pixel value
        pixel_value = flat_image[i]
        
        # Modify the least significant bit to store the binary data
        new_pixel_value = (pixel_value & ~1) | int(binary_text[i])
        
        # Ensure the pixel value is within the valid range (0-255)
        new_pixel_value = np.clip(new_pixel_value, 0, 255)
        
        # Update the pixel value
        flat_image[i] = new_pixel_value
    
    return flat_image.reshape(image.shape)

# Read and preprocess the image
image_path = "plain_nid.png"
img = cv2.imread(image_path)
grayscale_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Extract the ID number
extracted_text = ocr_core(grayscale_img)
print(f"Extracted Text: {extracted_text}")

# Get the ID number (assuming it's the last number in the text)
id_number = extracted_text.split()[-1]
print(f"ID Number: {id_number}")

# Encrypt the ID number
key = get_random_bytes(32)  # 32 bytes for AES-256
encrypted_id = encrypt_text(id_number, key)
print(f"Encrypted ID: {encrypted_id}")

# Embed the encrypted ID into the image
# stego_image = embed_text_in_image(img, encrypted_id)

# Display the encrypted image
# cv2.imshow("Encrypted Image", stego_image)
# cv2.waitKey(0)
# cv2.destroyAllWindows()

# Save the output image
# output_path = "encrypted_image.png"
# cv2.imwrite(output_path, stego_image)
# print(f"Encrypted image saved at {output_path}")

