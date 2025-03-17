import tkinter as tk
from tkinter import ttk
from length_unit_conversions import LengthUnitConversions


class App(tk.Tk):

    def __init__(self):
        super().__init__()
        self.title("Unit Converter")
        # self.geometry("300x200")
        self.create_GUI()
        self.mainloop()

    def create_GUI(self):

        self.converter = LengthUnitConversions()
        self.units = self.converter.units()

        # Input section
        self.input_label = ttk.Label(self, text="Input:")
        self.input_label.pack(pady=5)

        self.from_unit_combobox = ttk.Combobox(self, values=self.units)
        self.from_unit_combobox.pack(pady=5)
        self.from_unit_combobox.current(0)

        self.input_value = tk.Entry(self)
        self.input_value.pack(pady=5)

        # Output section
        self.output_label = ttk.Label(self, text="Output:")
        self.output_label.pack(pady=5)

        self.to_unit_combobox = ttk.Combobox(self, values=self.units)
        self.to_unit_combobox.pack(pady=5)
        self.to_unit_combobox.current(0)

        self.output_value = tk.Entry(self)
        self.output_value.pack(pady=5)
        self.output_value.config(state="readonly")

        # Convert button
        self.convert_button = ttk.Button(
            self, text="Convert", command=self.convert_units
        )
        self.convert_button.pack(pady=10)

    def convert_units(self):
        try:
            value = float(self.input_value.get())
            from_unit = self.from_unit_combobox.get()
            to_unit = self.to_unit_combobox.get()
            converted_value = self.converter.convert(value, from_unit, to_unit)
            self.output_value.config(state="normal")
            self.output_value.delete(0, tk.END)
            self.output_value.insert(0, str(converted_value))
            self.output_value.config(state="readonly")
        except ValueError as ve:
            self.output_value.config(state="normal")
            self.output_value.delete(0, tk.END)
            self.output_value.insert(0, f"Error: {ve}")
            self.output_value.config(state="readonly")
        except TypeError as te:
            self.output_value.config(state="normal")
            self.output_value.delete(0, tk.END)
            self.output_value.insert(0, f"Error: {te}")
            self.output_value.config(state="readonly")


App()
