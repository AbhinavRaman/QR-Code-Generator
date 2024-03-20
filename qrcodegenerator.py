import qrcode
import image

qr = qrcode.QRCode(
    version = 15, #15 means the version of QR Code. Higher the number bigger will be the code image and complicated picture.
    box_size = 10, # Size of the box where qr code will be displayed
    border = 5 # it is the white part of the image -- border in all 4 sides with white color
)

data = "https://github.com/AbhinavRaman"
# Now this is the path of my github page

qr.add_data(data)
qr.make(fit = True)
img = qr.make_image(fill="black", background_color = "white")
img.save("test.png")