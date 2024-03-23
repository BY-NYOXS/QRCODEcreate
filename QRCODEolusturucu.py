import tkinter as tk
import qrcode


arayuz = tk.Tk()
arayuz.title("qrcode")
arayuz.geometry("350x200")

url=tk.Label(text="QRCODE URL:")
url.place(x=15, y=15)

y = tk.StringVar()
url_grs=tk.Entry(textvariable=y)
url_grs.place(x=98, y=15)

#dosya yolu 
yol=tk.Label(text="DOSYA İSMİ:")
yol.place(x=15, y=40)

x = tk.StringVar()
yol_grs=tk.Entry(textvariable=x)
yol_grs.place(x=98, y=40)

#button
def olusturma():
    import qrcode
    
    qrsave=x.get()
    urlQR=y.get()
    qrURL25= qrcode.make(urlQR)
    qrURL25.save(qrsave)


ols=tk.Button(text="OLUSTUR",command=olusturma)
ols.place(x=250, y=20)

acıklama = tk.Label(text="QR kodlarını kullanarak iletişim\nbilgilerini paylaşmak artık çok kolay!\nQR kodu oluşturucu uygulamamızla, bir URL veya\nmetin girin, dosya adını\nseçin ve QR kodunu oluşturun.\nHemen deneyin ve bilgilerinizi\npaylaşmayı daha hızlı hale getirin!")
acıklama.place(x=30, y=70)

developer = tk.Label(text="BY NYOXS")
developer.place(x=280, y=170)

arayuz.mainloop()

