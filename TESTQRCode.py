import segno

AMFQRCode = 'https://www.archermanfitness.uk'

QRCode = segno.make(AMFQRCode, error='h')

QRCode.save('AMFQRCode.png', 
            border = 2, 
            scale = 10,
            finder_dark = "darkorange"
            )