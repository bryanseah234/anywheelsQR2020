# Anywheel QR Code Generator

A Python tool to generate QR codes for Anywheel bike-sharing rental bikes and parking locations in Singapore.

## Description

This project generates QR codes for the Anywheel bike-sharing service in Singapore. It creates QR codes for bike rental (to unlock and rent bicycles) and parking location codes (to properly park and end your rental). The tool batch-generates thousands of QR codes as PNG images for both bikes and locations.

## Features

- Generate QR codes for Anywheel rental bikes
- Generate QR codes for parking locations (AMK, BDK, BBT areas)
- Batch processing of thousands of codes
- High-quality PNG output with customizable scale

## Technologies Used

- Python
- pyqrcode - QR code generation library
- pypng - PNG image format support

## Installation

```bash
# Clone the repository
git clone https://github.com/bryanseah234/anywheelsQR2020.git

# Navigate to project directory
cd anywheelsQR2020

# Install dependencies
pip install pyqrcode pypng
```

## Usage

```bash
# Generate QR codes for bikes
python bikes.py

# Generate QR codes for parking locations
python locations.py
```

The generated QR codes will be saved in the `output/bikes/` and `output/locations/` directories respectively.

## Disclaimer

1. FOR EDUCATIONAL PURPOSES ONLY
2. USE AT YOUR OWN DISCRETION

## License

MIT License

---

**Author:** <a href="https://github.com/bryanseah234">bryanseah234</a>
