import qrcode

# Data to be stored in QR Code
data = input("Enter text or URL: ")

# Create QR Code
qr = qrcode.QRCode(
    version=1,
    box_size=10,
    border=5
)

qr.add_data(data)
qr.make(fit=True)

# Generate image
img = qr.make_image(fill_color="black", back_color="white")

# Save image
img.save("qrcode.png")

print("QR Code generated successfully as 'qrcode.png'")