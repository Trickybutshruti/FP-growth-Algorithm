import tkinter as tk
from tkinter import scrolledtext
import pyfpgrowth

# Function to run FP-Growth and display results
def run_fpgrowth():
    min_support = float(min_support_entry.get())
    transactions = [[item for item in line.strip().split(',') if item != ''] for line in transactions_entry.get("1.0", tk.END).split('\n') if line.strip()]
    patterns = pyfpgrowth.find_frequent_patterns(transactions, min_support)
    sorted_patterns = sorted(patterns.items(), key=lambda x: x[1], reverse=True)
    
    output_text.delete("1.0", tk.END)  # Clear previous output
    for pattern, support in sorted_patterns:
        output_text.insert(tk.END, f"{pattern}: {support}\n")

# Create main window
window = tk.Tk()
window.title("FP-Growth with Tkinter")

# Input Frame
input_frame = tk.Frame(window)
input_frame.pack(padx=10, pady=10)

tk.Label(input_frame, text="Transactions (comma-separated items per transaction):").pack(anchor=tk.W)
transactions_entry = scrolledtext.ScrolledText(input_frame, width=50, height=10)
transactions_entry.pack()

tk.Label(input_frame, text="Minimum Support (0-1):").pack(anchor=tk.W)
min_support_entry = tk.Entry(input_frame)
min_support_entry.insert(0, "0.5")  # Default value
min_support_entry.pack()

# Button to run FP-Growth
run_button = tk.Button(window, text="Run FP-Growth", command=run_fpgrowth)
run_button.pack(pady=10)

# Output Frame
output_frame = tk.Frame(window)
output_frame.pack()

output_text = scrolledtext.ScrolledText(output_frame, width=50, height=20)
output_text.pack()

window.mainloop()
