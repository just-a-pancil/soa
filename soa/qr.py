import qrcode
qr = qrcode.QRCode(
    error_correction=qrcode.constants.ERROR_CORRECT_H,
    box_size=10,
    border=1,)
token = '4xbOG0BYVgMuyUi9-hrDZ_PpBmauBSe0KSNKQpjF1nU'
qr.add_data("")
qr.make()
img=qr.make_image()
img.save("1qr.png")
