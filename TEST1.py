import qrcode
from PIL import Image

qr = qrcode.QRCode(version = 1,
                   box_size = 10,
                   border = 2)
qr.add_data('https://www.archermanfitness.uk')
qr.make(fit = True)
img = qr.make_image(fill = 'black', back_colour = 'white')
img.save('qrcode.png')