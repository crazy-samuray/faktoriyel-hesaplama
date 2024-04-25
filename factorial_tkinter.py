import tkinter as tk

# Factorial calculation function
def factorial(num):
    if num == 0:
        return 1
    else:
        return num * factorial(num - 1)

# When the Calculate button is clicked
def calculate_factorial():
    try:
        num = int(entry.get())
        result = factorial(num)
        result_label.config(text=f"{num}! = {result}")
    except ValueError:
        result_label.config(text="Please enter a valid number.")

# Main Tkinter window
root = tk.Tk()
root.title("Factorial Calculator")

# Calculate the center position of the screen
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
window_width = 300
window_height = 200
x = (screen_width - window_width) // 2
y = (screen_height - window_height) // 2
root.geometry(f"{window_width}x{window_height}+{x}+{y}")

# Entry box for user input
entry_label = tk.Label(root, text="Enter a number:")
entry_label.pack()
entry = tk.Entry(root)
entry.pack()

# Calculate button
calculate_button = tk.Button(root, text="Calculate Factorial", command=calculate_factorial)
calculate_button.pack()

# Result label
result_label = tk.Label(root, text="")
result_label.pack()

# Open the window
root.mainloop()