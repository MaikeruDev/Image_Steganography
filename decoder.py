import numpy as np 
from PIL import Image 
import re

def main():
    print("Filename of stego image with extension:")
    filename = input()
    stego_image = Image.open(filename)
    stego_array = np.array(stego_image)

    def decode_lsb(stego_array):
        print("Decoding...") 
        stego_flat = stego_array.flatten()
         
        message_bits = [] # get lsb of every pixel
        for i in range(len(stego_flat)):
            message_bits.append(str(stego_flat[i] & 1)) 
         
        message = "" #binary to ascii
        for i in range(0, len(message_bits), 8):
            message += chr(int(''.join(message_bits[i:i+8]), 2)) 
        
        return message

    decoded = decode_lsb(stego_array)

    message = re.search('steg_start:(.*):steg_stop', decoded) 

    print("Decoded message: ", message.group(1))
 
if __name__ == "__main__":
    main()