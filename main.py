import tkinter as tk
from tkinter import filedialog, messagebox, ttk
from internshala_bot import apply_for_multiple_internships
from database import save_credentials

# Global variables for file paths
resume_path = ""
cover_letter_path = ""

def store_credentials():
    """Saves encrypted credentials."""
    email = entry_email.get()
    password = entry_password.get()

    if not email or not password:
        messagebox.showerror("Error", "Enter both email and password!")
        return

    save_credentials(email, password)
    messagebox.showinfo("Success", "Credentials saved securely!")

def browse_resume():
    """Allows users to select a PDF resume."""
    global resume_path
    file_path = filedialog.askopenfilename(filetypes=[("PDF files", "*.pdf")])
    if file_path:
        resume_path = file_path
        lbl_resume_path.config(text=f"Selected: {file_path}")

def browse_cover_letter():
    """Allows users to select a TXT cover letter."""
    global cover_letter_path
    file_path = filedialog.askopenfilename(filetypes=[("Text files", "*.txt")])
    if file_path:
        cover_letter_path = file_path
        lbl_cover_letter_path.config(text=f"Selected: {file_path}")

def start_application():
    """Starts internship applications."""
    max_apps = int(entry_max_apps.get())
    work_from_home = work_from_home_var.get()
    category = entry_category.get()

    if not resume_path or not cover_letter_path:
        messagebox.showerror("Error", "Select both Resume & Cover Letter before applying!")
        return

    progress_bar["value"] = 0
    root.update_idletasks()

    apply_for_multiple_internships(max_apps, work_from_home, category, resume_path, cover_letter_path, progress_bar)

# GUI
root = tk.Tk()
root.title("InstaFill - Internship Auto-Fill")

tk.Label(root, text="Internshala Email:").pack()
entry_email = tk.Entry(root)
entry_email.pack()

tk.Label(root, text="Internshala Password:").pack()
entry_password = tk.Entry(root, show="*")
entry_password.pack()

tk.Button(root, text="Save Credentials", command=store_credentials).pack(pady=5)

tk.Label(root, text="Select Resume (PDF):").pack()
btn_browse_resume = tk.Button(root, text="Browse", command=browse_resume)
btn_browse_resume.pack()
lbl_resume_path = tk.Label(root, text="No file selected")
lbl_resume_path.pack()

tk.Label(root, text="Select Cover Letter (TXT):").pack()
btn_browse_cover_letter = tk.Button(root, text="Browse", command=browse_cover_letter)
btn_browse_cover_letter.pack()
lbl_cover_letter_path = tk.Label(root, text="No file selected")
lbl_cover_letter_path.pack()

tk.Label(root, text="Max Applications:").pack()
entry_max_apps = tk.Entry(root)
entry_max_apps.pack()

tk.Label(root, text="Category (e.g., Python, Marketing):").pack()
entry_category = tk.Entry(root)
entry_category.pack()

work_from_home_var = tk.BooleanVar()
tk.Checkbutton(root, text="Work From Home", variable=work_from_home_var).pack()

progress_bar = ttk.Progressbar(root, orient="horizontal", length=300, mode="determinate")
progress_bar.pack(pady=10)

tk.Button(root, text="Start Application", command=start_application).pack(pady=5)

root.mainloop()
