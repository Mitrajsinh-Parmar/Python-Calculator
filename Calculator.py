import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

# Function to perform calculations in the basic calculator
def calculate():
    try:
        expression = entry.get()
        result = eval(expression)
        entry.delete(0, tk.END)
        entry.insert(tk.END, str(result))
    except Exception as e:
        messagebox.showerror("Error", "Invalid Expression")

# Function to clear the calculator input field
def clear_entry():
    entry.delete(0, tk.END)

# Function to open the unit converter window
def open_unit_converter():
    unit_converter_window = tk.Toplevel(root)
    unit_converter_window.title("Unit Converter")

    # Function to perform unit conversion
    def convert_units():
        try:
            value = float(entry_value.get())
            from_unit = combo_from.get()
            to_unit = combo_to.get()

            # Unit conversion logic for each type
            conversion_rates = {
                'Distance': {'km': 1000, 'm': 1, 'cm': 100, 'mm': 1000, 'mile': 0.621371, 'yard': 1.09361, 'inch': 39.3701},
                'Mass': {'kg': 1, 'g': 1000, 'mg': 1000000, 'ton': 0.001, 'lb': 2.20462, 'oz': 35.274},
                'Area': {'sq_m': 1, 'sq_km': 1e-6, 'sq_cm': 10000, 'sq_mm': 1000000, 'acre': 0.000247105, 'hectare': 1e-4, 'sq_inch': 1550.0031},
                'Speed': {'m/s': 1, 'km/h': 3.6, 'mph': 2.23694, 'ft/s': 3.28084, 'kn': 1.94384},  # kn = knot
                'Volume': {'m^3': 1, 'l': 1000, 'ml': 1000000, 'cup': 4226.75, 'gal': 264.172, 'qt': 1056.69, 'pt': 2113.38, 'oz': 33814},
                'Data': {'MB': 1, 'KB': 1024, 'GB': 0.001, 'TB': 1e-6, 'PB': 1e-9, 'Byte': 1024, 'KB': 1024},
            }

            # Get selected category
            category = category_combo.get()
            conversion_dict = conversion_rates[category]

            # Convert value
            converted_value = value * conversion_dict[to_unit] / conversion_dict[from_unit]
            label_result.config(text=f"Converted Value: {converted_value:.6f}")
        except Exception as e:
            messagebox.showerror("Error", "Invalid input")

    # Category selection
    label_category = tk.Label(unit_converter_window, text="Select Category:")
    label_category.grid(row=0, column=0, padx=10, pady=5)

    category_combo = ttk.Combobox(unit_converter_window, values=["Distance", "Mass", "Area", "Speed", "Volume", "Data"])
    category_combo.set("Distance")
    category_combo.grid(row=0, column=1, padx=10, pady=5)

    # Entry for value to be converted
    label_value = tk.Label(unit_converter_window, text="Enter Value:")
    label_value.grid(row=1, column=0, padx=10, pady=5)

    entry_value = tk.Entry(unit_converter_window)
    entry_value.grid(row=1, column=1, padx=10, pady=5)

    # Unit From and Unit To selection
    label_from = tk.Label(unit_converter_window, text="From Unit:")
    label_from.grid(row=2, column=0, padx=10, pady=5)

    combo_from = ttk.Combobox(unit_converter_window)
    combo_from.grid(row=2, column=1, padx=10, pady=5)

    label_to = tk.Label(unit_converter_window, text="To Unit:")
    label_to.grid(row=3, column=0, padx=10, pady=5)

    combo_to = ttk.Combobox(unit_converter_window)
    combo_to.grid(row=3, column=1, padx=10, pady=5)

    def update_units(*args):
        category = category_combo.get()
        units = {
            'Distance': ['km', 'm', 'cm', 'mm', 'mile', 'yard', 'inch'],
            'Mass': ['kg', 'g', 'mg', 'ton', 'lb', 'oz'],
            'Area': ['sq_m', 'sq_km', 'sq_cm', 'sq_mm', 'acre', 'hectare', 'sq_inch'],
            'Speed': ['m/s', 'km/h', 'mph', 'ft/s', 'kn'],
            'Volume': ['m^3', 'l', 'ml', 'cup', 'gal', 'qt', 'pt', 'oz'],
            'Data': ['MB', 'KB', 'GB', 'TB', 'PB', 'Byte'],
        }
        unit_list = units[category]
        combo_from['values'] = unit_list
        combo_to['values'] = unit_list
        combo_from.set(unit_list[0])
        combo_to.set(unit_list[0])

    category_combo.bind("<<ComboboxSelected>>", update_units)
    update_units()

    # Convert Button
    button_convert = tk.Button(unit_converter_window, text="Convert", command=convert_units)
    button_convert.grid(row=4, column=0, columnspan=2, pady=10)

    # Label for displaying converted result
    label_result = tk.Label(unit_converter_window, text="Converted Value: ")
    label_result.grid(row=5, column=0, columnspan=2, pady=10)

# Function to open the interest converter window
def open_interest_converter():
    interest_converter_window = tk.Toplevel(root)
    interest_converter_window.title("Interest Calculator")

    # Function to calculate compound interest
    def calculate_interest():
        try:
            principal = float(entry_principal.get())
            rate = float(entry_rate.get())
            time = float(entry_time.get())
            frequency = int(entry_frequency.get())

            # Compound Interest Formula
            amount = principal * (1 + rate / (100 * frequency)) ** (frequency * time)
            interest = amount - principal
            label_result_interest.config(text=f"Compound Interest: {interest:.2f}\nTotal Amount: {amount:.2f}")
        except Exception as e:
            messagebox.showerror("Error", "Invalid input")

    # Input fields for compound interest
    label_principal = tk.Label(interest_converter_window, text="Principal Amount:")
    label_principal.grid(row=0, column=0, padx=10, pady=5)

    entry_principal = tk.Entry(interest_converter_window)
    entry_principal.grid(row=0, column=1, padx=10, pady=5)

    label_rate = tk.Label(interest_converter_window, text="Rate of Interest (%):")
    label_rate.grid(row=1, column=0, padx=10, pady=5)

    entry_rate = tk.Entry(interest_converter_window)
    entry_rate.grid(row=1, column=1, padx=10, pady=5)

    label_time = tk.Label(interest_converter_window, text="Time Period (years):")
    label_time.grid(row=2, column=0, padx=10, pady=5)

    entry_time = tk.Entry(interest_converter_window)
    entry_time.grid(row=2, column=1, padx=10, pady=5)

    label_frequency = tk.Label(interest_converter_window, text="Frequency per year:")
    label_frequency.grid(row=3, column=0, padx=10, pady=5)

    entry_frequency = tk.Entry(interest_converter_window)
    entry_frequency.grid(row=3, column=1, padx=10, pady=5)

    # Button to calculate compound interest
    button_calculate_interest = tk.Button(interest_converter_window, text="Calculate", command=calculate_interest)
    button_calculate_interest.grid(row=4, column=0, columnspan=2, pady=10)

    # Label for displaying result
    label_result_interest = tk.Label(interest_converter_window, text="Compound Interest: \nTotal Amount: ")
    label_result_interest.grid(row=5, column=0, columnspan=2, pady=10)

# Toggle dark/light mode function
def toggle_dark_mode():
    global dark_mode
    if dark_mode:
        # Light mode
        root.config(bg="white")
        entry.config(bg="white", fg="black")
        for button in buttons:
            button.config(bg="lightgray", fg="black")
        dark_mode = False
    else:
        # Dark mode
        root.config(bg="black")
        entry.config(bg="black", fg="white")
        for button in buttons:
            button.config(bg="gray", fg="white")
        dark_mode = True

# Creating the main window
root = tk.Tk()
root.title("Basic Calculator with Unit & Interest Converter")

# Dark mode flag
dark_mode = False

# Creating a Menu bar
menu = tk.Menu(root)
root.config(menu=menu)

file_menu = tk.Menu(menu, tearoff=0)
menu.add_cascade(label="File", menu=file_menu)
file_menu.add_command(label="Unit Converter", command=open_unit_converter)
file_menu.add_command(label="Interest Converter", command=open_interest_converter)
file_menu.add_separator()
file_menu.add_command(label="Toggle Dark/Light Mode", command=toggle_dark_mode)
file_menu.add_separator()
file_menu.add_command(label="Exit", command=root.quit)

# Basic Calculator Section
entry = tk.Entry(root, width=20, font=("Arial", 14), borderwidth=2, relief="solid", justify="right")
entry.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

# Button Layout for Calculator
buttons = []

# Button creation
for (text, row, col) in [
    ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
    ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
    ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
    ('0', 4, 0), ('.', 4, 1), ('=', 4, 2), ('+', 4, 3),
    ('C', 5, 0),  # Clear button
]:
    if text == 'C':
        button = tk.Button(root, text=text, width=5, height=2, font=("Arial", 14),
                           command=clear_entry)
    else:
        button = tk.Button(root, text=text, width=5, height=2, font=("Arial", 14),
                           command=lambda t=text: entry.insert(tk.END, t) if t != "=" else calculate())
    button.grid(row=row, column=col, padx=5, pady=5)
    buttons.append(button)  # Add the button widget to the list

# Run the main loop
root.mainloop()
