import tkinter as tk
import qrcode


arayuz = tk.Tk()
arayuz.title("qrcode")
arayuz.geometry("400x200")

url=tk.Label(text="QRCODE URL:")
url.place(x=5, y=15)

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
    qrsave=x.get()
    urlQR=y.get()
    qrURL25= qrcode.make(urlQR)
    qrURL25.save(qrsave)


ols=tk.Button(text="OLUSTUR",command=olusturma)
ols.place(x=270, y=20)

developer = tk.Label(text="BY NYOXS")
developer.place(x=320, y=170)

arayuz.mainloop()

