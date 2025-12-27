import tkinter as tk
from tkinter import filedialog, messagebox
import pandas as pd 
import matplotlib.pyplot as mat


last_sequence = []

def parse_collatz(val):
    val = val.replace(" ", "").lower()
    try:
        # Handle 2.7*10^64 style
        if "*10^" in val:
            base, exp = val.split("*10^")
            return int(float(base) * (10 ** int(exp)))
        # Handle exponentiation like 2**64 or 2.7*10**64
        elif "**" in val:
            base, exp = val.split("**")
            if "*10" in base:
                base_num = float(base.replace("*10", ""))
                return int(base_num * (10 ** int(exp)))
            else:
                return int(float(base) ** int(exp))
        # Handle simple exponentiation like 2^64
        elif "^" in val:
            base, exp = val.split("^")
            return int(float(base) ** int(exp))
        # Handle scientific notation like 2e64
        elif "e" in val:
            return int(float(val))
        # Plain numbers
        else:
            return int(float(val))
    except (ValueError, IndexError, OverflowError):
        return None
def collatz():
    global last_sequence 
    try:
        n = parse_collatz(inpt.get())
        if n is None or n <= 0:
            result.config(text="Error: Enter a positive integer and make it not larger than your RAM can handle", bg="black", fg="red")
            btn_export.pack_forget()
            btn_visualize.pack_forget()
            return
        last_sequence = [n]
        while n != 1:
            if n % 2 == 0: n //= 2
            else: n = 3 * n + 1
            last_sequence.append(n)
        
        # Check the actual number of steps in the list
        if len(last_sequence) >= 200 or max(last_sequence) > 1e18: 
             result.config(text=f"Steps: {len(last_sequence)} | Max Value: {max(last_sequence)} \nSequence too long to display (Export for details).", bg="tomato", fg="black")
        else:
             sequence_str = ", ".join(map(str, last_sequence))
             result.config(text=f"Steps: {len(last_sequence)} | Max Value: {max(last_sequence)} \nSequence: {sequence_str}", bg="tomato", fg="black")
        btn_export.pack(pady=5)
        btn_visualize.pack(pady=5)
    except ValueError:
        pass


def visualize_graph():
    global last_sequence
    if not last_sequence:
        return
    starting_number = last_sequence[0]
    

    is_massive = max(last_sequence) > 1e18

    fig, ax = mat.subplots()
    manager = fig.canvas.manager
    try:
        manager.window.state('zoomed')          # Windows
    except AttributeError:
        try:
            manager.full_screen_toggle()        # macOS/Linux fallback
        except AttributeError:
            pass
    if is_massive:
       ax.plot(last_sequence, color='royalblue', linewidth=1)
       ax.set_yscale('log')
       ax.set_ylabel("Value (log₁₀ scale)")
       ax.set_title(f"Collatz Path for {starting_number}\n(Logarithmic Scale)\nNote: display starts from highest number in sequence for convenience", pad=20)
    else:
        ax.plot(last_sequence, marker='o', linestyle='-', color='royalblue')
        ax.set_ylabel("Value")
        ax.set_title(f"Collatz Sequence for {starting_number}", pad=20)

    mat.xlabel("Steps")
    mat.grid(True, linestyle='--', alpha=0.7)

    if not is_massive:
        import matplotlib.ticker as ticker
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
lbl=tk.Label(root,text="Enter a number and click Submit\nStandard form and Exponential form are allowed", bg="turquoise", fg="black")
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