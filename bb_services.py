class BBInvoice:

    def __init__(self):
        self.services = {
            "Hagyományos manikűr": 3000,
            "Japán manikűr": 3500,
            "Orosz manikűr (gépi)": 3500,
            "Alkalmi gél lakk (töltése 2 hetente javasolt)": 5000,
            "Erősített gél lakk (XS)": 6300,
            "Erősített gél lakk (S)": 6500,
            "Műköröm építés (S méret)": 8000,
            "Műköröm építés (M méret)": 9000,
            "Műköröm építés (L méret)": 10000,
            "Műköröm építés (XL méret)": 11000,
            "Műköröm töltés (S méret)": 7500,
            "Műköröm töltés (M méret)": 8500,
            "Műköröm töltés (L méret)": 9500,
            "Műköröm töltés (XL méret)": 10000,
            "Eltávolítás + manikűr gél lakk": 3000,
            "Eltávolítás + manikűr műköröm": 3500,
            "Műköröm pótlása": 1000
        }
        self.per_nail_services = {
            "Kézzel festett minta": 200,
            "Teli köves köröm (S méret)": 600,
            "Teli köves köröm (M méret)": 700,
            "Teli köves köröm (L méret)": 900,
            "Kővariációk (kő + kaviár)": 300,
            "Kövek, formakövek, körömékszerek": 500,
            "Csillámok, porok, nyomda": 50,
            "Festett francia / babyboomer": 80,
            "Reszelt mosolyvonalas francia": 300,
        }
        self.chosen_services = []
        self.total_price = 0

    def add_service(self, name, price, quantity=1):
        total_cost = price * quantity
        self.chosen_services.append((name, total_cost))
        self.total_price += total_cost

    def generate_invoice(self):
        invoice = "Számla:\n"
        invoice += "=" * 30 + "\n"
        for name, cost in self.chosen_services:
            invoice += f"{name}: {cost} Ft\n"
        invoice += "=" * 30 + "\n"
        invoice += f"Végösszeg: {self.total_price} Ft\n"
        return invoice

    def save_invoice(self, filename="szamla.txt"):
        with open(filename, "w", encoding="utf-8") as file:
            file.write(self.generate_invoice())
