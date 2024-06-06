import tkinter as tk
from tkinter import messagebox

class TodoApp:
    def __init__(self, root):
        self.root = root
        self.root.title("To-Do List App")
        
        # Frame for the listbox and scrollbar
        self.frame = tk.Frame(self.root)
        self.frame.pack(pady=10)
        
        # Listbox to display tasks
        self.listbox = tk.Listbox(
            self.frame, 
            width=50, 
            height=10, 
            bd=0, 
            font=("Helvetica", 12), 
            selectbackground="#a6a6a6"
        )
        self.listbox.pack(side=tk.LEFT, fill=tk.BOTH)
        
        # Scrollbar for the listbox
        self.scrollbar = tk.Scrollbar(self.frame)
        self.scrollbar.pack(side=tk.RIGHT, fill=tk.BOTH)
        
        self.listbox.config(yscrollcommand=self.scrollbar.set)
        self.scrollbar.config(command=self.listbox.yview)
        
        # Entry widget to add new tasks
        self.entry = tk.Entry(
            self.root, 
            font=("Helvetica", 12)
        )
        self.entry.pack(pady=20)
        
        # Buttons frame
        self.button_frame = tk.Frame(self.root)
        self.button_frame.pack(pady=20)
        
        # Add Task button
        self.add_task_button = tk.Button(
            self.button_frame, 
            text="Add Task", 
            font=("Helvetica", 12), 
            command=self.add_task
        )
        self.add_task_button.pack(side=tk.LEFT, padx=20)
        
        # Delete Task button
        self.delete_task_button = tk.Button(
            self.button_frame, 
            text="Delete Task", 
            font=("Helvetica", 12), 
            command=self.delete_task
        )
        self.delete_task_button.pack(side=tk.LEFT, padx=20)

    def add_task(self):
        task = self.entry.get()
        if task != "":
            self.listbox.insert(tk.END, task)
            self.entry.delete(0, tk.END)
        else:
            messagebox.showwarning("Warning", "You must enter a task.")

    def delete_task(self):
        try:
            selected_task_index = self.listbox.curselection()[0]
            self.listbox.delete(selected_task_index)
        except:
            messagebox.showwarning("Warning", "You must select a task to delete.")

if __name__ == "__main__":
    root = tk.Tk()
    app = TodoApp(root)
    root.mainloop()
