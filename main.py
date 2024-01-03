import tkinter as tk
from main_window import setup_main_window
from student_treeview import setup_treeview
from student_form import setup_student_form

def main():
    # Create the main application window
    root = tk.Tk()
    
    # Set up the main window, including title and style
    setup_main_window(root)
    
    # Set up the Treeview widget and get a reference to it
    tree = setup_treeview(root)
    
    # Set up the form for adding and deleting student records, passing the Treeview as a reference
    setup_student_form(root, tree)
    
    # Start the Tkinter event loop
    root.mainloop()

if __name__ == '__main__':
    main()
