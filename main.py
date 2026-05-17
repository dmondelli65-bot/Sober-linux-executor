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
def esegui_script():
    print("Pulsante cliccato! L'IA collegherà questo tasto a Roblox nel prossimo passaggio.")

# Pulsante per eseguire lo script
pulsante_execute = tk.Button(finestra, text="EXECUTE", command=esegui_script, bg="#4CAF50", fg="white", font=("Arial", 10, "bold"), width=15)
pulsante_execute.pack(pady=10)

finestra.mainloop()
