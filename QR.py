import qrcode as qr


website_url = input("Enter your URL : ")


img = qr.make(website_url)
img.save("yuvi_linkedin.png")

print("Your QR code is generated and saved in  yuvi_linkedin.png ")

