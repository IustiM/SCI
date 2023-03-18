import qrcode

data = "Bun venit! Accesati urmatorul link: localgost:8000/pagina1/homepage"
qr = qrcode.QRCode(version=1, box_size=50, border=1)
qr.add_data(data)
qr.make(fit=True)
img = qr.make_image(fill_color="black", back_color="white")
img.save("QR_universal.png")
