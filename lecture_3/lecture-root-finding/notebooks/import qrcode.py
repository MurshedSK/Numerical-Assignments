import qrcode

def generate_qr(text, filename):
    img = qrcode.make(text)
    img.save(f"{filename}.png")

generate_qr('https://freedium.cfd/https://blog.stackademic.com/20-python-scripts-that-will-give-you-superpowers-4c6f4b15fe63', 'my_qr_code')