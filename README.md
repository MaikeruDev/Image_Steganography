# Image Steganography Project

This Python project provides a simple implementation of image steganography for hiding and extracting secret messages within images using the least significant bit (LSB) technique.

## Encoder

The `encoder.py` script allows you to embed a hidden message into a cover image. The script prompts for the filename of the cover image along with the message to be hidden. The message is converted to binary and encoded into the least significant bits of the cover image pixels. The encoded image (stego image) is saved with the filename `stego_cover_image`.

## Decoder

The `decoder.py` script is used to extract the hidden message from a stego image. It prompts for the filename of the stego image and then decodes the message using the LSB technique. The decoded message is printed on the screen.

## How to Use

1. Clone the repository: `git clone https://github.com/MaikeruDev/Image_Steganography.git`
2. Place your cover image in the project directory.
3. Encode a message in the cover image: Run `python encoder.py`.
4. Decode the hidden message from a stego image: Run `python decoder.py`.

**Note**: Make sure you have Python and the required dependencies (`numpy` and `PIL`) installed.
