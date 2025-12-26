import tkinter as tk
from tkinter import filedialog, messagebox
import pandas as pd 
import matplotlib.pyplot as mat
import math

last_sequence = []

def parse_collatz(val):
    val = val.replace(" ", "").lower()
    try:
        if "*" in val and "^" in val:
            base_part, rest = val.split("*")
            _, exponent_part = rest.split("^")
            
            # Use int() for the base if it has no decimal point
            # This avoids the 10^308 limit of floats!
            if "." in base_part:
                # If it's a decimal like 2.7, we handle it carefully
                # Multiply by 10^exp, then convert to int
                return int(float(base_part) * (10 ** int(exponent_part)))
            else:
                return int(base_part) * (10 ** int(exponent_part))
            
        return int(float(val))
    except (ValueError, IndexError, OverflowError):
        return None
def collatz():
    global last_sequence 
    try:
        n = parse_collatz(inpt.get())
        if n is None or n <= 0:
            result.config(text="Error: Enter a positive integer (> 0).", bg="black", fg="red")
            btn_export.pack_forget()
            btn_visualize.pack_forget()
            return
        last_sequence = [n]
        while n != 1:
            if n % 2 == 0: n //= 2
            else: n = 3 * n + 1
            last_sequence.append(n)
        sequence_str = ", ".join(map(str, last_sequence))
        # Check the actual number of steps in the list
        if len(last_sequence) >= 200: 
             result.config(text=f"Steps: {len(last_sequence)} | Max Value: {max(last_sequence)} \nSequence too long to display (Export for details).", bg="tomato", fg="black")
        else:
             sequence_str = ", ".join(map(str, last_sequence))
             result.config(text=f"Steps: {len(last_sequence)} | Max Value: {max(last_sequence)} \nSequence: {sequence_str}", bg="tomato", fg="black")
        btn_export.pack(pady=5)
        btn_visualize.pack(pady=5)
    except ValueError:
        result.config(text="Please enter a valid integer.", bg="black", fg="red")
        btn_export.pack_forget()
        btn_visualize.pack_forget()


def visualize_graph():
    global last_sequence
    if not last_sequence:
        return
    starting_number = last_sequence[0]
    

    is_massive = max(last_sequence) > 1e18

    mat.figure(figsize=(10, 6))
    
    if len(str(starting_number)) > 40 or len(last_sequence) > 200:
        manager = mat.get_current_fig_manager()
        try:
            manager.window.state('zoomed') 
        except AttributeError:
            manager.full_screen_toggle()
    
    if is_massive:
       mat.plot(last_sequence, color='royalblue', linewidth=1)
       mat.yscale('log')
       mat.ylabel("Value (log₁₀ scale)")
       mat.title(f"Collatz Path for {starting_number}\n(Logarithmic Scale)\nNote: display starts from highest number in sequence for convenience", pad=20)
    else:
        mat.plot(last_sequence, marker='o', linestyle='-', color='royalblue')
        mat.ylabel("Value")
        mat.title(f"Collatz Sequence for {starting_number}", pad=20)

    mat.xlabel("Steps")
    mat.grid(True, linestyle='--', alpha=0.7)

    if not is_massive:
        import matplotlib.ticker as ticker
        ax = mat.gca()
        formatter = ticker.ScalarFormatter(useMathText=True)
        formatter.set_scientific(True) 
        formatter.set_powerlimits((-3, 4)) 
        ax.yaxis.set_major_formatter(formatter)
    
    mat.show()
    btn_visualize.pack_forget()
    btn_export.pack_forget()
    result.config(text="Graph closed. Enter a new number to start again!", bg="turquoise")
    last_sequence = [] # Clear the data so it's ready for a fresh start
    inpt.delete(0, tk.END)
def export_csv():
    if not last_sequence:
        messagebox.showwarning("No Data", "Please click Submit first to generate a sequence!")
        return
    
    filepath = filedialog.asksaveasfilename(defaultextension=".csv", filetypes=[("CSV", "*.csv")])
    if filepath:
        df = pd.DataFrame({"Step": range(len(last_sequence)), "Value": last_sequence})
        df.to_csv(filepath, index=False)
        result.config(text="Data exported successfully!", bg="lime")


root=tk.Tk()
root.geometry("600x500")
root.title("Collatz Conjecture Visualizer")
root.config(bg="turquoise")
lbl=tk.Label(root,text="Enter a number and click Submit", bg="turquoise", fg="black")
lbl.pack()
inpt=tk.Entry(root)
inpt.pack()
btn=tk.Button(root,text="Submit",command=collatz, bg="royal blue",fg="black")
btn.pack()
result=tk.Label(root,text="",bg="turquoise", wraplength=580)
result.pack()
btn_export = tk.Button(root, text="Export CSV", command=export_csv, bg="forest green", fg="white")
btn_visualize = tk.Button(root, text="Visualize Graph", command=visualize_graph, bg="dark orange", fg="white")
root.mainloop()