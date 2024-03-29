import qrcode
from PIL import Image

qr = qrcode.QRCode(version = 1,
                   box_size = 10,
                   border = 2)
qr.add_data('https://www.archermanfitness.uk')
qr_img = qr.make_image(back_color = 'white')

logo = Image.open('/Users/alyarees/Downloads/QR code/kisspng-computer-icons-weight-dumbbell-dumbbell-5abdb9c4c84851.4300711415223833008204.png').resize((75,75), Image.LANCZOS)
offset = ((qr_img.size[0] - 75) // 2, (qr_img.size[1] - 75) // 2)

qr_img.paste(logo, offset, mask = logo.split()[3] if logo.mode == 'RGBA' else None)
qr_img.save('qr_with_logo.png')