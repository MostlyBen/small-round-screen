from PIL import Image
import sys
import os

# Function to write text to framebuffer
def write_to_framebuffer(framebuffer='/dev/fb1', width=240, height=240, gap=2, resolution=32, padding_fill=0, file_path="./sad-pepe.png"):
    # determine variables
    pixel_size = (width // resolution) - gap

    padding = width - ((width // resolution) * resolution)
    padding = -(padding // -2) + 1

    image = Image.open(file_path)
    image = image.convert('RGB')

    # initialize bytarray
    data = bytearray()

    for x in range(width):
        for y in range(height):
            
            # gap
            x_in_px_gap_sequence = (x - padding) % (pixel_size + gap)
            y_in_px_gap_sequence = (y - padding) % (pixel_size + gap)
            if ((pixel_size + gap) - x_in_px_gap_sequence) < gap or ((pixel_size + gap) - y_in_px_gap_sequence) < gap:
                data.append(0)
                data.append(0)
                continue

            # top/left/right/bottom padding
            if y <= padding or x <= padding or x > (width - padding) or y > (height - padding):
                data.append(padding_fill)
                data.append(padding_fill)
                continue

            # get location
            row = (y - padding) // (pixel_size + gap)
            col = (x - padding) // (pixel_size + gap)

            # get pixel & convert to 16 bit
            r, g, b = image.getpixel((row, col))
            rgb565 = ((r & 0xf8) << 8) | ((g & 0xfc) << 3) | (b >> 3)

            # write to bytearray 
            data.append(rgb565 & 0xff)        # low byte
            data.append((rgb565 >> 8) & 0xff) # high byte

    # Write to framebuffer
    with open(framebuffer, 'wb') as f:
        f.write(data)

# write image to the framebuffer
if __name__ == "__main__":
    # get arguments 
    args = {} 
    if "-gap" in sys.argv:
        gap = sys.argv[sys.argv.index("-gap") + 1]
        args['gap'] = int(gap)
    if "-padding_fill" in sys.argv:
        if sys.argv[sys.argv.index("-padding_fill") + 1] == "white":
            args['padding_fill'] = 255
    if "-file" in sys.argv:
        args['file_path'] = sys.argv[sys.argv.index("-file") + 1]
    if "-framebuffer" in sys.argv:
        args['framebuffer'] = sys.argv[sys.argv.index("-framebuffer") + 1]
     
    write_to_framebuffer(**args)

