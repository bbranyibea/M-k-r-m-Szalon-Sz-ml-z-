import os
import tkinter as tk
from bb_services import BBInvoice
from tkinter import messagebox
from datetime import datetime

def run_app():
    root = tk.Tk()
    root.title("Műköröm Szalon Számlázó")
    root.geometry("800x600")

    invoice = BBInvoice()
    save_count = 1

    save_folder = r"C:\Users\MGH5DS\OneDrive - Dunaújvárosi Egyetem\Asztal\Szkript nylevek beadandó\Számlák"

    if not os.path.exists(save_folder):
        os.makedirs(save_folder)

    def add_service_to_invoice(service, cost, qty):
        invoice.add_service(service, cost, qty)
        update_invoice_display()

    def remove_last_service():
        if invoice.chosen_services:
            removed_item = invoice.chosen_services.pop()
            invoice.total_price -= removed_item[1]
            update_invoice_display()
            messagebox.showinfo("Törlés", f"A következő elem eltávolítva: {removed_item[0]} - {removed_item[1]} Ft")
        else:
            messagebox.showwarning("Hiba", "Nincs eltávolítható elem!")

    def update_invoice_display():
        invoice_text.set(invoice.generate_invoice())

    def save_invoice():
        nonlocal save_count
        current_time = datetime.now().strftime("%Y%m%d_%H%M")
        file_name = f"{save_count}_{current_time}_szamla.txt"
        file_path = os.path.join(save_folder, file_name)
        try:
            invoice.save_invoice(file_path)
            save_count += 1
            messagebox.showinfo("Mentés", f"A számla sikeresen elmentve ide: {file_path}")
        except Exception as e:
            messagebox.showerror("Mentési hiba", f"Nem sikerült menteni a fájlt: {e}")

    main_frame = tk.Frame(root)
    main_frame.pack(fill="both", expand=True)

    canvas = tk.Canvas(main_frame)
    scrollbar = tk.Scrollbar(main_frame, orient="vertical", command=canvas.yview)
    scrollable_frame = tk.Frame(canvas)

    scrollable_frame.bind(
        "<Configure>",
        lambda e: canvas.configure(scrollregion=canvas.bbox("all"))
    )

    canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")
    canvas.configure(yscrollcommand=scrollbar.set)

    canvas.pack(side="left", fill="both", expand=True)
    scrollbar.pack(side="right", fill="y")

    invoice_text = tk.StringVar()
    invoice_display = tk.Label(scrollable_frame, textvariable=invoice_text, justify="left", anchor="nw")
    invoice_display.grid(row=0, column=0, columnspan=2, pady=10)

    row = 1
    for service_name, price in invoice.services.items():
        frame = tk.Frame(scrollable_frame)
        frame.grid(row=row, column=0, sticky="w", padx=10, pady=5)
        tk.Label(frame, text=f"{service_name} - {price} Ft").pack(side="left")
        tk.Button(
            frame,
            text="Hozzáad",
            command=lambda s=service_name, p=price: add_service_to_invoice(s, p, 1)
        ).pack(side="right")
        row += 1

    row = 1
    for nail_service_name, nail_service_price in invoice.per_nail_services.items():
        frame = tk.Frame(scrollable_frame)
        frame.grid(row=row, column=1, sticky="w", padx=10, pady=5)
        tk.Label(frame, text=f"{nail_service_name} - {nail_service_price} Ft/köröm").pack(side="left")
        entry = tk.Entry(frame, width=5)
        entry.pack(side="left", padx=5)
        tk.Button(
            frame,
            text="Hozzáad",
            command=lambda s=nail_service_name, p=nail_service_price, e=entry: add_service_to_invoice(
                s, p, int(e.get()) if e.get().isdigit() else 1
            )
        ).pack(side="right")
        row += 1

    row += 1
    button_frame = tk.Frame(scrollable_frame)
    button_frame.grid(row=row, column=0, columnspan=2, pady=20)

    save_button = tk.Button(button_frame, text="Számla mentése", command=save_invoice)
    save_button.pack(side="left", padx=20)

    remove_button = tk.Button(button_frame, text="Utolsó elem törlése", command=remove_last_service)
    remove_button.pack(side="right", padx=20)

    update_invoice_display()

    root.mainloop()

if __name__ == "__main__":
    run_app()
