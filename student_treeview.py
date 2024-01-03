import tkinter as tk
from tkinter import ttk, messagebox
import database

def setup_treeview(root):
    """Set up the Treeview for displaying student records."""
    tree_frame = ttk.Frame(root)
    tree_frame.pack(pady=10)

    tree_scroll = ttk.Scrollbar(tree_frame)
    tree_scroll.pack(side=tk.RIGHT, fill=tk.Y)

    tree = ttk.Treeview(tree_frame, yscrollcommand=tree_scroll.set, selectmode='extended', columns=('ID', 'Name', 'Age', 'Grade'))
    tree.pack()

    tree_scroll.config(command=tree.yview)

    tree.column('#0', width=0, stretch=tk.NO)
    tree.column('ID', anchor=tk.W, width=120)
    tree.column('Name', anchor=tk.W, width=120)
    tree.column('Age', anchor=tk.CENTER, width=80)
    tree.column('Grade', anchor=tk.W, width=120)

    tree.heading('#0', text='', anchor=tk.W)
    tree.heading('ID', text='ID', anchor=tk.W)
    tree.heading('Name', text='Name', anchor=tk.W)
    tree.heading('Age', text='Age', anchor=tk.CENTER)
    tree.heading('Grade', text='Grade', anchor=tk.W)

    return tree
