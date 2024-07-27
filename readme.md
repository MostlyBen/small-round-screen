# What is this?

I purchased a couple of small (maybe 1.3"), round screens on amazon.

The screens are GC9A01-based LCD displays.

I'm trying to get them to display content from the raspberry pi.

# Pinout Config
| LCD | GPIO         | Physical Pin |
| --- | ------------ | ------------ |
| Vin | 3.3V         | 1            |
| GND | GND          | 6            |
| SDA | 10 (MOSI)    | 19           |
| SCL | 11 (SCLK)    | 23           |
| CS  | 8 (CE0)      | 24           |
| DC  | 25           | 22           |
| RST | 27           | 13           |
| BL  | 18 (PCM_CLK) | 12           |


