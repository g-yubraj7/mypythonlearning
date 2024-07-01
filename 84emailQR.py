import qrcode

email_address = input("Please enter the email address: ")
email_subject = input("Please enter the subject for the email: ")
email_body = input("Please enter the message for the email: ")
mail = f"mailto:{email_address}?subject={email_subject}&body={email_body}"
img = qrcode.make(mail)
type(img)  # qrcode.image.pil.PilImage
img.save("QRmail.png")
print("QR code for this email has been generated please find it.")