from tkinter import *
from tkinter import ttk
import tkinter.messagebox


def convert_amount(event=None):
    try:
        amount = float(ent_amount.get())
        from_currency = combo_from.get()
        to_currency = combo_to.get()
        exchange_rate = valuta[from_currency][to_currency]
        converted_amount = amount * exchange_rate
        lab_res['text'] = f'{amount} {from_currency} = {converted_amount} {to_currency}'
    except:
        tkinter.messagebox.showerror('Error', 'Введіть суму')


valuta = {
    'UAH': {'EUR': 0.024, 'GBP': 0.02, 'JPY': 3.85, 'UAH': 1},
    'EUR': {'UAH': 41.8, 'GBP': 0.73, 'JPY': 109.43, 'EUR': 1},
    'GBP': {'UAH': 49.12, 'EUR': 1.36, 'JPY': 134.23, 'GBP': 1},
    'JPY': {'UAH': 0.26, 'EUR': 0.0086, 'GBP': 0.0074, 'JPY': 1},
}

root = Tk()
root.title("Currency Exchange")

lab_amount = ttk.Label(root, text="Сума:")
lab_amount.grid(row=0, column=0)
ent_amount = ttk.Entry(root, width=10)
ent_amount.grid(row=0, column=1, padx=5, pady=5)
ent_amount.bind("<Return>", convert_amount)

lab_from = ttk.Label(root, text="З:")
lab_from.grid(row=1, column=0, padx=5, pady=5)
combo_from = ttk.Combobox(root, values=list(valuta.keys()))
combo_from.grid(row=1, column=1, padx=5, pady=5)
combo_from.current(0)

# Create the to_currency combobox
lab_to = ttk.Label(root, text="На:")
lab_to.grid(row=2, column=0, padx=5, pady=5)
combo_to = ttk.Combobox(root, values=list(valuta.keys()))
combo_to.grid(row=2, column=1, padx=5, pady=5)
combo_to.current(0)

btn = ttk.Button(root, text='Конвертувати', command=convert_amount)
btn.grid(row=3, column=0, columnspan=2, padx=5, pady=5)

lab_res = ttk.Label(root)
lab_res.grid(row=4, column=0, columnspan=2, padx=5, pady=5)

root.mainloop()