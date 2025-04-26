


import tkinter

class JOESGUI:
    def __init__(self):
        self.main_window = tkinter.Tk()
        self.main_window.title("Joe's Automotive Services")

        self.services_frame = tkinter.Frame(self.main_window)
        self.services_frame.pack(padx=10, pady=10)

        # Dictionary of services and their prices
        self.services = {
            "Oil change": 30.0,
            "Lube job": 20.0,
            "Radiator flushj": 40.0,
            "Transmission fluid": 100.0,
            "Inspection": 35.0,
            "Muffler replacement": 200.0,
            "Tire rotation": 20.0
        }

        self.service_vars = {}
        for service in self.services:
            var = tkinter.IntVar()
            chk = tkinter.Checkbutton(self.services_frame,
                                      text=f"{service} - ${self.services[service]:.2f}",
                                      variable=var)
            chk.pack(anchor='w')
            self.service_vars[service] = var

        self.result_label = tkinter.Label(self.main_window, text="Total Charges:")
        self.result_label.pack(pady=5)
        self.total_var = tkinter.StringVar()
        self.total_display = tkinter.Label(self.main_window, textvariable=self.total_var)
        self.total_display.pack()

        self.calc_button = tkinter.Button(self.main_window, text="Calculate total", command=self.calculate_total)
        self.quit_button = tkinter.Button(self.main_window, text="Quit", command=self.main_window.destroy)
        self.calc_button.pack(pady=5)
        self.quit_button.pack(pady=5)

        tkinter.mainloop()

    def calculate_total(self):
        total = 0.0
        for service, var in self.service_vars.items():
            if var.get() == 1:
                total += self.services[service]
        self.total_var.set(f"${total:.2f}")

if __name__=="__main__":
    JOESGUI()
