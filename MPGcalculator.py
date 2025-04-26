


import tkinter

class MPGCalculator:
    def __init__(self):
        self.main_window = tkinter.Tk()  # Corrected this line
        self.main_window.title("MPG Calculator")

        # Frames
        self.gas_frame = tkinter.Frame(self.main_window)
        self.miles_frame = tkinter.Frame(self.main_window)
        self.mpg_frame = tkinter.Frame(self.main_window)
        self.button_frame = tkinter.Frame(self.main_window)

        # Gas input
        self.gas_label = tkinter.Label(self.gas_frame, text='Enter range in miles with a full tank:')
        self.gas_entry = tkinter.Entry(self.gas_frame, width=10)
        self.gas_label.pack(side='left')
        self.gas_entry.pack(side='left')

        # Miles input
        self.miles_label = tkinter.Label(self.miles_frame, text='Enter gallons in a full tank:')
        self.miles_entry = tkinter.Entry(self.miles_frame, width=10)
        self.miles_label.pack(side='left')
        self.miles_entry.pack(side='left')

        # MPG display
        self.result_label = tkinter.Label(self.mpg_frame, text='MPG:')
        self.mpg = tkinter.StringVar()
        self.mpg_label = tkinter.Label(self.mpg_frame, textvariable=self.mpg)
        self.result_label.pack(side='left')
        self.mpg_label.pack(side='left')

        # Buttons
        self.calc_button = tkinter.Button(self.button_frame, text='Calculate MPG', command=self.calculate_mpg)
        self.quit_button = tkinter.Button(self.button_frame, text='Quit', command=self.main_window.destroy)
        self.calc_button.pack(side='left')
        self.quit_button.pack(side='left')

        # Pack frames
        self.gas_frame.pack()
        self.miles_frame.pack()
        self.mpg_frame.pack()
        self.button_frame.pack()

        # Start the main loop
        tkinter.mainloop()

    def calculate_mpg(self):
        try:
            miles = float(self.gas_entry.get())
            gallons = float(self.miles_entry.get())

            if gallons == 0:
                self.mpg.set("Zero is not a valid input")
            else:
                mpg = miles / gallons
                self.mpg.set(f"{mpg:.2f}")
        except ValueError:
            self.mpg.set("Invalid input, please enter numbers")


if __name__ == '__main__':
    MPGCalculator()












