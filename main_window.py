import tkinter as tk
from tkinter import ttk

def setup_main_window(root):
    """Set up the main window."""
    root.title('Student Database Management System')

    # Configure the style
    style = ttk.Style()
    style.theme_use('default')
    style.configure('Treeview', background='#D3D3D3', rowheight=25, fieldbackground='#D3D3D3')
    style.map('Treeview', background=[('selected', '#347083')])
