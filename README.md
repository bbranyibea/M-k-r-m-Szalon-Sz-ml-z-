A feladat rövid leírás:
Egy müköröm szalon számlázó kalkulátorát készítettem el, melyben ki lehet választani az adott szolgáltatásokat, majd azt egy külön txt fájlban lementi.

Függvények a Kódból
main.py
run_app()
add_service_to_invoice(service, cost, qty)
remove_last_service()
update_invoice_display()
save_invoice()
bb_services.py
__init__()
add_service(name, price, quantity=1)
generate_invoice()
save_invoice(filename="szamla.txt")

Modulok a Kódból
Beépített Modulok
os
tkinter
tkinter.messagebox
datetime
Egyedi Modulok
bb_services
