from PIL import Image, ImageDraw, ImageFont
import os

# Function to write text to framebuffer
def write_to_framebuffer(text, framebuffer='/dev/fb1', width=240, height=240, padding=40):
    # Create a blank image with a white background
    image = Image.new('RGB', (width, height), 'black')
    draw = ImageDraw.Draw(image)

    # Load the default font
    font_path = "/usr/share/fonts/truetype/msttcorefonts/Arial.ttf"

    font = ImageFont.truetype(font_path, 1)

    # Find the maximum font size that fits the text within the screen
    font_size = 1
    while True:
        text_bbox = draw.textbbox((0, 0), text, font=font)
        text_width = draw.textlength(text, font=font)
        text_height = font_size
        if text_width + 2*padding > width or text_height + 2*padding > height:
            font = ImageFont.truetype(font_path, font_size - 1)
            text_width = draw.textlength(text, font=font)
            text_height = font_size
            break
        font_size += 1
        font = ImageFont.truetype(font_path, font_size)

    # Calculate text size and position
    text_x = (width - text_width) // 2
    text_y = (height - text_height) // 2

    # Draw the text onto the image
    draw.text((text_x, text_y), text, fill='white', font=font)

    # Convert the image to RGB565 format (16-bit)
    image = image.convert('RGB')
    data = bytearray()
    for y in range(height):
        for x in range(width):
            r, g, b = image.getpixel((x, y))
            rgb565 = ((r & 0xf8) << 8) | ((g & 0xfc) << 3) | (b >> 3)
            data.append((rgb565 >> 8) & 0xff)
            data.append(rgb565 & 0xff)

    with open(framebuffer, 'wb') as f:
        f.write(data)

# Get user input
user_text = input("Enter text to display:")

# Write input to the framebuffer
write_to_framebuffer(user_text)
