import qrcode

# Taking UPI Id as a input

upiId = input("Enter your UPI ID = ")

# FORMAT OF UPI
# upi://pay?pa=upiId&apn=NAME&am=AMOUNT&cu=CUREENCY&tn=MESSAGE


phonepe_url = f'upi://pay?pa={upiId}&pn=Recipient%20Name'
paytm_url = f'upi://pay?pa={upiId}&pn=Recipient%20Name'
google_url = f'upi://pay?pa={upiId}&pn=Recipient%20Name'

# create QR code for each payment app
phonepeQR = qrcode.make(phonepe_url)
paytmQR = qrcode.make(paytm_url)
googleQR = qrcode.make(google_url)

# save the QR code in image file
phonepeQR.save('phonepeQR.png')
paytmQR.save('paytmQR.png')
googleQR.save('googleQR.png')

# display the qr code
phonepeQR.show()
paytmQR.show()
googleQR.show()
