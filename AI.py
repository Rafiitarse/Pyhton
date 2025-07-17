import tkinter as tk

def proses_input():
    user_input = entry.get().lower()
    chat_log.insert(tk.END, f"Kamu: {user_input}\n")
    entry.delete(0, tk.END)

    # Logika respon
    if "tambah" in user_input or "kali" in user_input or "kurang" in user_input or "bagi" in user_input:
        try:
            user_input = user_input.replace("tambah", "+")
            user_input = user_input.replace("kurang", "-")
            user_input = user_input.replace("kali", "*")
            user_input = user_input.replace("bagi", "/")
            hasil = eval(user_input)
            response = f"Hasilnya adalah {hasil}"
        except:
            response = "Maaf saya tidak mengerti maksud anda"
    elif "halo" in user_input:
        response = "Halo juga bro! Saya siap membantu!"
    elif "nama lu?" in user_input:
        response = "Nama saya Friday!"
    elif "siapa yang buat" in user_input or "Lu siapa yang buat?" in user_input:
        response = "saya dibuat oleh Lintar Ar' Rafii!"
    elif "keluar" in user_input:
        response = "Sampai jumpa!"
        root.quit()
    else:
        response = "Maaf saya belum mengerti apa maksud anda"

    chat_log.insert(tk.END, f"AI: {response}\n")

# Setup GUI
root = tk.Tk()
root.title("Lintar AI Chat")

chat_log = tk.Text(root, height=20, width=50)
chat_log.pack()

entry = tk.Entry(root, width=40)
entry.pack(side=tk.LEFT, padx=(10,0))

kirim_btn = tk.Button(root, text="Kirim", command=proses_input)
kirim_btn.pack(side=tk.LEFT)

root.mainloop()
