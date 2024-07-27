from PIL import Image
import os

# Function to write text to framebuffer
def write_to_framebuffer(framebuffer='/dev/fb1', width=240, height=240, pixel_size=5, gap=2, padding=9, resolution=32):
    image = Image.open('./sad-pepe.png')
    image = image.convert('RGB')

    data = bytearray()

    for x in range(width):
        for y in range(height):
            # top/left/right/bottom padding
            if y <= padding or x <= padding or x > (width - padding) or y > (height - padding):
                data.append(0)
                data.append(0)
                continue

            x_in_px_gap_sequence = (x - padding) % (pixel_size + gap)
            y_in_px_gap_sequence = (y - padding) % (pixel_size + gap)
            if ((pixel_size + gap) - x_in_px_gap_sequence) < gap or ((pixel_size + gap) - y_in_px_gap_sequence) < gap:
                data.append(0)
                data.append(0)
                continue

            row = (y - padding) // (pixel_size + gap)
            col = (x - padding) // (pixel_size + gap)
            # value = 255 * pixel_array[col][row]
            # data.append(value)
            # data.append(value)

            r, g, b = image.getpixel((row, col))
            # convert RGB888 to RGB565
            rgb565 = ((r & 0xf8) << 8) | ((g & 0xfc) << 3) | (b >> 3)
            # screen expects bytes in little-endian order (low byte first)
            data.append(rgb565 & 0xff)        # low byte
            data.append((rgb565 >> 8) & 0xff) # high byte

    with open(framebuffer, 'wb') as f:
        f.write(data)

# write input to the framebuffer
write_to_framebuffer()
