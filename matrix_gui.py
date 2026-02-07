import tkinter as tk
from tkinter import messagebox
import numpy as np

# -------------------- THEME COLORS --------------------
BG = "#0f172a"        # dark navy
CARD = "#1e293b"      # card background
BTN = "#38bdf8"       # cyan button
BTN_HOVER = "#0ea5e9"
TXT = "#e5e7eb"       # light text
ACCENT = "#22c55e"    # green

# -------------------- MAIN WINDOW --------------------
root = tk.Tk()
root.title("Matrix Calculator v2026")
root.geometry("600x650")
root.configure(bg=BG)
root.resizable(False, False)

# -------------------- TITLE --------------------
tk.Label(
    root,
    text="Matrix Calculator",
    font=("Segoe UI", 22, "bold"),
    fg=BTN,
    bg=BG
).pack(pady=10)

# -------------------- INPUT FRAME --------------------
frame = tk.Frame(root, bg=CARD)
frame.pack(padx=20, pady=10, fill="both")

def create_label(text):
    tk.Label(frame, text=text, fg=TXT, bg=CARD, font=("Segoe UI", 11)).pack(anchor="w", pady=5)

create_label("Matrix A (rows separated by new line, values by space)")
entry_A = tk.Text(frame, height=6, bg=BG, fg=TXT, insertbackground="white")
entry_A.pack(fill="x", pady=5)

create_label("Matrix B (rows separated by new line, values by space)")
entry_B = tk.Text(frame, height=6, bg=BG, fg=TXT, insertbackground="white")
entry_B.pack(fill="x", pady=5)

# -------------------- RESULT BOX --------------------
create_label("Result")
result_box = tk.Text(frame, height=8, bg=BG, fg=ACCENT)
result_box.pack(fill="x", pady=5)

# -------------------- MATRIX PARSER --------------------
def get_matrix(text_widget):
    try:
        lines = text_widget.get("1.0", "end").strip().split("\n")
        matrix = [list(map(float, line.split())) for line in lines]
        return np.array(matrix)
    except:
        messagebox.showerror("Error", "Invalid matrix format")
        return None

# -------------------- OPERATIONS --------------------
def add():
    A, B = get_matrix(entry_A), get_matrix(entry_B)
    if A is not None and B is not None:
        result_box.delete("1.0", "end")
        result_box.insert("end", A + B)

def multiply():
    A, B = get_matrix(entry_A), get_matrix(entry_B)
    if A is not None and B is not None:
        result_box.delete("1.0", "end")
        result_box.insert("end", A @ B)

def transpose():
    A = get_matrix(entry_A)
    if A is not None:
        result_box.delete("1.0", "end")
        result_box.insert("end", A.T)

def determinant():
    A = get_matrix(entry_A)
    if A is not None:
        result_box.delete("1.0", "end")
        result_box.insert("end", np.linalg.det(A))

def inverse():
    A = get_matrix(entry_A)
    if A is not None:
        result_box.delete("1.0", "end")
        result_box.insert("end", np.linalg.inv(A))

# -------------------- BUTTONS --------------------
btn_frame = tk.Frame(root, bg=BG)
btn_frame.pack(pady=15)

def make_button(text, cmd):
    return tk.Button(
        btn_frame,
        text=text,
        command=cmd,
        bg=BTN,
        fg="black",
        font=("Segoe UI", 11, "bold"),
        width=18,
        relief="flat",
        activebackground=BTN_HOVER
    )

make_button("A + B", add).grid(row=0, column=0, padx=8, pady=6)
make_button("A × B", multiply).grid(row=0, column=1, padx=8, pady=6)
make_button("Transpose A", transpose).grid(row=1, column=0, padx=8, pady=6)
make_button("Determinant A", determinant).grid(row=1, column=1, padx=8, pady=6)
make_button("Inverse A", inverse).grid(row=2, column=0, columnspan=2, pady=6)

# -------------------- FOOTER --------------------
tk.Label(
    root,
    text="© Shivjot Choudhary | v2026",
    fg="#94a3b8",
    bg=BG,
    font=("Segoe UI", 9)
).pack(side="bottom", pady=8)

# -------------------- RUN --------------------
root.mainloop()
