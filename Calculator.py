import tkinter as tk  # Import the tkinter module for creating the GUI

# Basic arithmetic operations
def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        return "Cannot divide by zero!"
    return x / y

# Function to handle button clicks
def on_click(button_text):
    global display_var
    if button_text == "=":  # If "=" button is clicked, evaluate the expression and display the result
        try:
            result = eval(display_var.get())  # Evaluate the expression in the Entry widget
            display_var.set(result)  # Update the Entry widget with the result
        except Exception as e:
            display_var.set("Error")  # If an error occurs during evaluation, display "Error" in the Entry widget
    elif button_text == "C":  # If "C" button is clicked, clear the input
        display_var.set("")
    else:  # For other buttons, update the Entry widget with the clicked button's text
        display_var.set(display_var.get() + button_text)

# Function to create a button with the specified text
def create_button(frame, button_text):
    return tk.Button(frame, text=button_text, padx=20, pady=20, command=lambda: on_click(button_text))

# Function to create the calculator GUI
def create_calculator():
    global display_var
    root = tk.Tk()  # Create the main application window
    root.title("Calculator")  # Set the window title to "Calculator"

    display_var = tk.StringVar()  # Create a StringVar to hold the input and display in the Entry widget
    display_var.set("")  # Initialize the StringVar with an empty string

    display_frame = tk.Frame(root)  # Create a frame to hold the Entry widget
    display_frame.pack(padx=10, pady=10)  # Pack the frame with padding

    display = tk.Entry(display_frame, textvariable=display_var, font=('Helvetica', 20), justify='right')
    # Create the Entry widget to display the input and result with right justification
    display.pack(fill='both', expand=True)  # Pack the Entry widget to fill the available space

    button_frame = tk.Frame(root)  # Create a frame to hold the buttons
    button_frame.pack(padx=10, pady=10)  # Pack the frame with padding

    buttons = [
        '7', '8', '9', '/',  # List of button texts for the calculator
        '4', '5', '6', '*',
        '1', '2', '3', '-',
        '0', '.', '=', '+',
        'C'
    ]

    for i, button_text in enumerate(buttons):
        button = create_button(button_frame, button_text)  # Create a button with the specified text
        button.grid(row=i // 4, column=i % 4)  # Grid layout to arrange the buttons in rows and columns

    root.mainloop()  # Start the main event loop to display the GUI and handle user interactions

if __name__ == "__main__":
    create_calculator()  # Call the create_calculator function to run the GUI application
