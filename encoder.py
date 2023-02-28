import numpy as np 
from PIL import Image

def main():
    print("Filename of cover image with extension:")
    filename = input()
    cover_image = Image.open(filename)
    cover_array = np.array(cover_image)

    print("Hidden Message:")
    message = input()

    detectors = "steg_start:" + message + ":steg_stop"

    binary_message = ''.join(format(ord(i), '08b') for i in detectors) 

    max_bits = cover_array.shape[0] * cover_array.shape[1] * 3 // 8

    if len(binary_message) > max_bits:
        print("Message is too large to be hidden in the cover image.")
        return

    def encode_lsb(cover_array, message): 
        cover_flat = cover_array.flatten()
         
        for i in range(len(message)): #modify lsb of cover pixel to the message
            cover_flat[i*8] = (cover_flat[i*8] & 254) | int(message[i][0])
            cover_flat[i*8+1] = (cover_flat[i*8+1] & 254) | int(message[i][1])
            cover_flat[i*8+2] = (cover_flat[i*8+2] & 254) | int(message[i][2])
            cover_flat[i*8+3] = (cover_flat[i*8+3] & 254) | int(message[i][3])
            cover_flat[i*8+4] = (cover_flat[i*8+4] & 254) | int(message[i][4])
            cover_flat[i*8+5] = (cover_flat[i*8+5] & 254) | int(message[i][5])
            cover_flat[i*8+6] = (cover_flat[i*8+6] & 254) | int(message[i][6])
            cover_flat[i*8+7] = (cover_flat[i*8+7] & 254) | int(message[i][7])
        
        stego_array = np.reshape(cover_flat, cover_array.shape) 
        stego_image = Image.fromarray(stego_array)
        return stego_image

    stego_image = encode_lsb(cover_array, [binary_message[i:i+8] for i in range(0, len(binary_message), 8)])

    stego_image.save("stego_" + filename)
    print("Image created with filename: stego_" + filename)

if __name__ == "__main__":
    main()