import tkinter as tk
from tkinter import messagebox

import webbrowser
webbrowser.open("https://www.youtube.com/watch?v=dQw4w9WgXcQ")

def hesapla():
    try:
        x = float(giris1.get())
        y = float(giris2.get())
        islem = islem_giris.get()

        if islem == "+":
            sonuc = x + y
        elif islem == "-":
            sonuc = x - y
        elif islem == "*":
            sonuc = x * y
        elif islem == "/":
            if y == 0:
                messagebox.showerror("Hata", "Sıfıra bölme yapılamaz!")
                return
            sonuc = x / y
        else:
            messagebox.showerror("Hata", "Geçersiz işlem!")
            return

        sonuc_etiket.config(text=f"Sonuç: {sonuc}")
    except ValueError:
        messagebox.showerror("Hata", "Lütfen geçerli sayılar giriniz!")

pencere = tk.Tk()
pencere.title("Basit Hesap Makinesi")

tk.Label(pencere, text="İlk Sayı:").pack()
giris1 = tk.Entry(pencere)
giris1.pack()

tk.Label(pencere, text="İkinci Sayı:").pack()
giris2 = tk.Entry(pencere)
giris2.pack()

tk.Label(pencere, text="İşlem (+, -, *, /):").pack()
islem_giris = tk.Entry(pencere)
islem_giris.pack()

tk.Button(pencere, text="Hesapla", command=hesapla).pack()
sonuc_etiket = tk.Label(pencere, text="Sonuç: ")
sonuc_etiket.pack()

pencere.mainloop()

webbrowser.open("https://www.youtube.com/watch?v=dQw4w9WgXcQ")
