import tkinter as tk

# Crea la finestra principale dell'executor
finestra = tk.Tk()
finestra.title("Sober Linux Executor - Interfaccia")
finestra.geometry("500x350")
finestra.configure(bg="#2e2e2e")

# Titolo della finestra
titolo = tk.Label(finestra, text="Sober Executor", fg="white", bg="#2e2e2e", font=("Arial", 16, "bold"))
titolo.pack(pady=10)

# Spazio di testo dove si scriveranno gli script Lua
spazio_testo = tk.Text(finestra, width=55, height=12, bg="#1e1e1e", fg="lightgreen", insertbackground="white")
spazio_testo.pack(pady=5)

# Funzione temporanea del pulsante
# Funzione che salva lo script in un file di testo
def esegui_script():
    codice = spazio_testo.get("1.0", tk.END)
    # Crea o sovrascrive il file script.txt
    with open("script.txt", "w") as file:
        file.write(codice)
    print("[IA] Script salvato in script.txt! Pronto per essere letto.")
    
# Pulsante per eseguire lo script
pulsante_execute = tk.Button(finestra, text="EXECUTE", command=esegui_script, bg="#4CAF50", fg="white", font=("Arial", 10, "bold"), width=15)
pulsante_execute.pack(pady=10)

finestra.mainloop()
