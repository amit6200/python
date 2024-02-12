import qrcode as qr
img=qr.make("https://www.youtube.com/watch?v=OKuiyX5k6zg&t=971s")
img.save("wscube_youtube.png")
# img=qr.make("Amit singh")
# img.save("amit.png")