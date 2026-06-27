import qrcode

id_billets = "VAS_001"
url = f"https://bal-de-promo-back-end.onrender.com/billets/{id_billets}"
qr = qrcode.make(url)

qr.save(f'{id_billets}.png')
