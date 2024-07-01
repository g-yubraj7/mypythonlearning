import qrcode
img = qrcode.make('Yubraj Ghimire')
type(img)  # qrcode.image.pil.PilImage
img.save("Yubraj.png")