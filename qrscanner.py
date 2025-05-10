import qrcode
from pyzbar.pyzbar import decode
from PIL import Image

# Generate QR code
qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_L,
    box_size=10,
    border=4,
)
qr.add_data('https://www.youtube.com/watch?v=PyDn2gU9DJo')
qr.make(fit=True)

img = qr.make_image(fill_color="black", back_color="white")
img.save('myqr.png')

# Read QR code
decoded_qr = decode(Image.open('myqr.png'))
print(decoded_qr[0].data.decode('ascii'))