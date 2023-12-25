import tkinter as tk

def on_button_click():
    input_text = entry.get()
    result_label.config(text=f"You entered: {input_text}")

# Create the main window
root = tk.Tk()
root.title("Noor's form")

# Create and place widgets (labels, entry, button)
label = tk.Label(root, text="Enter Text:")
label.pack(pady=10)

entry = tk.Entry(root)
entry.pack(pady=10)

button = tk.Button(root, text="Submit", command=on_button_click)
button.pack(pady=10)

result_label = tk.Label(root, text="")
result_label.pack(pady=10)

# Start the GUI event loop
root.mainloop()
