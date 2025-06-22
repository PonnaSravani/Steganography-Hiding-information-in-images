# Steganography: Hiding Information in Images

This project provides a Python script to hide (encode) secret messages inside images and to extract (decode) them. The technique works by modifying the least significant bits (LSBs) of image pixels, making the embedded data imperceptible to the human eye.

## Features

- **Encode** a secret message into an image file.
- **Decode** and reveal a hidden message from an image.
- Simple command-line interface.
- Uses OpenCV and Pillow for image processing.

## Requirements

- Python 3.x
- [opencv-python](https://pypi.org/project/opencv-python/)
- [numpy](https://pypi.org/project/numpy/)
- [Pillow](https://pypi.org/project/Pillow/)

Install dependencies with:

```bash
pip install opencv-python numpy Pillow
```

## Usage

Run the script from the command line:

```bash
python steganography.py
```

You’ll be prompted to choose encode (`E`) or decode (`D`):

### Encode a Message

1. Enter `E` at the prompt.
2. Provide the path to your input image (e.g., `input_image.png`).
3. Type your secret message.
4. Specify the output image path (e.g., `output_image.png`).

The script will save the image with your hidden message.

### Decode a Message

1. Enter `D` at the prompt.
2. Provide the path to the encoded image.
3. The script will reveal the hidden message.

## How It Works

- **Encoding:**  
  Converts your message to binary and embeds each bit into the LSB of each color channel (R, G, B) of the image pixels. An end marker (`#####`) signifies the end of the hidden message.
- **Decoding:**  
  Reads the LSBs from each pixel, reconstructs the binary data, and converts it back to readable text until the end marker is found.

## Example

```text
=== Steganography: Hide Message in Image ===
Enter E to encode or D to decode: E
Enter input image path (e.g., input_image.png): mypic.png
Enter your secret message: hello!
Enter output image path (e.g., output_image.png): hidden.png
✅ Message encoded and saved to hidden.png
```

To decode:

```text
=== Steganography: Hide Message in Image ===
Enter E to encode or D to decode: D
Enter image path to decode (e.g., output_image.png): hidden.png
🔓 Hidden Message: hello!
```
