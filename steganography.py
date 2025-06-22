import cv2
import numpy as np
from PIL import Image

def encode_image(image_path, secret_message, output_path):
    image = cv2.imread(image_path)
    if image is None:
        raise ValueError("Image not found or path is incorrect")

    message = secret_message + '#####'  # end marker
    binary_msg = ''.join([format(ord(i), '08b') for i in message])
    data_index = 0

    rows, cols, _ = image.shape

    for row in range(rows):
        for col in range(cols):
            pixel = image[row, col]
            for channel in range(3):
                if data_index < len(binary_msg):
                    pixel[channel] = (pixel[channel] & ~1) | int(binary_msg[data_index])
                    data_index += 1
                else:
                    break

    cv2.imwrite(output_path, image)
    print("✅ Message encoded and saved to", output_path)

def decode_image(encoded_image_path):
    image = cv2.imread(encoded_image_path)
    if image is None:
        raise ValueError("Image not found or path is incorrect")

    binary_data = ""
    for row in image:
        for pixel in row:
            for channel in range(3):
                binary_data += str(pixel[channel] & 1)

    all_bytes = [binary_data[i:i+8] for i in range(0, len(binary_data), 8)]
    decoded_msg = ""
    for byte in all_bytes:
        decoded_msg += chr(int(byte, 2))
        if decoded_msg[-5:] == "#####":
            break

    return decoded_msg[:-5]

if __name__ == "__main__":
    print("=== Steganography: Hide Message in Image ===")
    choice = input("Enter E to encode or D to decode: ").upper()

    if choice == "E":
        image_path = input("Enter input image path (e.g., input_image.png): ")
        message = input("Enter your secret message: ")
        output_path = input("Enter output image path (e.g., output_image.png): ")
        encode_image(image_path, message, output_path)

    elif choice == "D":
        encoded_path = input("Enter image path to decode (e.g., output_image.png): ")
        message = decode_image(encoded_path)
        print("🔓 Hidden Message:", message)

    else:
        print("❌ Invalid option")
