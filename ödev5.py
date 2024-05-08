import tkinter as tk
from tkinter import messagebox, filedialog
import sqlite3
import hashlib
import os


conn = sqlite3.connect('users.db')
c = conn.cursor()


c.execute('''CREATE TABLE IF NOT EXISTS users
             (username TEXT PRIMARY KEY, password_hash TEXT)''')


def open_menu_window():
    menu_window = tk.Toplevel()
    menu_window.title("Menü")
    menu_window.geometry("400x300")

    frame = tk.Frame(menu_window)
    frame.pack(padx=10, pady=10)

    compare_button = tk.Button(frame, text="Karşılaştır", command=open_compare_window)
    compare_button.pack(side=tk.LEFT, padx=5)

    operations_button = tk.Button(frame, text="İşlemler", command=open_operations_menu)
    operations_button.pack(side=tk.LEFT, padx=5)

    exit_button = tk.Button(frame, text="Çıkış", command=menu_window.destroy)
    exit_button.pack(side=tk.LEFT, padx=5)


    menu_window.mainloop()



def create_database():
    conn = sqlite3.connect('metinler.db')
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS metinler
                 (id INTEGER PRIMARY KEY, metin TEXT)''')
    conn.commit()
    conn.close()


def metin_al(metin):
    conn = sqlite3.connect('metinler.db')
    c = conn.cursor()
    c.execute("INSERT INTO metinler (metin) VALUES (?)", (metin,))
    conn.commit()
    conn.close()


def open_compare_window():
    compare_window = tk.Toplevel()
    compare_window.title("Metin Karşılaştırma")
    compare_window.geometry("500x400")

    def algorithm1_compare(metin1,metin2): #karakter_benzerligi
        sayac = 0
        len_metin1 =len(metin1)
        len_metin2 =len(metin2)
        if len_metin1>len_metin2:
            for i in range(len_metin2):
                if metin1[i] == metin2[i]:
                    sayac +=1
            return sayac/len_metin2
        else:
            for i in range(len_metin1):
                if metin1[i] == metin2[i]:
                    sayac +=1
            return sayac/len_metin1

    def algorithm2_compare(metin1, metin2): #jaccard karşılaştırması
        kelime_set1 = set(metin1.split())
        kelime_set2 = set(metin2.split())
        kesisim = len(kelime_set1.intersection(kelime_set2))
        hesap = len(kelime_set1) + len(kelime_set2) - kesisim
        return kesisim / hesap


    def compare_texts(algorithm):
        text1 = text1_entry.get("1.0", tk.END)  # Metin girişi 1
        text2 = text2_entry.get("1.0", tk.END)  # Metin girişi 2
        result = ""
        if algorithm == "Algorithm1":
            result = algorithm1_compare(text1, text2)  # Karşılaştırma algoritması 1
        elif algorithm == "Algorithm2":
            result = algorithm2_compare(text1, text2)  # Karşılaştırma algoritması 2
        messagebox.showinfo("Karşılaştırma Sonucu", result)


    def select_algorithm():
        algorithm = algorithm_var.get()
        compare_texts(algorithm)


    text1_frame = tk.Frame(compare_window)
    text1_frame.pack(pady=5)
    text1_label = tk.Label(text1_frame, text="Metin 1:")
    text1_label.pack(side=tk.LEFT)
    text1_entry = tk.Text(text1_frame, height=5, width=50)
    text1_entry.pack(side=tk.LEFT, padx=5)


    text2_frame = tk.Frame(compare_window)
    text2_frame.pack(pady=5)
    text2_label = tk.Label(text2_frame, text="Metin 2:")
    text2_label.pack(side=tk.LEFT)
    text2_entry = tk.Text(text2_frame, height=5, width=50)
    text2_entry.pack(side=tk.LEFT, padx=5)


    algorithm_var = tk.StringVar(compare_window)
    algorithm_var.set("Algorithm1")  # Varsayılan algoritma
    algorithm_menu = tk.OptionMenu(compare_window, algorithm_var, "Algorithm1", "Algorithm2")
    algorithm_menu.pack(pady=10)


    compare_button = tk.Button(compare_window, text="Karşılaştır", command=select_algorithm)
    compare_button.pack(pady=10)

    compare_window.mainloop()


def open_operations_menu():
    operations_menu = tk.Toplevel()
    operations_menu.title("İşlemler")
    operations_menu.geometry("400x300")


    def open_password_submenu():
        password_submenu = tk.Toplevel()
        password_submenu.title("Şifre")
        password_submenu.geometry("400x300")


        def change_password():
            new_password = password_entry.get()
            if not new_password:
                messagebox.showerror("Hata", "Yeni şifre boş olamaz.")
                return
            update_password(new_password)
            messagebox.showinfo("Başarılı", "Şifre başarıyla güncellendi.")


        password_frame = tk.Frame(password_submenu)
        password_frame.pack(pady=5)
        password_label = tk.Label(password_frame, text="Yeni Şifre:")
        password_label.pack(side=tk.LEFT)
        password_entry = tk.Entry(password_frame, width=30, show="*")
        password_entry.pack(side=tk.LEFT, padx=5)


        change_button = tk.Button(password_submenu, text="Değiştir", command=change_password)
        change_button.pack(pady=10)

        password_submenu.mainloop()


    password_button = tk.Button(operations_menu, text="Şifre", command=open_password_submenu)
    password_button.pack(pady=10)


    operations_menu.mainloop()


def register_user():
    username = username_entry.get()
    password = password_entry.get()
    if not username or not password:
        messagebox.showerror("Hata", "Kullanıcı adı veya şifre boş olamaz.")
        return
    if check_existing_user(username):
        messagebox.showerror("Hata", "Bu kullanıcı zaten mevcut.")
        return
    add_user(username, password)
    messagebox.showinfo("Başarılı", "Kullanıcı başarıyla kaydedildi.")


def add_user(username, password):
    password_hash = hashlib.sha256(password.encode()).hexdigest()
    c.execute("INSERT INTO users (username, password_hash) VALUES (?, ?)", (username, password_hash))
    conn.commit()


def check_existing_user(username):
    c.execute("SELECT * FROM users WHERE username=?", (username,))
    result = c.fetchone()
    return result is not None


def login():
    username = username_entry.get()
    password = password_entry.get()
    if not username or not password:
        messagebox.showerror("Hata", "Kullanıcı adı veya şifre boş olamaz.")
        return
    if authenticate_user(username, password):
        open_menu_window()
        root.destroy()
    else:
        messagebox.showerror("Hata", "Kullanıcı adı veya şifre hatalı.")


def authenticate_user(username, password):
    password_hash = hashlib.sha256(password.encode()).hexdigest()
    c.execute("SELECT * FROM users WHERE username=? AND password_hash=?", (username, password_hash))
    result = c.fetchone()
    return result is not None


def update_password(new_password):
    username = username_entry.get()
    password_hash = hashlib.sha256(new_password.encode()).hexdigest()
    c.execute("UPDATE users SET password_hash=? WHERE username=?", (password_hash, username))
    conn.commit()


root = tk.Tk()
root.title("Kullanıcı Girişi")


username_label = tk.Label(root, text="Kullanıcı Adı:")
username_label.grid(row=0, column=0, padx=5, pady=5)
username_entry = tk.Entry(root)
username_entry.grid(row=0, column=1, padx=5, pady=5)

password_label = tk.Label(root, text="Parola:")
password_label.grid(row=1, column=0, padx=5, pady=5)
password_entry = tk.Entry(root, show="*")
password_entry.grid(row=1, column=1, padx=5, pady=5)


register_button = tk.Button(root, text="Kayıt Ol", command=register_user)
register_button.grid(row=2, column=0, columnspan=2, padx=5, pady=5, sticky="we")


login_button = tk.Button(root, text="Giriş Yap", command=login)
login_button.grid(row=3, column=0, columnspan=2, padx=5, pady=5, sticky="we")


root.mainloop()


conn.close()

