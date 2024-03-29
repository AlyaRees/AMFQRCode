import segno

QRCode = segno.make('https://www.archermanfitness.uk')

QRCode.save('TESTQRCode.png', scale=7)