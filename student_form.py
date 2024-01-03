import tkinter as tk
from tkinter import ttk, messagebox
import database

def setup_student_form(root, tree):
    """Set up the form for adding and deleting student records."""

    # Function to populate data in Treeview
    def populate_data():
        """Populate the Treeview with data from the database."""
        for i in tree.get_children():
            tree.delete(i)
        for row in database.view_students():
            tree.insert('', tk.END, values=row)

    # Entry Frame for adding new records
    entry_frame = ttk.Frame(root)
    entry_frame.pack(pady=20)

    # Name Entry
    ttk.Label(entry_frame, text="Name:").grid(row=0, column=0, sticky=tk.W)
    name_entry = ttk.Entry(entry_frame)
    name_entry.grid(row=0, column=1)

    # Age Entry
    ttk.Label(entry_frame, text="Age:").grid(row=1, column=0, sticky=tk.W)
    age_entry = ttk.Entry(entry_frame)
    age_entry.grid(row=1, column=1)

    # Grade Entry
    ttk.Label(entry_frame, text="Grade:").grid(row=2, column=0, sticky=tk.W)
    grade_entry = ttk.Entry(entry_frame)
    grade_entry.grid(row=2, column=1)

    # Button Frame for add and delete buttons
    button_frame = ttk.Frame(root)
    button_frame.pack(pady=10)

    # Add Button Functionality
    def add_student():
        """Add a new student record to the database."""
        name = name_entry.get()
        age = age_entry.get()
        grade = grade_entry.get()
        if name and age and grade:
            try:
                database.add_student(name, int(age), grade)
                populate_data()
                name_entry.delete(0, tk.END)
                age_entry.delete(0, tk.END)
                grade_entry.delete(0, tk.END)
            except ValueError:
                messagebox.showerror("Error", "Invalid input for age. Please enter a number.")
            except Exception as e:
                messagebox.showerror("Error", str(e))
        else:
            messagebox.showwarning("Warning", "All fields are required")

    ttk.Button(button_frame, text="Add Record", command=add_student).grid(row=0, column=0)

    # Delete Button Functionality
    def delete_student():
        """Delete the selected student record from the database."""
        selected_item = tree.selection()
        if selected_item:
            item = tree.item(selected_item)
            record_id = item['values'][0]  # Get the ID of the selected record
            database.delete_student(record_id)
            populate_data()  # Refresh the Treeview with updated data
        else:
            messagebox.showwarning("Warning", "Please select a record to delete")

    ttk.Button(button_frame, text="Delete Record", command=delete_student).grid(row=0, column=1)

    # Refresh Button to reload data from the database
    ttk.Button(button_frame, text="Refresh Data", command=populate_data).grid(row=0, column=2)

    # Initially populate the Treeview with data from the database
    populate_data()
