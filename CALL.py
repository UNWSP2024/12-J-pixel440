


import tkinter
from tkinter import messagebox

class ChargeCalculator:
    def __init__(self):
        self.main_window = tkinter.Tk()
        self.main_window.title("Call charge calculator")

        self.rate_frame = tkinter.LabelFrame(self.main_window, text="Select rate category")
        self.rate_frame.pack(padx=10, pady=10)

        self.rate_var = tkinter.StringVar()
        self.rate_var.set("day")

        tkinter.Radiobutton(self.rate_frame, text="Daytime (6 AM - 5:59 PM) - $0.02/min", variable=self.rate_var, value="day").pack(anchor="w")
        tkinter.Radiobutton(self.rate_frame, text="Evening (6 PM - 11:59 PM) - $0.12/min", variable=self.rate_var, value="evening").pack(anchor="w")
        tkinter.Radiobutton(self.rate_frame, text="Off-Peak (Midnight - 5:59 AM) - $0.05/min", variable=self.rate_var, value="offpeak").pack(anchor="w")

        self.input_frame = tkinter.Frame(self.main_window)
        self.input_frame.pack(pady=5)

        self.minutes_label = tkinter.Label(self.input_frame, text="Enter minutes:")
        self.minutes_label.pack(side="left")
        self.minutes_entry = tkinter.Entry(self.input_frame, width=10)
        self.minutes_entry.pack(side="left")

        self.button_frame = tkinter.Frame(self.main_window)
        self.button_frame.pack(pady=10)

        self.calc_button = tkinter.Button(self.button_frame, text="Calculate Charge", command=self.calculate_charge)
        self.quit_button = tkinter.Button(self.button_frame, text="Quit", command=self.main_window.destroy)
        self.calc_button.pack(side="left", padx=10)
        self.quit_button.pack(side="left")

        tkinter.mainloop()

    def calculate_charge(self):

        rate_map = {
            "day": 0.02,
            "evening": 0.12,
            "offpeak": 0.05
        }

        try:
            minutes = float(self.minutes_entry.get())
            if minutes < 0:
                raise ValueError("Minutes must be a positive number.")
            rate = rate_map[self.rate_var.get()]
            charge = minutes * rate
            messagebox.showinfo("Total charge", f"Call charge: ${charge:.2f}")
        except ValueError:
            messagebox.showerror("Invalid input", "Please try again.")

if __name__ == '__main__':
    ChargeCalculator()
