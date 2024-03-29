import segno

random_string = 'Hello world'

URL = segno.make('https://www.archermanfitness.uk')
URL.save('AMFQRCode.svg', border=5, scale=10)
URL.save('AMFQRCode.png', border=0, scale=10)