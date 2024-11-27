import tkinter as tk

class LoanReceipt:
    def __init__(self, client_name, credit_analyst, loan_number, capital, interest_rate, last_payment, next_payment, capital_balance):
        self.client_name = client_name
        self.credit_analyst = credit_analyst
        self.loan_number = loan_number
        self.capital = capital
        self.interest_rate = interest_rate
        self.last_payment = last_payment
        self.next_payment = next_payment
        self.capital_balance = capital_balance
        self.itf_rate = 0.005 / 100  # ITF rate of 0.005%
    
    def calculate_interest(self):
        return self.capital * self.interest_rate
    
    def calculate_itf(self):
        return self.capital * self.itf_rate
    
    def total_charge(self):
        interest = self.calculate_interest()
        itf = self.calculate_itf()
        return self.capital + interest + itf
    
    def display_receipt(self):
        interest = self.calculate_interest()
        itf = self.calculate_itf()
        total_charge = self.total_charge()
        
        receipt_text = (
            "                 MI BANCO                 \n"
            "         COBRO DE PRÉSTAMO - CAJA         \n"
            f"Fecha y Hora: {self.last_payment}\n"
            f"Cliente: {self.client_name}\n"
            f"Anal. Crédito: {self.credit_analyst}\n"
            f"Nro Préstamo: {self.loan_number}\n"
            f"Capital: S/ {self.capital:.2f}\n"
            f"Interés Compensatorio: S/ {interest:.2f}\n"
            f"ITF (0.005%): S/ {itf:.2f}\n"
            "----------------------------------------\n"
            f"Total Cobro: S/ {total_charge:.2f}\n"
            "Total Pagado:\n"
            "Son: Ciento ochenta y cuatro con 20/100 Soles\n"
            "----------------------------------------\n"
            f"Última Cuota Pagada: 11\n"
            f"Próximo Pago: {self.next_payment}\n"
            f"Saldo de Capital: S/ {self.capital_balance:.2f}\n"
            "Los montos pendientes de pago no incluyen cargos ni moras.\n"
            "Evite recargos pagando su cuota completa puntualmente.\n"
            "El presente no es válido para crédito fiscal."
        )
        return receipt_text

# Función para mostrar el recibo en una ventana de tkinter
def show_receipt():
    client_name = entry_client_name.get()
    
    # Crear una instancia de LoanReceipt con el nombre del cliente ingresado
    receipt = LoanReceipt(
        client_name=client_name,
        credit_analyst="DEIVID DAVID IMAN BRUNO",
        loan_number=126877877,
        capital=133.34,
        interest_rate=0.3821,  # Tasa de interés para dar un monto cercano a S/ 50.86
        last_payment="11/11/2024 09:30:29",
        next_payment="10/12/2024",
        capital_balance=1113.24
    )
    
    # Obtener el texto del recibo y mostrarlo en la ventana de recibo
    receipt_text = receipt.display_receipt()
    receipt_window = tk.Toplevel(root)
    receipt_window.title("Recibo de Préstamo")
    receipt_label = tk.Label(receipt_window, text=receipt_text, justify="left", font=("Courier", 10))
    receipt_label.pack(padx=10, pady=10)

# Configuración de la ventana principal de tkinter
root = tk.Tk()
root.title("Generador de Recibo de Préstamo")

# Etiqueta y entrada para el nombre del cliente
label_client_name = tk.Label(root, text="Ingrese el nombre del cliente:")
label_client_name.pack(pady=5)
entry_client_name = tk.Entry(root)
entry_client_name.pack(pady=5)

# Botón para generar el recibo
generate_button = tk.Button(root, text="Generar Recibo", command=show_receipt)
generate_button.pack(pady=10)

# Ejecutar la ventana principal
root.mainloop()
