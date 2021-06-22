# import module
import pyqrcode
import sys
import png

# welcome message
print("Welcome to QR code generator")

# enter secret meassage
msg = input("Type your secret message: ")

code = pyqrcode.create(msg)

code.png("QRcode.png", scale=5)

print("Done successfully")