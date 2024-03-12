from sense_emu import SenseHat
import tkinter as tk


hat = SenseHat()
hat.clear()

main_window = tk.Tk()
main_window.title('Python RPi Meteo')
main_window.geometry('600x400')

lbl_temperature_title = tk.Label(main_window,
                                text='Temperatura u C')
lbl_temperature_title.grid(row=0, column=0, padx=15, pady=15)

lbl_temperature_var = tk.StringVar()
lbl_temperature_var.set(str(round(hat.get_temperature(), 1)))
lbl_temperature = tk.Label(main_window,
                            textvariable=lbl_temperature_var)
lbl_temperature.grid(row=0, column=1, padx=15, pady=15)

main_window.mainloop()
