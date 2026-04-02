import tkinter

def miles_to_kms():
    try:
        km = float(miles_input.get()) * 1.609
        kilometer_label.config(text=f"{km}")
    except ValueError:
        kilometer_label.config(text="Please enter a valid number")



window = tkinter.Tk()
window.title("Miles to Kilometer convertor")
window.config(padx=50, pady=50)


miles_input = tkinter.Entry(width=7)
miles_input.grid(column=1, row=0)

miles_label = tkinter.Label(text="Miles")
miles_label.config(padx=10, pady=10)
miles_label.grid(column=2, row=0)

is_equal_label = tkinter.Label(text="is equal to")
is_equal_label.config(padx=10, pady=10)
is_equal_label.grid(row=1, column=0)

kilometer_label = tkinter.Label(text="0")
kilometer_label.config(padx=10, pady=10)
kilometer_label.grid(row=1, column=1)

km_label = tkinter.Label(text="Km")
km_label.config(padx=10, pady=10)
km_label.grid(row=1, column=2)

calculate = tkinter.Button(text="Calculate",command=miles_to_kms)
calculate.config(padx=10, pady=10)
calculate.grid(row=2, column=1)





















window.mainloop()