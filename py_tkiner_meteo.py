import tkinter as tk
from sense_emu import SenseHat


hat = SenseHat()

class MeteoApp():
    def __init__(self, master):
        self.master = master
        self.master.title('Python METEO')
        self.master.geometry('600x400')
        

        self.lbl_temperature_label = tk.Label(self.master,
                            text='Temperatura zraka',
                            font=('Segoe UI', 15))
        self.lbl_temperature_label.grid(row=0, column=0, padx=15, pady=20, sticky='e')
        self.lbl_temperature_var = tk.StringVar()
        self.lbl_temperature = tk.Label(self.master,
                            textvariable=self.lbl_temperature_var,
                            font=('Segoe UI', 15))
        self.lbl_temperature.grid(row=0, column=1, padx=15, pady=20, sticky='e')


        self.lbl_humidity_label = tk.Label(self.master,
                        text='Vlaznost zraka',
                        font=('Segoe UI', 15))
        self.lbl_humidity_label.grid(row=1, column=0, padx=15, pady=20, sticky='e')
        self.lbl_humidity_var = tk.StringVar()
        self.lbl_humidity = tk.Label(self.master,
                        textvariable=self.lbl_humidity_var,
                        font=('Segoe UI', 15))
        self.lbl_humidity.grid(row=1, column=1, padx=15, pady=20, sticky='e')


        self.lbl_pressure_label = tk.Label(self.master,
                        text='Tlak zraka',
                        font=('Segoe UI', 15))
        self.lbl_pressure_label.grid(row=2, column=0, padx=15, pady=20, sticky='e')
        self.lbl_pressure_var = tk.StringVar()
        self.lbl_pressure = tk.Label(self.master,
                        textvariable=self.lbl_pressure_var,
                        font=('Segoe UI', 15))
        self.lbl_pressure.grid(row=2, column=1, padx=15, pady=20, sticky='e')

        self.update_values()


    def update_values(self):
        if self.lbl_temperature_var.get() != '':
            temperature = float(self.lbl_temperature_var.get())
        else:
            temperature = 0.0
        current_temperature = round(hat.get_temperature(), 2)
        temp_diff = current_temperature - temperature
        if temp_diff >= 1:
            self.lbl_temperature_var.set(f'{str(round(hat.get_temperature(), 2))} \u2103')
        elif temp_diff <= -1:
            self.lbl_temperature_var.set(f'{str(round(hat.get_temperature(), 2))} \u2103')
   
        if self.lbl_humidity_var.get() != '':
            humidity = float(self.lbl_humidity_var.get())
        else:
            humidity = 0.0
        current_humidity = round(hat.get_humidity(), 2)
        humidity_diff = current_humidity - humidity
        if humidity_diff >= 1:
            self.lbl_humidity_var.set(f'{str(round(hat.get_humidity(), 2))} %')
        elif humidity_diff <= -1:
            self.lbl_humidity_var.set(f'{str(round(hat.get_humidity(), 2))} %')


        if self.lbl_pressure_var.get() != '':
            pressure = float(self.lbl_pressure_var.get())
        else:
            pressure = 260.0
        current_pressure = round(hat.get_pressure(), 2)
        pressure_diff = current_pressure - pressure
        if pressure_diff >= 1:
            self.lbl_pressure_var.set(f'{str(round(hat.get_pressure(), 2))} hPa')
        elif pressure_diff <= -1:
            self.lbl_pressure_var.set(f'{str(round(hat.get_pressure(), 2))} hPa')


        self.master.after(2000, self.update_values)




if __name__ == '__main__':
    window = tk.Tk()
    app = MeteoApp(window)
    window.mainloop()
